from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv


app = Flask(__name__)
CORS(app)
api = Api(app)

load_dotenv()

from src.api.login_api import LoginAPI
from src.api.signup_api import SignupAPI

# Add resources
api.add_resource(LoginAPI, '/login')
api.add_resource(SignupAPI, '/signup')

if __name__ == '__main__':
    app.run(debug=True)
