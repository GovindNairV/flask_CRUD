from flask import Flask
from flask_pymongo import PyMongo
from flask_restful import Api
from resources.user_resource import UserResource
import os

app = Flask(__name__)
api = Api(app)

mongo_uri = os.environ.get('MONGO_URI')
# mongo_uri = "mongodb://localhost:27017/CoRider"

if not mongo_uri:
    raise ValueError("MONGO_URI environment variable is not set.")
app.config['MONGO_URI'] = mongo_uri
mongo = PyMongo(app)

@app.route('/')
def home():
    return "<p>Flask API<p>"

api.add_resource(UserResource, '/users', '/users/<string:id>', resource_class_kwargs={'db': mongo.db})

if __name__ == "__main__":
    app.run(debug=True, port=5001)

