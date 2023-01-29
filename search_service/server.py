# from flask import Flask 
from routes import main
from mongo_client import MonogoDatabase
from models import DatabaseClass 




def init_mongo_db():
    mongo_databse_obj = MonogoDatabase()
    db = mongo_databse_obj._init_db()
    return db


from flask import Flask

app = Flask(__name__)
app.register_blueprint(main)
client = init_mongo_db()
db_obj = DatabaseClass(client)
app.db = db_obj.get_db_instance()
db_obj.create_index()


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)




# @celery.task
# def my_background_task(arg1, arg2):
#     print(arg1,arg2)
#     return result

# task = my_background_task.apply_async(args=[10, 20])


#    app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
#     app.config['CELERY_RESULT_BACKEND'] = 'redis://localhost:6379/0'
#     celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
#     celery.conf.update(app.config)
#     print(celery)