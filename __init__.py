from flask import (Flask, request, jsonify, session)
import json, os
from urllib import response
from flask_restful import Api, Resource
#from requests import put, get
app = Flask(__name__)
api = Api(app)

class Timeline(Resource):
    def get(self):
        return "This is a test"
    
    def get_user(self,user_id):
        return user_id

class Login(Resource):
    def get(self):
        """
        """
        return "You will be logged in now"

class Signup(Resource):
    def post(self):
        #1. get posted data by the user
        postedData = request.get_json()
        #2. data is verified by app or web Gui
        #3. get the data
        username = postedData['username']
        password = postedData['password']

        return {"This shit works": "for now"}
        pass
#### api Resources
api.add_resource(Timeline, '/')
api.add_resource(Login, '/login')
api.add_resource(Signup, '/signup')

if __name__ == '__main__':
    app.run(debug=True)