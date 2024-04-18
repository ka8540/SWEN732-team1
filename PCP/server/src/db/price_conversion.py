try:
    from src.utilities.swen_344_db_utils import exec_get_all
except ImportError:
    from utilities.swen_344_db_utils import exec_get_all
    
def get_convert_price_to_canadian(price_usd):
    # Current exchange rate from USD to CAD
    exchange_rate = 1.38  # Example rate, replace with actual rate
    # Convert price to CAD
    price_cad = price_usd * exchange_rate
    
    return price_cad

    

def get_convert_price_to_indian(price_usd):
    # Current exchange rate from USD to INR
    exchange_rate = 83.60  # Example rate, replace with actual rate
    # Convert price to CAD
    price_inr = price_usd * exchange_rate
    return price_inr
