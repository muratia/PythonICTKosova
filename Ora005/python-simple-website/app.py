import configparser as configparser
import os

import mysql as mysql
import mysql.connector
from flask import *  # importing flask (Install it using# )
from werkzeug.utils import secure_filename

from User import User

app = Flask(__name__)  # initialising flask

config = configparser.ConfigParser()

config.read('./config/config.ini')
upload = config.get("UPLOAD_FOLDER", "UPLOAD_FOLDER")
app.config["SQLALCHEMY_DATABASE_URI"] = config.get("SQLAlchemy", "DATABASE_URI")
app.config["SECRET_KEY"] = "This_Is_A_S3Cr3T"
app.config.from_object(config)
Database1 = 'mysql'
Database2 = 'postgresql'
host = config['mysql']['host']
user = config['mysql']['user']
passwd = config['mysql']['passwd']
database = config['mysql']['db']
uploadFolder = config["UPLOAD_FOLDER"]["UPLOAD_FOLDER"]

host2 = config['postgresql']['host']
user2 = config['postgresql']['user']
passwd2 = config['postgresql']['passwd']
db2 = config['postgresql']['db']

app.config.from_object(config)


@app.route("/")  # defining the routes for the home() function (Multiple routes can be used as seen here)
@app.route("/home")
def home():
    return render_template("home.html")  # rendering our home.html contained within /templates


def getPhotos():
    """

      :param filename:
      """
    records = None
    try:
        connection = mysql.connector.connect(
            host=config["mysql"]["host"], db=config["mysql"]["db"],
            user=config["mysql"]["user"], password=config["mysql"]["passwd"])

        sql = f"SELECT  `images`.`filename`,  `images`.`alt`, `images`.`title` FROM `website`.`images`;"
        print(sql)
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
    usr = "<User Not Defined>"  # Creating a variable usr
    if request.method == "POST":  # Checking if the method of request was post
        usr = request.form["name"]  # getting the name of the user from the form on home page
        if not usr:  # if name is not defined it is set to default string
            usr = "<User Not Defined>"
        photos = getPhotos()
        print("Printing photos")

        photosCount = len(photos)

    return render_template("profile.html", username=usr, Photos=photos,
                           PhotosCount=photosCount)  # rendering our about.html contained within /templates


@app.route("/account", methods=["POST", "GET"])  # defining the routes for the account() funtion
def account():
    usr = "<User Not Defined>"  # Creating a variable usr
    if request.method == "POST":  # Checking if the method of request was post
        usr = request.form["name"]  # getting the name of the user from the form on home page
        if not usr:  # if name is not defined it is set to default string
            usr = "<User Not Defined>"
    return render_template("account.html", username=usr)  # rendering our about.html contained within /templates


@app.route("/about", methods=["GET"])  # defining the routes for the account() funtion
def about():
    usr = "<User Not Defined>"  # Creating a variable usr

    return render_template("about.html", username=usr)  # rendering our about.html contained within /templates


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':

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

            print(f"Trying to store data {fileName} in database {Database1}")
            print(f"Alt {alt}")
            print(f"Title {title}")
            if insertIntoDB(upload_folder + filename, alt, title):
                result = "Data stored successfully"
            else:
                result = "Sorry, data are not stored successfully"

        return render_template("upload-success.html", result=result)
    else:
        return render_template("upload.html")


def insertIntoDB(filename, alt, title):
    """

    :param title:
    :param alt:
    :param filename:
    """
    result = False
    try:
        connection = mysql.connector.connect(
            host=config["mysql"]["host"], db=config["mysql"]["db"],
            user=config["mysql"]["user"], password=config["mysql"]["passwd"])
        sql = f"INSERT INTO `website`.`images` (`id`, `filename`, `published`, `alt`, `title`) VALUES " \
              f"(null, '{filename}', 1, '{alt}', '{title}');"
        print(f"File name: {filename}")

        print(f"SQL {sql}")
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


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(uploadFolder, filename)


def loadUserByPassword(username):
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


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        User.load = staticmethod(User.load)
        if 'username' not in request.form:
            flash('No username part')

        if 'pwd' not in request.form:
            flash('No password part')
        username = request.form["username"];
        password = request.form["pwd"];

        u = loadUserByPassword(username)
        print(f"User = {u}")
        pwd = u[5]
        print(f"Pwd = {pwd}")
        if pwd == password:
            return render_template("/home.html", username=u)
        else:
            return render_template("login.html", errors="Incorrect data")
    return render_template("login.html")


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
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


def page_not_found(e):
    return render_template('404.html'), 404


def internal_issue(e):
    return render_template("500.html"), 500


if __name__ == "__main__":  # checking if __name__'s value is '__main__'. __name__ is a python environment variable
    # whose value will always be '__main__' till this is the first instance of app.py running
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_issue)
    app.run(debug=True, port=4949)  # running flask (Initalised on line 4)
