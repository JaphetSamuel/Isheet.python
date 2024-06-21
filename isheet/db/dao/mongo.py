from pymongo import MongoClient

from isheet.settings import settings

client = MongoClient(settings.MONGODB_URI)
db = client.interventions
