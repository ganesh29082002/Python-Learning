# read_records.py
from db_connection import create_connection

def read_records():
    connection = create_connection()
    cursor = connection.cursor()
    
    select_query = "SELECT * FROM customers"
    cursor.execute(select_query)
    records = cursor.fetchall()
    
    for row in records:
        print(f"ID: {row[0]}, Name: {row[1]}, Email: {row[2]}, Age: {row[3]}")
    
    cursor.close()
    connection.close()

# Example usage
read_records()
