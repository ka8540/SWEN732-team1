from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

from src.utilities.swen_344_db_utils import *
from src.api.example_api import *
from src.api.UserAPI import UserAPI, UsersAPI, AuthAPI 

app = Flask(__name__) #create Flask instance
CORS(app) #Enable CORS on Flask server to work with Nodejs pages
api = Api(app) #api router

# user accounts api
api.add_resource(UserAPI, '/users/<string:id>')
api.add_resource(UsersAPI, '/users')
api.add_resource(AuthAPI, '/auth/<string:action>')


if __name__ == '__main__':
    print("Loading db");
    exec_sql_file('data/setup_tables.sql');
    print("Starting flask");
    app.run(debug=True), #starts Flask

    