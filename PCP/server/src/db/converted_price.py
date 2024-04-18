try:
    from src.api.converted_prices_api import *
    from src.utilities.swen_344_db_utils import *
except:
    from api.converted_prices_api import *
    from utilities.swen_344_db_utils import *
    

def get_indian_converted_prices():
    sql = """
    SELECT * FROM ConvertedPrices WHERE ConvertedCurrency = 'INR';
    """
    return exec_get_all(sql)

def get_canadian_prices():
    sql = """
    SELECT * FROM ConvertedPrices WHERE ConvertedCurrency = 'CAD';
    """
    return exec_get_all(sql)

def get_all_prices():
    sql = """
    SELECT * FROM ConvertedPrices;
    """
    return exec_get_all(sql)