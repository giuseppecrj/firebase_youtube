from requests_toolbelt.adapters import appengine
from flask import Flask
from flask_restful import Api, Resource
from googleapiclient.discovery import build
from firebase_admin import credentials
from firebase_admin import db
import requests
import firebase_admin


# setup
appengine.monkeypatch()
app = Flask(__name__)
api = Api(app)

# firebase
cred = credentials.Certificate('./service_account.json')
firebase_admin.initialize_app(cred, {
    'databaseURL': 'FIREBASE_URL'
})
print db.reference().child('test').get()


# youtube
DEVELOPER_KEY = "API_KEY"
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=DEVELOPER_KEY)
search_response = youtube.search().list(
    q='Hello',
    part='id,snippet',
    maxResults=5
  ).execute()
print search_response # ResponseNotReady



# routes
class SampleRoute(Resource):
    def get(self):
        return {'youtube': 'v3'}
api.add_resource(SampleRoute, '/')