from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter:
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, username: str, password: str, host: str, port: str, database: str, collection):
        # Initializing the MongoClient. This helps to
        # access the MongoDB databases and collections.
        # The username, password, host, port, 
        # database name, and collection name are left 
        # to the user of this class to specify
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (username, password, host, port))
        self.database = self.client['%s' % (database)]
        self.collection = self.database['%s' % (collection)]

    # Complete this create method to implement the C in CRUD.
    # Returns true on successful insertion, false otherwise
    def create(self, data) -> bool:
        if data is not None:
            self.database.animals.insert_one(data) # data should be dictionary
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

    # Create method to implement the R in CRUD
    # Returns either
    # a list of animals that fit the query (potentially zero)
    # or an empty list on failure
    def read(self, query: dict) -> list:
        try:
            return list(self.collection.find(query))
        except:
            return list()

    # Method may be used to update any documents
    # within the animal collection that match the given query
    # Returns the number of modified documents
    def update(self, query: dict, update: dict) -> int:
        result: UpdateResult = self.collection.update_many(query, update)
        return result.modified_count

    # Method may be used to delete any documents
    # within the animal collection that match the given query
    # Returns the number of deleted documents
    def delete(self, query: dict) -> int:
        result: DeleteResult = self.collection.delete_many(query)
        return result.deleted_count
