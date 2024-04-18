from flask import make_response
from flask_restful import Resource
from flask import jsonify
from flask_restful import request
from flask_restful import reqparse
import json

try:
    from src.utilities.swen_344_db_utils import *
    from src.db.converted_price import *
except:
    from utilities.swen_344_db_utils import *
    from db.converted_price import *

class IndianConvertedPricesAPI(Resource):
    def get(self):
        prices = get_indian_converted_prices()
        return make_response(jsonify(prices), 200)

class CanadianPricesAPI(Resource):
    def get(self):
        prices = get_canadian_prices()
        return make_response(jsonify(prices), 200)

class AllPricesAPI(Resource):
    def get(self):
        prices = get_all_prices()
        return make_response(jsonify(prices), 200)

