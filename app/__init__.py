from flask import Flask 
from app.routes import main
from app.models import YoutubeData
from app.mongo_client import MonogoDatabase



def init_mongo_db():
    mongo_databse_obj = MonogoDatabase()
    db = mongo_databse_obj._init_client()
    return db



def create_app(config_file='settings.py'):
    app = Flask(__name__)
    app.config.from_pyfile(config_file)
    app.register_blueprint(main)
    app.db = init_mongo_db()

    yt = YoutubeData(app.db)

    #print(yt)
    #yt.insert_youtube_meta_data()



    return app


 