import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")

conn = MongoClient(MONGO_URL, server_api=ServerApi('1'),serverSelectionTimeoutMS=3000)

db = conn.Notes
collection = db["Notes_coll"]

