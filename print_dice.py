from pymongo import MongoClient,mongo_client

client = MongoClient("localhost", 27017, maxPoolSize=50)
DB= client.get_database('Dataset')
collection=DB.get_collection('dicelogs')

for document in collection.find():
    print(document)
    