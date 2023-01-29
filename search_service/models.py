import pymongo

class DatabaseClass:
    def __init__(self , client) :
        self.mongo_client = client 
    
    def get_db_instance(self):
        return self.mongo_client.video_meta_data

    def create_index(self):
        self.mongo_client.video_meta_data.create_index(
            [("video_title", pymongo.TEXT) , ("description" , pymongo.TEXT)]
        )
    