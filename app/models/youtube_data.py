class YoutubeData: 
    def __init__(self , db) :
        self.db = db

    def insert_youtube_meta_data(self) : 
        meta_data  = {
            "video_title" : "xyz" , 
        }
        self.db.video_meta_data.insert_one(meta_data)

    def insert_many_record(self , temp) : 
        self.db.video_meta_data.insert_many(temp)
        