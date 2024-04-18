from decimal import Decimal
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

class PriceConverter:
    
    def add_converted_prices():
        # Assuming a fixed conversion rate from USD to INR
        usd_to_inr_rate = Decimal('85.0')  # Convert rate to Decimal
        
        # SQL to fetch all prices in USD from the Prices table
        select_sql = "SELECT PriceID, Price FROM Prices WHERE Currency = 'USD'"
        
        # Fetch USD prices
        prices = exec_get_all(select_sql)
        
        # SQL to insert converted prices into the ConvertedPrices table
        insert_sql = """
        INSERT INTO ConvertedPrices (PriceID, ConvertedPrice, ConvertedCurrency) 
        VALUES (%s, %s, 'INR')
        """
        
        # Convert and insert INR prices
        for price_id, usd_price in prices:
            inr_price = usd_price * usd_to_inr_rate
            exec_commit(insert_sql, (price_id, inr_price))
    
   
    def add_converted_prices_to_cad():
        # Assuming a fixed conversion rate from USD to CAD
        usd_to_cad_rate = Decimal('1.25')  # Convert rate to Decimal
        
        # SQL to fetch all prices in USD from the Prices table
        select_sql = "SELECT PriceID, Price FROM Prices WHERE Currency = 'USD'"
        
        # Fetch USD prices
        prices = exec_get_all(select_sql)
        
        # SQL to insert converted prices into the ConvertedPrices table
        insert_sql = """
        INSERT INTO ConvertedPrices (PriceID, ConvertedPrice, ConvertedCurrency) 
        VALUES (%s, %s, 'CAD')
        """
        
        # Convert and insert CAD prices
        for price_id, usd_price in prices:
            cad_price = usd_price * usd_to_cad_rate
            exec_commit(insert_sql, (price_id, cad_price))