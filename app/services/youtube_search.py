import requests 
from app.settings import YOUTUBE_API_KEY

def post_youtube_search():
    search_url = 'https://www.googleapis.com/youtube/v3/search'

    search_params = {
        'key' :  YOUTUBE_API_KEY , 
        'q' : 'cricket' , 
        'part' : 'snippet' , 
        'maxResults' : 50 ,
        'order' : 'date' , 
        'type' : 'video' , 
    }

    r = requests.get(search_url , params=search_params)

    print(r.text)

    return r.text

