from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27018/royaldrie"
# MONGO_URI = "mongodb://localhost:27019/royaldrie"


def connection():
    try:
        client = MongoClient(MONGO_URI)

        databases = client.list_database_names()

        print("Connected to MongoDB!")
        print("Databases:", databases)

    except Exception as e:
        print("Failed to connect:", e)


def create_db():
    try:
        client = MongoClient(MONGO_URI)
        db = client["royaldrie"]
        collection = db["my_collection"]

        sample_document = {"name": "Test Item", "value": 123}
        collection.insert_one(sample_document)

        print("Collection and document created successfully!")
        print("Collections in 'royaldrie':", db.list_collection_names())

    except Exception as e:
        print("Failed to connect or create collection:", e)


create_db()
connection()
