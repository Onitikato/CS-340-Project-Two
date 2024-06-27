import pymongo
from pymongo import MongoClient

class AnimalShelter(object):
    def __init__(self):
        USER = 'aacuser'
        PASS = 'password'
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30531
        DB = 'aac'
        COL = 'animals'
        self.client = MongoClient(f'mongodb://{USER}:{PASS}@{HOST}:{PORT}')
        self.database = self.client[DB]
        self.collection = self.database[COL]

    def create(self, data):
        if data:
            result = self.collection.insert_one(data)
            return result.inserted_id
        else:
            raise ValueError("Nothing to save, because data parameter is empty")

    def read(self, readData=None):
        if readData:
            data = self.collection.find(readData)
        else:
            data = self.collection.find({})
        return list(data)

    def update(self, query, update_data):
        if query and update_data:
            result = self.collection.update_one(query, {'$set': update_data})
            return result.modified_count
        else:
            raise ValueError("Query and update data must be provided")

    def delete(self, query):
        if query:
            result = self.collection.delete_one(query)
            return result.deleted_count
        else:
            raise ValueError("Query must be provided")

