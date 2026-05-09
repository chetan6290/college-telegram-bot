from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)

db = client[DB_NAME]

# Collections
notes_collection = db["notes"]

print("MongoDB Connected Successfully")