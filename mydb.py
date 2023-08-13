import mysql.connector


database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        auth_plugin="mysql_native_password",
    )

cursorObject=database.cursor()

    # create the database if it does not exist
cursorObject.execute("CREATE DATABASE kunal")
cursorObject.fetchone()

print("all done")

