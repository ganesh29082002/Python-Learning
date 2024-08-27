# delete_record.py
from db_connection import create_connection

def delete_record(customer_id):
    connection = create_connection()
    cursor = connection.cursor()
    
    delete_query = "DELETE FROM customers WHERE id = %s"
    data = (customer_id,)
    cursor.execute(delete_query, data)
    connection.commit()
    
    print(f"Record with ID {customer_id} deleted successfully")
    cursor.close()
    connection.close()

# Example usage
delete_record(1)
