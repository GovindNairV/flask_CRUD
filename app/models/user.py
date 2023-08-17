from flask_pymongo import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from utils.validation import Validation

class User:
    def __init__(self, db):
        self.db = db

    # Function to get all the users from the User collection
    def get_all_users(self):
        return self.db.User.find()
    
    # Function to get a user from the User collection by the specified id
    # also useful in other methods like update and delete to verify if the user exists
    def find_user_by_id(self, id):
        return self.db.User.find_one({'_id': ObjectId(id)})
    
    # Function to create a new user in the User collection
    def create_user(self, name, email, password):
        # Validation
        validation_error = self._validate_user_input(name, email, password)
        if validation_error:
            return {'message': validation_error}, 400

        # Check if user with email already exists
        if self.find_user_by_email(email):
            return {'message': 'User with this email already exists'}, 400

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Create user
        new_user = {
            "name": name,
            "email": email,
            "password": hashed_password
        }
        inserted_id = self.db.User.insert_one(new_user).inserted_id

        return {'message': 'User created successfully', 'id': str(inserted_id)}, 201

    # Function to update a user in the User collection by specified it
    def update_user(self, id, name, email, password):
        # Validation
        validation_error = self._validate_user_input(name, email, password)
        if validation_error:
            return {'message': validation_error}, 400

        # Find the user to be updated
        user = self.find_user_by_id(id)
        if not user:
            return {'message': 'User not found'}, 404

        # Check if another user with the new email already exists
        if email != user['email'] and self.find_user_by_email(email):
            return {'message': 'Another user with this email already exists'}, 400

        # Hash the password
        hashed_password = generate_password_hash(password)

        # Update user
        update_query = {
            '$set': {
                'name': name,
                'email': email,
                'password': hashed_password
            }
        }
        
        self.db.User.update_one({'_id': ObjectId(id)}, update_query)

        return {'message': 'User updated successfully'}, 200
    
    # Function to delete a user in the User collection by specified it
    def delete_user(self, id):
        user = self.find_user_by_id(id)
        if not user:
            return {'message': 'User not found'}, 404

        self.db.User.delete_one({'_id': ObjectId(id)})
        return {'message': 'User deleted successfully'}, 200

    # Function to check if a user already exists with the given email id
    def find_user_by_email(self, email):
        return self.db.User.find_one({'email': email})
    
    # Function to utilize the Validation utility to check for validity of the request
    def _validate_user_input(self, name, email, password):
        validation_error = Validation.validate_user_input(name, email, password)
        return validation_error