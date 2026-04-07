from pymongo import MongoClient

uri = "mongodb://caiodb:caio123@ac-3gjyj1w-shard-00-00.wnew7tz.mongodb.net:27017,ac-3gjyj1w-shard-00-01.wnew7tz.mongodb.net:27017,ac-3gjyj1w-shard-00-02.wnew7tz.mongodb.net:27017/?ssl=true&replicaSet=atlas-13e1a6-shard-0&authSource=admin&appName=Cluster0"

client = MongoClient(uri)

db = client["test"]
collection = db["test"]

collection.insert_one({"teste": "ok"})

print("Conectou e inseriu!")

client.close()