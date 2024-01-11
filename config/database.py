import os
from pymongo import MongoClient

class Database:
    def __init__(self):
        username = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
        password = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')
        self.client = MongoClient(f'mongodb://{username}:{password}@bloger-gdsc-mongo-1:27017/')
        #dev
        #self.client = MongoClient('mongodb://localhost:27017/')

    def set_database(self, database):
        self.db = self.client[database]

    def set_collection(self, collection):
        return self.db[collection]

mongo_connection = Database()