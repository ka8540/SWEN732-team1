from flask import Flask
from flask_restful import Resource, Api
from flask_cors import CORS

from utilities.swen_344_db_utils import *
from api.login_api import *
from api.signup_api import *
from api.user_detail_api import *
from api.logout_api import *
from model.amazon import *
from api.categories_api import *
from api.products_api import *
from api.retailer_api import *
from api.prices_api import *
from api.user_favorites_api import *

app = Flask(__name__)  # create Flask instance
CORS(app)  # Enable CORS on Flask server to work with Nodejs pages
api = Api(app)  # api router

api.add_resource(SignUpApi, '/signUp')
api.add_resource(LoginAPI, '/login')
api.add_resource(UserDetail, '/userdetail')
api.add_resource(LogoutAPI, '/logout')
api.add_resource(ProductCategories, '/categories')
api.add_resource(CategoryById, '/categories/<int:category_id>')
api.add_resource(CategorySearch, '/categories/search')
api.add_resource(Products, '/products')
api.add_resource(ProductById, '/products/<int:product_id>')
api.add_resource(ProductSearch, '/products/search')
api.add_resource(Retailers, '/retailers')
api.add_resource(RetailerById, '/retailers/<int:retailer_id>')
api.add_resource(PricesByProduct, '/prices/products/<int:product_id>')
api.add_resource(Prices, '/prices')
api.add_resource(UserFavorites, '/user_favorites')
api.add_resource(UserFavoritesById, '/user_favorites/<int:user_id>')


def setup_database():
    print("Loading db")
    # exec_sql_file('data/UserDetail.sql')
    exec_sql_file('data/data.sql')
    insert_data_from_excel()


if __name__ == '__main__':
    print("Starting flask")
    setup_database()  # Set up the database and insert data from Excel
    app.run(debug=True)  # starts Flask
