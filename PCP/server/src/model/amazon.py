try:
    import pandas as pd
    import psycopg2
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
    from src.utilities.swen_344_db_utils import *
except:
    from utilities.swen_344_db_utils import *
    import pandas as pd
    import psycopg2
    from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def insert_data_from_excel():
    # Load the data from Excel
    excel_file = os.path.join(os.path.dirname(__file__), '../../data/Amazon.xlsx')
    df = pd.read_excel(excel_file)
    
    for index, row in df.iterrows():    
        # Assuming your Excel has columns: ProductName, ProductDescription, Category, ImageURL
        product_name = row.get('ProductName')
        product_description = row.get('ProductDescription')
        category_name = row.get('Category')
        image_url = row.get('ImageURL')
        retailer = row.get('Retailer')
        product_price = row.get('Price')
        
        # Check if the category already exists, insert if not, and get the CategoryID
        category_id = exec_get_one("SELECT CategoryID FROM ProductCategories WHERE CategoryName = %s", (category_name,))
        if not category_id:
            exec_commit("INSERT INTO ProductCategories (CategoryName) VALUES (%s)", (category_name,))
            category_id = exec_get_one("SELECT CategoryID FROM ProductCategories WHERE CategoryName = %s", (category_name,))
        
         # Assuming CategoryID is the first element of the returned tuple
        category_id = category_id[0]
        
        # Check if the retailer already exists, insert if not, and get the RetailerID
        retailer_id = exec_get_one("SELECT RetailerID FROM Retailers WHERE RetailerName = %s", (retailer,))
        retailer_website = 'https://www.amazon.com/'
        if not retailer_id:
            exec_commit("INSERT INTO Retailers (RetailerName,WebsiteURL) VALUES (%s,%s)", (retailer,retailer_website,))
            retailer_id = exec_get_one("SELECT RetailerID FROM Retailers WHERE RetailerName = %s", (retailer,))
            
        # Assuming RetailerID is the first element of the returned tuple
        retailer_id = retailer_id[0]
        
        
        # Insert product data
        exec_commit("""
            INSERT INTO Products (ProductName, ProductDescription, CategoryID, ImageURL) 
            VALUES (%s, %s, %s, %s)
            """, (product_name, product_description, category_id, image_url))
        
        product_id = exec_get_one("SELECT ProductID FROM Products WHERE ProductName = %s", (product_name,))
        product_id = product_id[0]
        
        # insert price data
        price_currency = 'USD'
        
        exec_commit("""
            INSERT INTO Prices(ProductID,RetailerID,Price,Currency)
            VALUES (%s, %s, %s, %s)
            """,(product_id,retailer_id,product_price,price_currency))
        