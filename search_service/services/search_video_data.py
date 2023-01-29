import requests 
from settings import YOUTUBE_API_KEY
from flask import current_app as app
from json_encoder import MongoJSONEncoder 

def get_video_data(request):
    print(request)
    page_limit = int(request.args.get("page_limit"))
    offset = int(request.args.get("offset"))


    output = app.db.find().sort("publish_time", -1).skip(page_limit * (offset - 1)).limit(page_limit)

    data = MongoJSONEncoder().encode(list(output))

    for x in output : 
        print(type(x))

    return data
