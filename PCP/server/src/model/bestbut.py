import os
import pandas as pd
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

try:
    from src.utilities.swen_344_db_utils import exec_commit, exec_get_one
except ImportError:
    from utilities.swen_344_db_utils import exec_commit, exec_get_one


def insert_data_from_excel_bestbuy():
    # Load the data from Excel
    excel_file_bestbuy = os.path.join(os.path.dirname(__file__), '../../data/BestBuy.xlsx')
    df_bestbuy = pd.read_excel(excel_file_bestbuy)
    
    for index, row in df_bestbuy.iterrows():
        # Assuming your Excel has columns: ProductName, ProductDescription, Category, ImageURL
        product_name_bestbuy = row.get('ProductName')
        product_description_bestbuy = row.get('ProductDescription')
        category_name_bestbuy = row.get('Category')
        image_url_bestbuy = row.get('ImageURL')
        retailer_bestbuy = row.get('Retailer')
        product_price_bestbuy = row.get('Price')
        
        # Check if the category already exists, insert if not, and get the CategoryID
        category_id_bestbuy = exec_get_one("SELECT CategoryID FROM ProductCategories WHERE CategoryName = %s", (category_name_bestbuy,))
        if not category_id_bestbuy:
            exec_commit("INSERT INTO ProductCategories (CategoryName) VALUES (%s)", (category_name_bestbuy,))
            category_id_bestbuy = exec_get_one("SELECT CategoryID FROM ProductCategories WHERE CategoryName = %s", (category_name_bestbuy,))
        
         # Assuming CategoryID is the first element of the returned tuple
        category_id_bestbuy = category_id_bestbuy[0]
        
        # Check if the product already exists, insert if not and get product id
        product_id_bestbuy = exec_get_one("SELECT ProductID FROM Products WHERE ProductName = %s", (product_name_bestbuy,))
        if not product_id_bestbuy:
            exec_commit("""INSERT INTO Products (ProductName, ProductDescription, CategoryID, ImageURL) VALUES (%s, %s, %s, %s)""", (product_name_bestbuy, product_description_bestbuy, category_id, image_url_bestbuy))
            product_id_bestbuy = exec_get_one("SELECT ProductID FROM Products WHERE ProductName = %s", (product_name_bestbuy,))
        
        # Assuming CategoryID is the first element of the returned tuple
        product_id_bestbuy = product_id_bestbuy[0]
        
        # Check if the retailer already exists, insert if not, and get the RetailerID
        retailer_id_bestbuy = exec_get_one("SELECT RetailerID FROM Retailers WHERE RetailerName = %s", (retailer_bestbuy,))
        retailer_website = 'https://www.bestbuy.com/'
        if not retailer_id_bestbuy:
            exec_commit("INSERT INTO Retailers (RetailerName,WebsiteURL) VALUES (%s,%s)", (retailer_bestbuy,retailer_website,))
            retailer_id_bestbuy = exec_get_one("SELECT RetailerID FROM Retailers WHERE RetailerName = %s", (retailer_bestbuy,))
            
        # Assuming RetailerID is the first element of the returned tuple
        retailer_id_bestbuy = retailer_id_bestbuy[0]
        
        # insert price data
        price_currency_bestbuy = 'USD'
        exec_commit("""
            INSERT INTO Prices(ProductID,RetailerID,Price,Currency)
            VALUES (%s, %s, %s, %s)
            """,(product_id_bestbuy,retailer_id_bestbuy,product_price_bestbuy,price_currency_bestbuy))
