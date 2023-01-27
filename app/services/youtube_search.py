import requests 
from app.settings import YOUTUBE_API_KEY

def get_youtube_video_information():
    search_url = 'https://www.googleapis.com/youtube/v3/search'

    search_params = {
        'key' :  YOUTUBE_API_KEY , 
        'q' : 'learn python' , 
        'part' : 'snippet' , 
        'maxResults' : 20 
    }

    r = requests.get(search_url , params=search_params)

    print(r.text)

    return r.text
    