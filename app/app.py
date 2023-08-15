from flask import Flask, request, jsonify
from pymongo import MongoClient

app = Flask(__name__)

app.config['MONGO_URI'] = 'URI'
app.config['MONGO_DBNAME'] = 'Database Name'
