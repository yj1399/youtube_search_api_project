from flask import current_app as app
from json_encoder import MongoJSONEncoder 

def validate_request(data):

    for key , value in data.items() :
        if key not in ["search_tag"] :
            return 400 , "Bad Request"
        if len(value) <= 0 :
            return 400 , "Bad Request"
        return 200 , "ok"

def get_video_title_search(request):

    data = request.args.to_dict()

    status_code , reason = validate_request(data)

    if status_code == 400 :
        return 400 , "Bad Request"
    

    search_tag = request.args.get("search_tag")
    output = app.db.find( { "$text" : { "$search" : f"{search_tag}" } } )
    print(output)
    data = MongoJSONEncoder().encode(list(output))
    print(request)
    return data
