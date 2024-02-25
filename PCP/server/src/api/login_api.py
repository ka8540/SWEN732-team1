from flask_restful import Resource
from flask import jsonify
from flask_restful import request
from flask_restful import reqparse
import json
from ..utilities.swen_344_db_utils import *
from api.login import *

class LoginAPIS(Resource):
    def get(self):
        return jsonify(list_info_items())

