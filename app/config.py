from dotenv import dotenv_values

config = dotenv_values(".env")

MONGO_SERVER = config['MONGO_SERVER']

MONGO_DB = config['MONGO_DB']

SECRET = config['SECRET']