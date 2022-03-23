import mysql
import mysql.connector
from MySQLdb import IntegrityError
import html.parser


class Post:
    cursor = 0  # global variable database cursor

    def __init__(self, ids, title, body, user, image):
        self.id = ids
        self.title = title
        self.body = body
        self.user = user
        self.image = image
        self.mariadb_connection = mysql.connector.connect(user='root', password='Palidhje',
                                                          database='website');  # instantiation of the database connectivity
        self.cursor = self.mariadb_connection.cursor()  # instantiation of db link

    def insert(self):
        result = False
        print("Trying to store data")




        try:  # trying to execute the query
            query = f"""
                INSERT INTO post(title, body, user, image) 
                VALUES ('{self.title}', '{self.body}', {self.user}, '{self.image}');"""
            print(f"The Query = {query}")
            self.cursor.execute(query)
            self.mariadb_connection.commit()  # usually auto_commit is inactive, and it is needed to do committing
            print("Data are stored perfectly.")
            result = True;
        except ValueError:
            self.mariadb_connection.rollback()  # if there is a problem transaction fails
            print("Data are not stored.")
        except IntegrityError:
            print("Unique Constrains exception.")
        return result


