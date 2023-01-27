import requests 

from flask import Blueprint , render_template
from app.settings import YOUTUBE_API_KEY
from app.services import youtube_search as ys

main = Blueprint('main' , __name__ )

@main.route("/")
def index():
   print(YOUTUBE_API_KEY)
   return render_template('index.html')

@main.route("/search" , methods=["GET"])
def get_video_search_params():
   return ys.get_youtube_video_information()

