from flask import make_response
from flask_restful import Resource
from flask import jsonify
from flask_restful import request

from db.cart import get_cart_contents

try:
    from src.db.categories import get_all_categories, get_category_by_id, search_categories
except ImportError:
    from db.categories import get_all_categories, get_category_by_id, search_categories


class Cart(Resource):

    def get(self, user_id):
        """Fetches all items in a user's shopping cart."""
        if not user_id:
            return jsonify({"error": "User ID is required"}), 400
        cart_items = get_cart_contents(user_id)
        if not cart_items:
            return jsonify(
                {"message": "No items found in the cart"}
            ), 404
        return jsonify(
            {"cart_items": cart_items}
        )
