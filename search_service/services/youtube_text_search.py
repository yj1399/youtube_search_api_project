from flask import current_app as app
from json_encoder import MongoJSONEncoder 

def get_video_title_search(request):
    output = app.db.find( { "$text" : { "$search" : "cricket" } } )
    print(output)
    data = MongoJSONEncoder().encode(list(output))
    print(request)
    return data
