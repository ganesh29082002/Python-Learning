from db_connection import get_db_connection

def update_customer(name, new_age):
    db = get_db_connection()
    collection = db["customers"]
    collection.update_one({"name": name}, {"$set": {"age": new_age}})
    print(f"Updated customer {name} to age {new_age}")

if __name__ == "__main__":
    update_customer("John Doe", 29)
