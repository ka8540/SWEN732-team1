from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

from .utilities.swen_344_db_utils import *
from api.login_api import *
from api.signup_api import *
from api.user_detail_api import *
from api.logout_api import *
app = Flask(__name__) #create Flask instance
CORS(app) #Enable CORS on Flask server to work with Nodejs pages
api = Api(app) #api router

api.add_resource(SignUpApi,'/signUp')
api.add_resource(LoginAPI,'/login')
api.add_resource(UserDetail,'/userdetail')
api.add_resource(LogoutAPI,'/logout')
if __name__ == '__main__':
    print("Loading db")
    exec_sql_file('data/UserDetail.sql')
    print("Starting flask")
    app.run(debug=True), #starts Flask

