import pymongo

client = pymongo.MongoClient("mongodb+srv://AjitVikram:Ajitvikmongo123@clusterajit1.vzy4tbg.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name" : "ajitvikram",
    "email": "ajit.intell@gmail.com",
    "surname":"singh"

}

db1 = client["mongotest1"]
coll = db1["test1"]
coll.insert_one(d)