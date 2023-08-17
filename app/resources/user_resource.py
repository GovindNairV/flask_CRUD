from flask_restful import Resource, reqparse
from bson.json_util import dumps
from models.user import User

class UserResource(Resource):
    def __init__(self, db):
        self.user_manager = User(db)

    def get(self, id=None):
        if id:
            user = self.user_manager.find_user_by_id(id)
            if user:
                return dumps(user), 200
            return {'message': 'User not found'}, 404
        else:
            users = self.user_manager.get_all_users()
            return dumps(users), 200

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('pwd', required=True)
        args = parser.parse_args()

        name = args['name']
        email = args['email']
        password = args['pwd']

        response = self.user_manager.create_user(name, email, password)
        return response

    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument('name', required=True)
        parser.add_argument('email', required=True)
        parser.add_argument('pwd', required=True)
        args = parser.parse_args()

        name = args['name']
        email = args['email']
        password = args['pwd']

        response = self.user_manager.update_user(id, name, email, password)
        return response

    def delete(self, id):
        response = self.user_manager.delete_user(id)
        return response
