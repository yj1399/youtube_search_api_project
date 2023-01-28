from flask import Flask 
from app.routes import main
from app.mongo_client import MonogoDatabase





def init_mongo_db():
    mongo_databse_obj = MonogoDatabase()
    db = mongo_databse_obj._init_db()
    return db



def create_app(config_file='settings.py'):
    app = Flask(__name__)

     
    app.config.from_pyfile(config_file)
    app.register_blueprint(main)
    client = init_mongo_db()
    db_obj = DatabaseClass(client)
    
    return app


# @celery.task
# def my_background_task(arg1, arg2):
#     print(arg1,arg2)
#     return result

# task = my_background_task.apply_async(args=[10, 20])


   # app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
    # app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
    # celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
    # celery.conf.update(app.config)
    # print(celery)