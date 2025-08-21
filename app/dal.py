from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

class Dal:

    uri = "mongodb+srv://IRGC:iraniraniran@iranmaldb.gurutam.mongodb.net/"
    
    def __init__(self):
        # Create a new client and connect to the server
        self.open_connection()

    def open_connection(self):
        try:
            conn = MongoClient(self.uri, server_api=ServerApi('1'))
            print("The connection created")
            return conn
        except Exception as e:
            print(e)
