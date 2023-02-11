import requests 
from settings import YOUTUBE_API_KEY
from flask import current_app as app
from json_encoder import MongoJSONEncoder 


def validate_request(data):
    for key , value in data.items() : 
        if key not in ["page_limit" , "offset"] : 
            return  400 , "Bad Request" 
        if not value.isnumeric() :
            return  400 , "Bad Request"
        if key == "offset" and int(value) <= 0 :
            return  400 , "Bad Request"
    return 200, "ok"


def get_video_data(request):
    print(request.args)

    data = request.args.to_dict()

    status_code , reason = validate_request(data)
    
    if status_code == 400 :
        return "Bad Request" , 400
    

    page_limit = int(request.args.get("page_limit"))
    offset = int(request.args.get("offset"))


    output = app.db.find().sort("publish_time", -1).skip(page_limit * (offset - 1)).limit(page_limit)

    data = MongoJSONEncoder().encode(list(output))

    for x in output : 
        print(type(x))

    return data
