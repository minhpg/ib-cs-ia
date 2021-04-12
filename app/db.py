from mongoengine import *
import app.config as config

connect(config.MONGO_DB)

class User(Document):
    username = StringField(required=True)
    password = StringField(required=True)
    user_id = StringField(required=True)

class Post(Document):
    pass


    