from flask import make_response
from flask_restful import Resource
from flask import jsonify
from flask_restful import request
from flask_restful import reqparse
import json

try:
    # from src.utilities.swen_344_db_utils import
    from src.db.categories import get_all_categories, get_category_by_id, search_categories
except:
    # from utilities.swen_344_db_utils import
    from db.categories import get_all_categories, get_category_by_id, search_categories
    
class ProductCategories(Resource):
    def get(self):
        result = get_all_categories()
        if result:
            categories = [{'CategoryID': row[0], 'CategoryName': row[1]} for row in result]
            return make_response(jsonify(categories), 200)
        else:
            return make_response(jsonify({'error': 'Categories not found'}), 404)
    

class CategoryById(Resource):
    def get(self, category_id):
        result = get_category_by_id(category_id)
        if result:
            category = {'CategoryID': result[0], 'CategoryName': result[1]}
            return make_response(jsonify(category), 200)
        else:
            return make_response(jsonify({'error': 'Category not found'}), 404)
        
class CategorySearch(Resource):
    def get(self):
        query = request.args.get('query')
        result = search_categories(query)
        categories = [{'CategoryID': row[0], 'CategoryName': row[1]} for row in result]
        return make_response(jsonify(categories), 200)
