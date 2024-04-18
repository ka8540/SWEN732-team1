from flask import Flask, jsonify, make_response, request
from flask_restful import Api, Resource, reqparse


# Import only necessary functions from the utilities and price database module
try:
    from src.utilities.swen_344_db_utils import exec_get_all
    from src.db.price_conversion import get_convert_price_to_canadian, get_convert_price_to_indian
except ImportError:
    from db.price_conversion import get_convert_price_to_canadian, get_convert_price_to_indian
    from utilities.swen_344_db_utils import exec_get_all

    
    
class Canadian(Resource):
    def get(self):
        price_usd = request.headers.get('Price')
        price_cad = get_convert_price_to_canadian(price_usd)
        return price_cad
        
class Indian(Resource):
    def get(self):
        price_usd = request.headers.get('Price')
        price_inr = get_convert_price_to_canadian(price_usd)
        return price_inr