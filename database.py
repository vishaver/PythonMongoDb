# URL = "mongodb://username:password@hostname:PORT/FLASK1?replicaSet=test"
# client = pymongo.MongoClient(URL)
# db = client['FLASK1']
# collection = db['user']
# test = collection.find()
# for j in test:
#     print(j["first_name"])

import pymongo
class Database():
    URL = "mongodb://username:password@hostname:PORT/FLASK1?replicaSet=test" #Replace this URL with specific mongo DB client.
    DATABASE = None

    @staticmethod
    def initilize():
        print("Initializing DB connection")
        client = pymongo.MongoClient(Database.URL)
        Database.DATABASE = client['FLASK1']

    @staticmethod
    def insert(collection,data):
        print("Inserting data to DB")
        Database.DATABASE[collection].insert(data)

    @staticmethod
    def find(collection,query):
        print("Finding all contented in DB")
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def find_one(collection,query):
        print("Finding single data entry in DB")
        return Database.DATABASE[collection].find_one(query)