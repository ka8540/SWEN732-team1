from flask import jsonify
from flask_restful import Resource

try:
    from src.db.cart import get_cart_contents
except ImportError:
    from db.cart import get_cart_contents, add_item_to_cart, remove_item_from_cart


class Cart(Resource):
    def get(self, user_id):
        """Fetches all items in a user's shopping cart by their user ID."""
        try:
            cart_items = get_cart_contents(user_id)
            if not cart_items:
                return jsonify({"error": "No items found in the cart"}), 404
            return jsonify({"cart_items": cart_items})
        except Exception as e:
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
    def delete(self, user_id, product_id):
        """Removes an item from the shopping cart."""
        try:
            remove_item_from_cart(user_id, product_id)
            return jsonify({'message': 'Item removed from cart successfully'}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500
