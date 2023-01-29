import requests 

from flask import Blueprint , render_template , request 
from services import post_youtube_search as ys
from services import search_video_data as svd

main = Blueprint('main' , __name__ )

@main.route("/")
def index():
   return render_template('index.html')

@main.route("/search" , methods=["GET"])
def get_video_search_params():
   return ys.post_youtube_search()

@main.route("/get-data" , methods=["GET"])
def get_video_search():
   return svd.get_video_data(request)

