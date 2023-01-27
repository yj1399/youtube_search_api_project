from os import getenv

YOUTUBE_API_KEY = getenv("YOUTUBE_API_KEY")
MONGO_DATABASE = {
    "HOST" : getenv("DB_HOST") , 
    "PORT" : getenv("DB_PORT") , 
    "USER_NAME" : getenv("USER_NAME") ,
    "PASSWORD" : getenv("PASSWORD") ,
    "DB_NAME" : getenv("DB_NAME")
    #app.config['MONGO_URI'] = "mongodb+srv://yrs_1399:" + urllib.parse.quote("Yash@1972")+ "@cluster0.q91npcb.mongodb.net/?retryWrites=true&w=majority"
}

