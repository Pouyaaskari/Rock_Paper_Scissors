import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017", serverSelectionTimeoutMS=5000)
db = client["game"]

try:
    print("DB connected")
except Exception:
    print("Unable to connect to the server.")