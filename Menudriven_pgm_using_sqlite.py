import sqlite3
try:
    sqliteConnection = sqlite3.connect('Hospital_db.db')
    cursor = sqliteConnection.cursor()
    print("Database created and Successfully Connected to SQLite")

    sqlite_select_Query = "select sqlite_version();"
    cursor.execute(sqlite_select_Query)
    record = cursor.fetchall()
    print("SQLite Database Version is: ", record)
    #cursor.close()

except sqlite3.Error as error:
    print("Error while connecting to sqlite", error)


try:
    sqliteConnection = sqlite3.connect('Hospital_db.db')
    sqlite_create_table_query = '''CREATE TABLE Patients_Records(
                                reg_no TEXT PRIMARY KEY,
                                name TEXT NOT NULL,
                                date_of_birth datetime,
                                gender TEXT NOT NULL,
                                address TEXT NOT NULL,
                                Phone TEXT NOT NULL);'''

    #cursor = sqliteConnection.cursor()
    #print("Successfully Connected to SQLite")
    cursor.execute(sqlite_create_table_query)
    sqliteConnection.commit()
    print("SQLite table created")

   #cursor.close()

except sqlite3.Error as error:
    print("Error while creating a sqlite table", error)


def insertVaribleIntoTable(reg_no, name, date_of_birth, gender, address, Phone):
    try:
        #sqliteConnection = sqlite3.connect('Hospital_db.db')
        #cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """INSERT INTO Patients_Records
                          (reg_no, name, date_of_birth, gender, address, Phone) 
                          VALUES (?, ?, ?, ?, ?, ?);"""

        data_tuple = (reg_no, name, date_of_birth, gender, address, Phone)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqliteConnection.commit()
        print("Python Variables inserted successfully into Patients_Records table")

        #cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert Python variable into sqlite table", error)


def viewTable():
    try:
        #sqliteConnection = sqlite3.connect('Hospital_db.db')
        #cursor = sqliteConnection.cursor()
        print("Connected to SQLite")

        sqlite_insert_with_param = """SELECT * FROM Patients_Records;"""

        #data_tuple = (reg_no, name, date_of_birth, gender, address, Phone)
        cursor.execute(sqlite_insert_with_param)
        details = cursor.fetchall()
        sqliteConnection.commit()
        print(details)
        print("Successfully viewed Patients_Records table")

        #cursor.close()

    except sqlite3.Error as error:
        print("Failed to open Patients_Records table", error)
 

i=1
while(i):
  option = int(input("\n\nChoose any option:\n\n 1. Enter the record of the new patient \n2. List the details of all patients \n3. Exit\n"))
  if(option==1):
    print("\n\nWelcome to the Hospital_FamJam")
    a = input("\nEnter the Registration_id: ")
    b = input("\nEnter the Name: ")
    c = input("\nEnter the dob: ")
    d = input("\nEnter the gender: ")
    e = input("\nEnter the Address: ")
    f = input("\nEnter the Phone no: ")
    insertVaribleIntoTable(a,b,c,d,e,f)
  elif(option==2):
    viewTable()
  elif(option==3):
    i=0
  else:
    print("\nEnter a valid option\n\n")
    
        
sqliteConnection.close()
print("The SQLite connection is closed")