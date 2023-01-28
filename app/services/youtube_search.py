import requests 
from app.settings import YOUTUBE_API_KEY
from app.models import YoutubeData
from . import *

def post_youtube_search():
    search_url = 'https://www.googleapis.com/youtube/v3/search'

    search_params = {
        'key' :  YOUTUBE_API_KEY , 
        'q' : 'cricket' , 
        'part' : 'snippet' , 
        'maxResults' : 50 ,
        'order' : 'date' , 
        'type' : 'video' , 
        'publishedAfter' : '2023-01-28T17:43:00.813891Z',
        'publishedBefore' : '2023-01-28T17:51:11.765597Z'
    }

    r = requests.get(search_url , params=search_params)

    result = r.json() 
    items = result["items"]
    print(items[0])
    result_dict = {}
    result = []
    for item in items : 
        result_dict = {}
        result_dict.update({'video_id' : item['id']['videoId']})
        result_dict.update({'channel_id' : item['snippet']['channelId']})
        result_dict.update({'video_title' :  item['snippet']['title']})
        result_dict.update({'description' :  item['snippet']['description']})
        result_dict.update({'publish_time' :  item['snippet']['publishTime']})
        result.append(result_dict)

    print(result)

    yt = YoutubeData(db)

    yt.insert_many_record(result)



    return r.json()

