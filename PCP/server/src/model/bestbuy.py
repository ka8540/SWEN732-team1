import pandas as pd
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from utilities.swen_344_db_utils import *  # Adjust the import path based on your project structure

def insert_data_from_excel_bestbuy():
    # Load the data from Excel
    excel_file = os.path.join(os.path.dirname(__file__), '../../data/BestBuy.xlsx')
    df = pd.read_excel(excel_file)
    
    for index, row in df.iterrows():
        # Extract product details
        product_name = row.get('ProductName')
        product_description = row.get('ProductDescription')
        category_name = row.get('Category')
        image_url = row.get('ImageURL')
        retailer = 'BestBuy'  # Assuming this is constant for all products in the file
        product_price = row.get('Price')
        
        # Insert or retrieve CategoryID
        category_id = exec_get_one("SELECT CategoryID FROM ProductCategories WHERE CategoryName = %s", (category_name,))
        if not category_id:
            exec_commit("INSERT INTO ProductCategories (CategoryName) VALUES (%s)", (category_name,))
            category_id = exec_get_one("SELECT CategoryID FROM ProductCategories WHERE CategoryName = %s", (category_name,))
        category_id = category_id[0]
        
        # Insert or retrieve RetailerID
        retailer_id = exec_get_one("SELECT RetailerID FROM Retailers WHERE RetailerName = %s", (retailer,))
        if not retailer_id:
            retailer_website = 'https://www.bestbuy.com/'  # Assuming a generic website for BestBuy
            exec_commit("INSERT INTO Retailers (RetailerName, WebsiteURL) VALUES (%s, %s)", (retailer, retailer_website))
            retailer_id = exec_get_one("SELECT RetailerID FROM Retailers WHERE RetailerName = %s", (retailer,))
        retailer_id = retailer_id[0]
        
        # Insert product
        exec_commit("""
            INSERT INTO Products (ProductName, ProductDescription, CategoryID, ImageURL) 
            VALUES (%s, %s, %s, %s)
        """, (product_name, product_description, category_id, image_url))
        
        product_id = exec_get_one("SELECT ProductID FROM Products WHERE ProductName = %s", (product_name,))
        product_id = product_id[0]
        
        # Insert price
        exec_commit("""
            INSERT INTO Prices (ProductID, RetailerID, Price, Currency)
            VALUES (%s, %s, %s, 'USD')
        """, (product_id, retailer_id, product_price))


