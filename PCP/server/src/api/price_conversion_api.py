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
        price_usd_str = request.headers.get('Price')
        print(price_usd_str, "USD Prices!!")
        try:
            price_usd = float(price_usd_str)
            price_cad = get_convert_price_to_canadian(price_usd)
            print(price_cad,"price_result!!")
            print(jsonify({'price_cad': price_cad}))
            return jsonify({'price_cad': price_cad})
        except (ValueError, TypeError):
            return make_response(jsonify({'error': 'Invalid price value'}), 400)

class Indian(Resource):
    def get(self):
        price_usd_str = request.headers.get('Price')
        try:
            price_usd = float(price_usd_str)
            print(price_usd)
            price_inr = get_convert_price_to_indian(price_usd)
            print("INR PRICE RESULT:",price_inr)
            return jsonify({'price_inr': price_inr})
        except (ValueError, TypeError):
            return make_response(jsonify({'error': 'Invalid price value'}), 400)