from flask import Flask, jsonify, make_response
from flask_restful import Api, Resource, reqparse

# Import only necessary functions from the utilities and price database module
try:
    from src.utilities.swen_344_db_utils import exec_get_all
    from src.db.prices import get_prices_by_product, get_all_prices
except ImportError:
    from utilities.swen_344_db_utils import exec_get_all
    from db.prices import get_prices_by_product, get_all_prices
    
    
class PricesByProduct(Resource):
    def get(self, product_id):
        prices = get_prices_by_product(product_id)
        return jsonify([{'PriceID': price[0], 'ProductID': price[1], 'RetailerID': price[2], 'Price': str(price[3]), 'Currency': price[4], 'RetailerName': price[5], 'WebsiteURL': price[6]} for price in prices])

class Prices(Resource):
    def get(self):
        prices = get_all_prices()
        return jsonify([{'PriceID': price[0], 'ProductID': price[1], 'RetailerID': price[2], 'Price': str(price[3]), 'Currency': price[4], 'RetailerName': price[5], 'WebsiteURL': price[6]} for price in prices])