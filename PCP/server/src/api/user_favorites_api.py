from flask import jsonify
from flask import make_response
from flask_restful import Resource
from flask_restful import reqparse, request

try:
    from src.utilities.swen_344_db_utils import exec_get_all
    from src.db.user_favorites import add_user_favorite, get_user_favorites,delete_user_favorite
except ImportError:
    from utilities.swen_344_db_utils import exec_get_all
    from db.user_favorites import add_user_favorite, get_user_favorites,delete_user_favorite
    


def verify_session_key(session_key):
    """Check the session key and return the user ID if valid."""
    query = "SELECT user_id FROM user_authentication WHERE session_key = %s;"
    result = exec_get_all(query, (session_key,))
    print(result)
    return result[0][0] if result else None

class UserFavorites(Resource):
    def post(self):
        session_key = request.headers.get('X-Session-Key')
        print(session_key)
        if not session_key:
            return {"message": "No session key given."}, 401

        user_id = verify_session_key(session_key)
        if not user_id:
            return {"message": "Invalid session key Provided."}, 401

        parser = reqparse.RequestParser()
        parser.add_argument('product_id', type=int, required=True, help="Product ID cannot be blank!")
        args = parser.parse_args()
        
        add_user_favorite(user_id, args['product_id'])
        return make_response(jsonify({'message': 'Favorite product added successfully'}), 201)
    
    def get(self):
        session_key = request.headers.get('X-Session-Key')
        if not session_key:
            return {"message": "No session key provided."}, 401

        user_id = verify_session_key(session_key)
        if not user_id:
            return {"message": "Invalid session key."}, 401

        favorites = get_user_favorites(user_id)

        return jsonify([{'FavoriteID': fav[4], 'ProductID': fav[0], 'ProductName': fav[1], 'ProductDescription': fav[2], 'ImageURL': fav[3]} for fav in favorites])
    
    

class UserFavoritesById(Resource):
    def delete(self, product_id):
        session_key = request.headers.get('X-Session-Key')
        if not session_key:
            return {"message": "No session key present."}, 401

        user_id = verify_session_key(session_key)
        if not user_id:
            return {"message": "Invalid session key given."}, 401
        print("idhar aa gaya")
        delete_user_favorite(user_id, product_id)
        return make_response(jsonify({'message': 'Favorite product deleted successfully'}), 204)
