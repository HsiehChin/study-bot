from pymongo import MongoClient
import os

CONF = {}


def setup():
    global CONF
    CONF["DB"] = MongoClient(os.environ.get("MONGO_URI", ""))["studyDB"]
