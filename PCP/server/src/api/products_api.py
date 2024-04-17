from flask import make_response
from flask_restful import Resource
from flask import jsonify
from flask_restful import request

try:
    from src.db.products import get_all_products,get_product_by_id,search_products
except:
    from db.products import get_all_products,get_product_by_id,search_products
    
class Products(Resource):
    def get(self):
        products = get_all_products()
        return make_response(jsonify([{'ProductID': prod[0], 'ProductName': prod[1], 'ProductDescription': prod[2], 'CategoryID': prod[3], 'ImageURL': prod[4]} for prod in products]), 200)

class ProductById(Resource):
    def get(self, product_id):
        product = get_product_by_id(product_id)
        if product:
            return make_response(jsonify({'ProductID': product[0], 'ProductName': product[1], 'ProductDescription': product[2], 'CategoryID': product[3], 'ImageURL': product[4]}), 200)
        else:
            return make_response(jsonify({'error': 'Product not found'}), 404)

class ProductSearch(Resource):
    def get(self):
        query = request.args.get('query')
        products = search_products(query)
        return make_response(jsonify([{'ProductID': prod[0], 'ProductName': prod[1], 'ProductDescription': prod[2], 'CategoryID': prod[3], 'ImageURL': prod[4]} for prod in products]), 200)
