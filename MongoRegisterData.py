from pymongo import MongoClient

MONGO_URI = "mongodb://localhost"

client = MongoClient(MONGO_URI)

employee_Db = client["database"]
employee_Collection = employee_Db["employee"]

admin_Db = client["Secret"]
admin_Collection = admin_Db["admin"]

product_one = {"name": "mouse"}
product_two = {"name": "monitor"}

# collection.insert_one()
# collection.insert_many()

for datas in employee_Collection.find():
    print(datas.values())

for datas in admin_Collection.find():
    print(datas.values())
    print(datas.get("username"))
    print(datas.get("password"))

