from flask import jsonify, make_response, request
from flask_restful import Resource

try:
    from src.db.cart import get_cart_contents, add_item_to_cart, remove_item_from_cart
    from src.utilities.swen_344_db_utils import exec_get_all
except ImportError:
    from db.cart import get_cart_contents, add_item_to_cart, remove_item_from_cart
    from utilities.swen_344_db_utils import exec_get_all


def verify_session_key(session_key):
    """Check the session key and return the user ID if valid."""
    query = "SELECT user_id FROM user_authentication WHERE session_key = %s;"
    result = exec_get_all(query, (session_key,))
    return result[0][0] if result else None


class Cart(Resource):
    def get(self, user_id):
        print(f"Fetching cart for user ID: {user_id}")
        try:
            cart_items = get_cart_contents(user_id)
            print(f"Cart items: {cart_items}")
            if not cart_items:
                return jsonify({"error": "No items found in the cart"}), 404
            return jsonify({"cart_items": cart_items})
        except Exception as e:
            print(f"Error: {e}")
            return jsonify({"error": str(e)}), 500


class AddToCart(Resource):
    def post(self, user_id, product_id, quantity):
        """Adds a new item to the shopping cart or updates the quantity if it already exists."""
        try:
            result = add_item_to_cart(user_id, product_id, quantity)
            if result:
                return jsonify({'message': 'Item added to cart successfully'}), 200
            else:
                return jsonify({'error': 'Failed to add item to cart'}), 500
        except Exception as e:
            return jsonify({"error": str(e)}), 500

class RemoveFromCart(Resource):
    def delete(self, product_id):
        # Retrieve session key from the request headers
        session_key = request.headers.get('X-Session-Key')
        if not session_key:
            return make_response(jsonify({"message": "No session key provided."}), 401)

        # Verify the session key and get the associated user ID
        user_id = verify_session_key(session_key)
        if not user_id:
            return make_response(jsonify({"message": "Invalid session key."}), 401)

        # Proceed with deleting the item from the cart
        try:
            remove_item_from_cart(user_id, product_id)
            return make_response(jsonify({'message': 'Item removed from cart successfully'}), 204)
        except Exception as e:
            return make_response(jsonify({"error": str(e)}), 500)
