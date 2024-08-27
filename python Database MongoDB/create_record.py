from db_connection import get_db_connection

def create_customer(name, email, age):
    db = get_db_connection()
    collection = db["customers"]
    customer = {"name": name, "email": email, "age": age}
    collection.insert_one(customer)
    print(f"Inserted customer: {customer}")

if __name__ == "__main__":
    create_customer("John Doe", "john.doe@example.com", 28)
