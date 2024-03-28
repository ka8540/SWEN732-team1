from flask import make_response
from flask_restful import Resource
from flask import jsonify
from flask_restful import request
from flask_restful import reqparse
import json

try:
    from src.utilities.swen_344_db_utils import *
    from src.db.user_favorites import *
except:
    from utilities.swen_344_db_utils import *
    from db.user_favorites import *
    

class UserFavorites(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('user_id', type=int, required=True, help="User ID cannot be blank!")
        parser.add_argument('product_id', type=int, required=True, help="Product ID cannot be blank!")
        args = parser.parse_args()
        add_user_favorite(args['user_id'], args['product_id'])
        return make_response(jsonify({'message': 'Favorite product added successfully'}), 201)
    
class UserFavoritesById(Resource):
    def get(self, user_id):
        favorites = get_user_favorites(user_id)
        return jsonify([{'FavoriteID': fav[4], 'ProductID': fav[0], 'ProductName': fav[1], 'ProductDescription': fav[2], 'ImageURL': fav[3]} for fav in favorites])