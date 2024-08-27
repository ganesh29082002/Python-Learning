# update_record.py
from db_connection import create_connection

def update_record(customer_id, new_email, new_age):
    connection = create_connection()
    cursor = connection.cursor()
    
    update_query = """
    UPDATE customers
    SET email = %s, age = %s
    WHERE id = %s
    """
    data = (new_email, new_age, customer_id)
    cursor.execute(update_query, data)
    connection.commit()
    
    print(f"Record with ID {customer_id} updated successfully")
    cursor.close()
    connection.close()

# Example usage
update_record(1, "new.email@example.com", 35)
