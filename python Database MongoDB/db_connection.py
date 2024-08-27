from pymongo import MongoClient

def get_db_connection():
    # Create a connection to MongoDB
    client = MongoClient("mongodb://localhost:27017/")
    # Select the database
    db = client["mydatabase"]
    return db
