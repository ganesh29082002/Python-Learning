from db_connection import get_db_connection

def read_customers():
    db = get_db_connection()
    collection = db["customers"]
    results = collection.find()
    for doc in results:
        print(doc)

if __name__ == "__main__":
    read_customers()
