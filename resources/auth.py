from models.user import User
from flask_restful import Resource, Api
from flask import request

class LoginResource(Resource):
    def post(self):
        body = request.get_json()
        user = User.query.filter_by(username=body.get('username')).first()
        if user is None:
            return {"error":"User is not found."}
        return {"username":user.username, "password":user.password}



class RegisterResource(Resource):
    def post(self):
        return "This is post."

    def get(self):
        return "This is get."


def init_resource(app):
    api = Api(app, prefix="/auth")

    api.add_resource(LoginResource, "/login")
    api.add_resource(RegisterResource, "/register")


