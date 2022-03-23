import configparser as configparser
import json
import os
import uuid
from xml.sax.saxutils import escape, unescape

import mysql as mysql
import mysql.connector
from flask import *  # importing flask (Install it using# )
from flask_ckeditor import *
from werkzeug.utils import secure_filename

from models.Post import Post
from models.User import User

# escape() and unescape() takes care of &, < and >.
html_escape_table = {
    '"': "&quot;",
    "'": "&apos;",
}
html_unescape_table = {v: k for k, v in html_escape_table.items()}


def html_escape(text):
    return escape(text, html_escape_table)


def html_unescape(text):
    return unescape(text, html_unescape_table)


app = Flask(__name__)  # initialising flask
ckeditor = CKEditor(app)


@app.route('/files/<filename>')
def uploaded_files(filename):
    path = app.config['UPLOADED_PATH']
    return send_from_directory(path, filename)


def upload_fail(message):
    pass


@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('upload')
    extension = f.filename.split('.')[1].lower()
    if extension not in ['jpg', 'gif', 'png', 'jpeg']:
        return upload_fail(message='Image only!')
    unique_filename = str(uuid.uuid4())
    f.filename = unique_filename + '.' + extension
    f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    url = url_for('uploaded_files', filename=f.filename)
    return upload_success(url=url)


config = configparser.ConfigParser()

config.read('./config/config.ini')
upload = config.get("UPLOAD_FOLDER", "UPLOAD_FOLDER")
app.config["SQLALCHEMY_DATABASE_URI"] = config.get("SQLAlchemy", "DATABASE_URI")
app.config["SECRET_KEY"] = "This_Is_A_S3Cr3T"
app.config.from_object(config)

uploadFolder = config["UPLOAD_FOLDER"]["UPLOAD_FOLDER"]
basedir = uploadFolder

app.config['CKEDITOR_SERVE_LOCAL'] = False
app.config['CKEDITOR_HEIGHT'] = 400
app.config['CKEDITOR_FILE_UPLOADER'] = 'upload'
app.config['UPLOADED_PATH'] = os.path.join(basedir, 'uploads')


@app.route("/")  # defining the routes for the home() function (Multiple routes can be used as seen here)
@app.route("/home")
def home():
    return render_template("home.html")  # rendering our home.html contained within /templates


@app.route("/logout")
def logout():
    username = None
    session["user"] = None
    return render_template("login.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        User.load = staticmethod(User.load)
        if 'username' not in request.form:
            flash('No username part')

        if 'pwd' not in request.form:
            flash('No password part')
        username = request.form["username"]
        password = request.form["pwd"]

        u = loadUserByUsername(username)

        if u is not None:
            if u[5] == password:
                session["user"] = u

                return render_template("/home.html", user=u)
        else:
            return render_template("login.html", errors="Incorrect data")
    return render_template("/login.html")


def getPhotos(user: User = None) -> []:
    """

      :return:
      :return:
      :param user:User
      """
    records = None
    try:
        connection = mysql.connector.connect(
            host=config["mysql"]["host"], db=config["mysql"]["db"],
            user=config["mysql"]["user"], password=config["mysql"]["passwd"])

        sql = f"SELECT  `images`.`filename`,  `images`.`alt`, `images`.`title`," \
              f"`images`.`userId` FROM `website`.`images` WHERE `images`.`userId`  = '{user[0]}';"

        # print(sql)
        cursor = connection.cursor()

        cursor.execute(sql)
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)
        cursor.close()

    except mysql.connector.Error as e:
        print("Failed to insert record into filename table {}".format(e))
        try:
            print(f"MySQL Error [%d]: {e.args[0]}, {e.args[1]}")
            return None
        except IndexError:
            print(f"MySQL Error: {str(e)}")
            return None
        except TypeError as e:
            print(e)
            return None
        except ValueError as e:
            print(e)
            return None
    return records


@app.route("/profile", methods=["POST", "GET"])
def profile():
    photos = []
    photosCount = 0
    user = session["user"]
    photos = getPhotos(user)
    photosCount = len(photos)
    posts = getPostings()

    postCount = len(posts)
    posts2 = posts

    return render_template("profile.html", user=user, Photos=photos,
                           PhotosCount=photosCount,
                           Posts=posts2, PostCount=postCount)  # rendering our about.html contained within /templates


@app.route('/tregime', methods=["GET"])
def tregime():
    if session.get("user") is not None:

        user = session["user"]
        posts = getPostings()
        postCount = len(posts)

        posts2 = []
        for i in range(1, len(posts)):
            idP = posts[i][0]
            title = posts[i][1]
            body = unescape(posts[i][2])
            user = posts[i][3]
            image = posts[i][4]
            item = [idP, title, body, user, image]
            postA = Post(idP, title, body, user, image)

            posts2.append(item)

        return render_template("post.html", user=user, Posts=posts2, PostCount=postCount)
    else:
        flash("Not logged in")
        return render_template("login.html")


@app.route("/post-add")
def postAdd():
    return render_template("posts-add.html")


@app.route("/addapost", methods=["POST"])
def addPost():
    if session.get("user") is not None:

        user = session["user"]

        if user is not None:
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']

            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            else:
                filename = secure_filename(file.filename)
                upload_folder = "." + uploadFolder
                fileName = upload_folder + filename
                file.save(os.path.join(upload_folder, filename))

                title = request.form.get("title")
                body = request.form.get("body")
                ids = 0
                post = Post(ids, title, body, user[0], fileName)

                if post.insert():
                    return render_template("/tregime", user=user, result="Data stored"),
                    # rendering our about.html contained within /templates

        else:
            return render_template("addapost.html")
    else:
        return render_template("/login")


@app.route("/posting/<id>", methods=["GET"])
def postings(id):
    print(f"Printing parameter id = {id}.")
    posting = getPosting(id)
    print(f"Print the posting: {id} {posting}")

    return json.dumps(posting)


@app.route("/account", methods=["POST", "GET"])  # defining the routes for the account() funtion
def account():
    usr = "<User Not Defined>"  # Creating a variable usr

    if session.get("user") is not None:

        user = session["user"]
        if user is not None:  # Checking if the method of request was post
            return render_template("account.html",
                                   username=user)  # rendering our about.html contained within /templates
    else:
        return render_template("/login")


@app.route("/about", methods=["GET"])  # defining the routes for the account() funtion
def about():
    usr = "<User Not Defined>"  # Creating a variable usr

    return render_template("about.html", username=usr)  # rendering our about.html contained within /templates


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        user = session["user"]
        if user is not None:
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            alt = request.form.get("alt")
            title = request.form.get("title")
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            else:
                filename = secure_filename(file.filename)
                upload_folder = "." + uploadFolder;
                fileName = upload_folder + filename
                file.save(os.path.join(upload_folder, filename))

                print(f"Trying to store data {fileName} in database mysql")
                print(f"Alt {alt}")
                print(f"Title {title}")
                if insertIntoDB(upload_folder + filename, alt, title, user[0]):
                    result = "Data stored successfully"
                else:
                    result = "Sorry, data are not stored successfully"

        return render_template("upload-success.html", result=result)
    else:
        return render_template("upload.html")


def insertIntoDB(filename, alt, title, userId):
    """

    :param userId:
    :param title:
    :param alt:
    :param filename:
    """
    result = False
    try:
        connection = mysql.connector.connect(
            host=config["mysql"]["host"], db=config["mysql"]["db"],
            user=config["mysql"]["user"], password=config["mysql"]["passwd"])

        sql = f"INSERT INTO `website`.`images` (`id`, `filename`, `published`, `alt`, `title`,`userId`) VALUES " \
              f"(null, '{filename}', 1, '{alt}', '{title}','{userId}');"

        cursor = connection.cursor()

        cursor.execute(sql)
        connection.commit()
        cursor.close()
        result = True
    except mysql.connector.Error as e:
        print("Failed to insert record into filename table {}".format(e))
        try:
            print(f"MySQL Error [%d]: {e.args[0]}, {e.args[1]}")
            return None
        except IndexError:
            print(f"MySQL Error: {str(e)}")
            return None
        except TypeError as e:
            print(e)
            return None
        except ValueError as e:
            print(e)
            return None
    return result


def loadUserByUsername(username):
    """

    :param username:
    :return: User
    """
    connection = mysql.connector.connect(host=config["mysql"]["host"], db=config["mysql"]["db"],
                                         user=config["mysql"]["user"], password=config["mysql"]["passwd"])

    try:  # trying to execute the query
        cursor = connection.cursor()
        query = """SELECT `users`.`id`,
`users`.`username`,
`users`.`firstName`,
`users`.`lastName`,
`users`.`email`,
`users`.`password`,
`users`.`phone`
FROM `website`.`users`
where  `users`.`username` = %s;"""

        cursor.execute(query, [username])
        user = cursor.fetchone()
    except ValueError:

        print("Data are not stored.")

    return user


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":

        result = ""
        pwd = request.form["pwd"]
        username = request.form["username"]
        firstName = request.form["firstName"]
        lastName = request.form["lastName"]
        email = request.form["email"]
        phone = request.form["phone"]
        p = User(username=username, firstName=firstName, lastName=lastName,
                 email=email, password=pwd, phone=phone)
        if p.insert():
            result = "Data are stored properly"
        else:
            result = "Sorry, try again trying to create the account"
        return render_template("registering-successfully.html", result=result)
    else:
        return render_template("register.html")


def getPostings():
    if session.get("user") is not None:
        user = session["user"]

        posts = loadPosts()
        postCount = len(posts)
    return posts


def getPosting(pid):
    post = loadAPost(pid)
    return post


def loadAPost(id=0):
    connection = mysql.connector.connect(host=config["mysql"]["host"], db=config["mysql"]["db"],
                                         user=config["mysql"]["user"], password=config["mysql"]["passwd"])

    cursor = connection.cursor()
    query = f"""SELECT * from post where {id};"""
    print(f"Printing the query = {query}.")
    cursor.execute(query)

    result = cursor.fetchone()

    return result


def loadPosts():
    user = session["user"]
    result = []

    connection = mysql.connector.connect(host=config["mysql"]["host"], db=config["mysql"]["db"],
                                         user=config["mysql"]["user"], password=config["mysql"]["passwd"])

    cursor = connection.cursor()

    cursor.execute(f"""SELECT * from post where user = {user[0]};""")

    result = cursor.fetchall()
    return result


@app.route("/album/{pid}/{name}")
def createAlbum(pid, name):
    header = {
        "Content-Type": "application/json",
        "User-Agent": "Windows",
        "X-Line-Mid": 1,
        "x-lct": "",
    }
    payload = {
        "type": "image",
        "title": name
    }
    r = request.post(
        "http://" + self.host + "/mh/album/v3/album?count=1&auto=0&homeId=" + pid,
        headers=header,
        data=json.dumps(payload)
    )
    return r.json()


def page_not_found(e):
    return render_template('404.html'), 404


def internal_issue(e):
    return render_template("500.html"), 500


if __name__ == "__main__":  # checking if __name__'s value is '__main__'. __name__ is a python environment variable
    # whose value will always be '__main__' till this is the first instance of app.py running
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_issue)
    app.run(debug=True, port=4949)  # running flask (Initialised on line 4)
