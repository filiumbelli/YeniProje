from pymongo import MongoClient

MONGO_URI = "mongodb://localhost"

client = MongoClient(MONGO_URI)

db = client["employees"]
collection = db["employees"]

product_one = {"name": "mouse"}
product_two = {"name": "monitor"}

# collection.insert_one()
# collection.insert_many()
results = collection.find()
