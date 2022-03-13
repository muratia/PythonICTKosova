import mysql
import mysql.connector
from MySQLdb import IntegrityError


class User:
    cursor = 0  # global variable database cursor

    def __init__(self):  # class constructor

        self.id = "";  # incialization of the variable
        self.firstName = "";  # incialization of the variable
        self.lastName = "";  # incialization of the variable
        self.email = "";  # incialization of the variable
        self.password = "";  # incialization of the variable
        self.phone = "";  # incialization of the variable

        # full constructor

    def __init__(self, id=None, username=None, firstName=None, lastName=None, email=None,
                 password=None, phone=None):
        self.id = id;  # passing value
        self.username = username;  # passing value
        self.firstName = firstName;  # passing value
        self.lastName = lastName;  # passing value
        self.email = email;  # passing value
        self.password = password;  # passing value
        self.phone = phone;  # passing value
        self.mariadb_connection = mysql.connector.connect(user='root', password='Palidhje',
                                                          database='website');  # instantiation of the database connectivity
        self.cursor = self.mariadb_connection.cursor()  # instantiation of the cursor and storing

    def insert(self):  # helper method to store the data into the database
        result = False;
        try:  # trying to execute the query

            self.cursor.execute(
                """
                INSERT INTO users(username, firstName, lastName, email, password, phone) 
                VALUES (%s, %s, %s, %s, %s, %s)""",
                (self.username, self.firstName, self.lastName, self.email, self.password, self.phone))
            self.mariadb_connection.commit()  # usually auto_commit is inactive, and it is needed to do committing
            print("Data are stored perfectly.")
            result = True;
        except ValueError:
            self.mariadb_connection.rollback()  # if there is a problem transaction fails
            print("Data are not stored.")
        except IntegrityError:
            print("Unique Constrains exception.")
        return result

    def load(self, username):
        user = User
        try:  # trying to execute the query

            self.cursor.execute(
                """
                SELECT `users`.`id`,
    `users`.`username`,
    `users`.`firstName`,
    `users`.`lastName`,
    `users`.`email`,
    `users`.`password`,
    `users`.`phone`
FROM `website`.`users`
where  `users`.`username` = %s;""",
                (self.username, 1))
            user = self.cursor.fetchone()
            print("Data are stored perfectly.")
            result = True;
        except ValueError:
            self.mariadb_connection.rollback()  # if there is a problem transaction fails
            print("Data are not stored.")
        except IntegrityError:
            print("Unique Constrains exception.")
        return user


