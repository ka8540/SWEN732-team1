from flask import jsonify
from flask import make_response, request
from flask_restful import Resource
from flask_restful import reqparse
from flask import request

try:
    from src.utilities.swen_344_db_utils import exec_get_all, exec_commit
    from src.db.cart import add_item_to_cart, get_cart_contents, remove_item_from_cart , update_item_quantity
except ImportError:
    from utilities.swen_344_db_utils import exec_get_all, exec_commit
    from db.cart import add_item_to_cart, get_cart_contents, remove_item_from_cart, update_item_quantity
    


def verify_session_key(session_key):
    """Check the session key and return the user ID if valid."""
    query = "SELECT user_id FROM user_authentication WHERE session_key = %s;"
    result = exec_get_all(query, (session_key,))
    return result[0][0] if result else None

class CartAPI(Resource):
    def post(self):
        session_key = request.headers.get('X-Session-Key')
        print(session_key)
        if not session_key:
            return {"message": "No session key provided."}, 401

        user_id = verify_session_key(session_key)
        if not user_id:
            return {"message": "Invalid session key."}, 401

        parser = reqparse.RequestParser()
        parser.add_argument('product_id', type=int, required=True, help="Product ID cannot be blank!")
        parser.add_argument('quantity', type=int, required=True, help="Quantity cannot be blank!")
        args = parser.parse_args()

        add_item_to_cart(user_id, args['product_id'], args['quantity'])
        return make_response(jsonify({'message': 'Item added to cart successfully'}), 201)

    def get(self):
        session_key = request.headers.get('X-Session-Key')
        if not session_key:
            return {"message": "No session key provided."}, 401

        user_id = verify_session_key(session_key)
        if not user_id:
            return {"message": "Invalid session key."}, 401

        cart_items = get_cart_contents(user_id)
        return jsonify([{'ProductID': item[0], 'Quantity': item[1]} for item in cart_items])


class CartAPIById(Resource):
    def delete(self, product_id):  # Include `product_id` in the method signature
        session_key = request.headers.get('X-Session-Key')
        if not session_key:
            return {"message": "No session key provided."}, 401

        user_id = verify_session_key(session_key)
        if not user_id:
            return {"message": "Invalid session key."}, 401

        remove_item_from_cart(user_id, product_id)  # Use the `product_id` parameter
        return make_response(jsonify({'message': 'Item removed from cart successfully'}), 204)
    
    def put(self, product_id):
        session_key = request.headers.get('X-Session-Key')
        if not session_key:
            return {"message": "No session key provided."}, 401
        print(session_key,"Session Key received")

        user_id = verify_session_key(session_key)
        if not user_id:
            return {"message": "Invalid session key."}, 401
        print(user_id,"user received")
        parser = reqparse.RequestParser()
        parser.add_argument('quantity', type=int, required=True, help="Quantity cannot be blank!")
        args = parser.parse_args()
        print(args['quantity'])
        # Assuming you have a function to update item quantity in the cart
        update_item_quantity(user_id, product_id, args['quantity'])
        
        return make_response(jsonify({'message': 'Item quantity updated successfully'}), 200)