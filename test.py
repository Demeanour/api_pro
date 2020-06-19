from flask import Flask
from flask_restful import Resource, Api, reqparse
app = Flask(__name__)
api = Api(app)

class Index(Resource):

    def get(self):
        """
        1. get token: user_id
        2. get user_id subscribed groups
        3. create a timeline json object
        4. send object to the user 

        """
        return {'title': 'This is a test'}

class Login(Resource):
    def get(self):
        """
        """
        return "You will be logged in now"

api.add_resource(Index, "/")
api.add_resource(Login, "/login")

if __name__ == '__main__':
    app.run(debug=True, port=2500)

