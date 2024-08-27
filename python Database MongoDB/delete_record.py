from db_connection import get_db_connection

def delete_customer(name):
    db = get_db_connection()
    collection = db["customers"]
    collection.delete_one({"name": name})
    print(f"Deleted customer with name {name}")

if __name__ == "__main__":
    delete_customer("John Doe")
