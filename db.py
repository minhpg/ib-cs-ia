import pymongo
import config
client = pymongo.MongoClient(config.MONGO_SERVER)
database = client[config.MONGO_DB]

    