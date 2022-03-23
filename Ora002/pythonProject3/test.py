# coding=utf8
# importimi i ndërlidhësit të mysql dhe riemërtimi i saj si mariadb
import mysql.connector as mariadb


# Klasa Person
class Person:
    cursor = 0;  # ndryshore globale kursori i bazës së të dhënave
    sleeping = 0;  # ndryshore globale ndryshore e cila e ruan gjendjen e fjetur

    mariadb_connection = 0;  # deklarimi i ndryshorës globale për lidhjen me bazën e të dhënave

    def __init__(self):  # konstruktori i klasës
        self.sleeping = 0;  # rivendosja e gjendjes së zgjuar
        self.personalID = "";  # pastrimi i ndryshores
        self.employeeName = "";  # pastrimi i ndryshores
        self.employeeJobDescription = "";  # pastrimi i ndryshores
        self.employeeAddress = "";  # pastrimi i ndryshores
        self.employeeCity = "";  # pastrimi i ndryshores
        self.employeePhone = "";  # pastrimi i ndryshores

    # konstruktori i plotë
    def __init__(self, personalID=None, employeeName=None, employeeJobDescription=None, employeeAddress=None,
                 employeeCity=None, employeePhone=None):
        self.personalID = personalID;  # pasimi i vlerës
        self.employeeName = employeeName;  # pasimi i vlerës
        self.employeeJobDescription = employeeJobDescription;  # pasimi i vlerës
        self.employeeAddress = employeeAddress;  # pasimi i vlerës
        self.employeeCity = employeeCity;  # pasimi i vlerës
        self.employeePhone = employeePhone;  # pasimi i vlerës
        self.mariadb_connection = mariadb.connect(user='root', password='Palidhje',
                                                  database='flowershop');  # krijimi i lidhjes me db
        self.cursor = self.mariadb_connection.cursor();  # krijimi i kursorit dhe bartja në ndryshoren globale

    def insert(self):  # metodë për futjen e të dhënave në bazën e të dhënave
        try:  # provon ta ekzekutojë strukturën

            self.cursor.execute("INSERT INTO employee(  " +
                                " personalID, " +
                                "employeeName, " +
                                "employeeJobDescription," +
                                " employeeAddress, " +
                                "employeeCity, " +
                                "employeePhone) VALUES (%s, %s, %s, %s, %s, %s)", (
                                    self.personalID,
                                    self.employeeName,
                                    self.employeeJobDescription,
                                    self.employeeAddress,
                                    self.employeeCity,
                                    self.employeePhone));
            self.mariadb_connection.commit();  # rëndom auto_commit është e pasivizuar dhe duhet bërë commit
            print("Data are stored perfectly.");
        except ValueError:
            self.mariadb_connection.rollback();  # nëse ka ndodhur ndonjë problem transaksioni dështon
            print("Data are not stored.");
        return;

    def sleep(self):  # metodë për të nisur fjetjen
        if self.sleeping == 0:  # kontrollon nëse personi është i zgjuar
            print("Person " + self.employeeName + " is sleeping");
            self.sleeping = 1;  # e vë gjendjen 1 te self.sleeping që do të thotë personi është duke fjetur
        else:  # përndryshe
            print("Person " + self.employeeName + " is already sleeping");
        return;

    def wakeup(self):  # metodë për të nisur zgjimin
        if (self.sleeping == 1):  # kontrollon nëse personi është i fjetur
            self.sleeping = 0;  # e vë gjendjen 0 te self.sleeping që do të thotë i zgjuar
            print("Person " + self.employeeName + " is awake.");
        else:  # përndryshe
            print("Person " + self.employeeName + " is not sleeping to be woken up");

    def walk(self):  # metodë për të nisur zgjimin
        if (self.sleeping == 0):  # kontrollon nëse personi është i zgjuar
            print("Person " + self.employeeName + " is walking");
        else:  # përndryshe
            print("Person " + self.employeeName + " can't walk he is sleeping");
        return;

    def run(self):  # metodë për të nisur vrapimin
        if (self.sleeping == 0):  # kontrollon nëse personi është i zgjuar
            print("Person " + self.employeeName + " is running");
        else:  # përndryshe
            print("Person " + self.employeeName + " can't run he is sleeping");
        return

    def load(self):
        try:  # provon ta ekzekutojë strukturën

            self.cursor.execute("SELECT * FROM employee;")
            data = self.cursor.fetchall()
            print("Data are loaded perfectly.");
        except ValueError:
            self.mariadb_connection.rollback();  # nëse ka ndodhur ndonjë problem transaksioni dështon
            print("Data are not loaded.")
        return data




# inicializimi i ndryshores p me instancën e klasës Person
p = Person(employeeName="Ahmet", employeeJobDescription="Programer");
# p.employeeName = "Ahmet"; # caktimi i emrit


p.sleep();
p.walk();
p.wakeup();
p.walk();
p.run();
p.insert();

data = p.load()

print(data)