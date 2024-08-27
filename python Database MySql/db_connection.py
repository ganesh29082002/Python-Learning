import mysql.connector as myConn

def create_connection():
    connection = myConn.connect(
        host="localhost",
        user="root",
        password="",
        database="mydatabase"
    )
    return connection