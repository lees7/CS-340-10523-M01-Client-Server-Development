from pymongo import MongoClient

class AnimalShelter(object):
    """CRUD operations for Animal collection in MongoDB"""

    def __init__(self, username, password):
        HOST = "localhost"
        PORT = 27017
        DB = "AAC"
        COL = "animals"

        uri = f"mongodb://{username}:{password}@localhost:27017/?authSource=admin"

        self.client = MongoClient(uri)
        self.database = self.client[DB]
        self.collection = self.database[COL]

    # CREATE
    def create(self, data):
        if data:
            return self.collection.insert_one(data).acknowledged
        else:
            raise Exception("Nothing to save, data is empty")

    # READ
    def read(self, criteria=None):
        if criteria is None:
            criteria = {}
        return list(self.collection.find(criteria, {"_id": 0}))

    # UPDATE
    def update(self, query, new_values):
        if not query or not new_values:
            raise Exception("Update parameters cannot be empty")
        result = self.collection.update_many(query, {"$set": new_values})
        return result.modified_count

    # DELETE
    def delete(self, query):
        if not query:
            raise Exception("Delete query cannot be empty")
        result = self.collection.delete_many(query)
        return result.deleted_count