# create_record.py
from db_connection import create_connection

def create_customers_table():
    connection = create_connection()
    cursor = connection.cursor()
    
    # SQL to create the customers table if it does not exist
    create_table_query = """
    CREATE TABLE IF NOT EXISTS customers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        age INT
    );
    """
    
    cursor.execute(create_table_query)
    connection.commit()
    print("Checked for table 'customers' and created it if it didn't exist.")
    
    cursor.close()
    connection.close()

create_customers_table()

def create_record(name, email, age):
    connection = create_connection()
    cursor = connection.cursor()
    
    insert_query = """
    INSERT INTO customers (name, email, age)
    VALUES (%s, %s, %s)
    """
    data = (name, email, age)
    cursor.execute(insert_query, data)
    connection.commit()
    
    print("Record inserted successfully")
    cursor.close()
    connection.close()

# Example usage
create_record("Alice Johnson", "alice.johnson@example.com", 30)
