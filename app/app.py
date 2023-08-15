from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from bson.json_util import dumps
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
import os

app = Flask(__name__)

mongo_uri = os.environ.get('MONGO_URI')
# mongo_uri = "mongodb://localhost:27017/CoRider"

if not mongo_uri:
    raise ValueError("MONGO_URI environment variable is not set.")

app.config['MONGO_URI'] = mongo_uri

mongo = PyMongo(app)

@app.route('/')
def home():
    return "<p>hello world<p>"

# Get all users
@app.route('/users', methods=['GET'])
def get_users():
    users = mongo.db.User.find()
    resp = dumps(users)
    return resp

# Get a particular user by ID
@app.route('/users/<id>', methods=['GET'])
def get_user(id):
    user = mongo.db.User.find_one({'_id': ObjectId(id)})
    resp = dumps(user)
    return resp

# Create a user
@app.route('/users', methods=['POST'])
def create_user():
    # Implement logic to create a new user
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']

    if _name and _email and _password and request.method == 'POST':
        _hashed_password = generate_password_hash(_password)

        id = mongo.db.User.insert_one({"name":_name,"email": _email, "password": _hashed_password})

        resp = jsonify("User created Successfully!")

        resp.status_code = 200

        return resp
    
    else:
        return not_found()

# Update a particular user
@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    _id = id
    _json = request.json
    _name = _json['name']
    _email = _json['email']
    _password = _json['pwd']
    
    if _name and _email and _password and request.method == "PUT":
        _hashed_password = generate_password_hash(_password)

        filter_query = {'_id': ObjectId(_id)} if ObjectId.is_valid(_id) else {'id': _id}

        # Construct the update query
        update_query = {
            '$set': {
                'name': _name,
                'email': _email,
                'password': _hashed_password
            }
        }  
        mongo.db.User.update_one(filter_query, update_query)

        resp = jsonify("User Updated Successfully!")

        resp.status_code = 200

        return resp
    
    else:
        return not_found()

# Delete a user by ID
@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    mongo.db.User.delete_one({'_id':ObjectId(id)})
    resp = jsonify("User Deleted Successfully!")

    resp.status_code = 200

    return resp

# Handling Errors
@app.errorhandler(404)
def not_found(error = None):
    message = {
        'status': 404,
        'message': 'Not Found' + request.url
    }
    resp = jsonify(message)

    resp.status_code = 404

    return resp


if __name__ == "__main__":
    app.run(debug  = True, port=5001)

