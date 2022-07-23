import pymongo

client = pymongo.MongoClient("mongodb+srv://Akshayhm:akku2001@akshay.0k99w.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
    "name":"akshay",
    "email" : "akku0378@gmail.com",
    "surname" : "kumar"
}
db1 = client['mongotest']
coll = db1['test']
coll.insert_one(d )