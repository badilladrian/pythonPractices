import MySQLdb

def getAllRows():
    try:
        connection = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Franco2!2!",  # your password
                     db="app")        # name of the data base

        cursor = connection.cursor()
        print("Connected to MySQL")

        MySQL_select_query = """SELECT * from clockinclockout"""
        cursor.execute(MySQL_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("HarmonID: ", row[0])
            print("Full Name: ", row[1])
            print("Worked Day: ", row[2])
            print("PaidHours: ", row[13])
            print("\n")

        cursor.close()
    except MySQLdb.Error as error:
        print("Failed to read data from table", error)
    finally:
        if (connection):
            connection.close()
            print("The MySQL connection is closed")

getAllRows()


def insertRow(arguments):
    try:
        connection = MySQLdb.connect(host="localhost",    # your host, usually localhost
                     user="root",         # your username
                     passwd="Franco2!2!",  # your password
                     db="app")        # name of the data base

        cursor = connection.cursor()
        print("Connected to MySQL")

        MySQL_select_query = """SELECT * from clockinclockout"""
        cursor.execute(MySQL_select_query)
        records = cursor.fetchall()
        print("Total rows are:  ", len(records))
        print("Printing each row")
        for row in records:
            print("HarmonID: ", row[0])
            print("Full Name: ", row[1])
            print("Worked Day: ", row[2])
            print("PaidHours: ", row[13])
            print("\n")

        cursor.commit()

        cursor.close()

    except MySQLdb.Error as error:
        print("Failed to write data from table", error)
    finally:
        if (connection):
            connection.close()
            print("The MySQL connection is closed")
