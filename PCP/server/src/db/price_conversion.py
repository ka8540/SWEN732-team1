def get_convert_price_to_canadian(price_usd):
    exchange_rate = 1.38
    price_cad = price_usd * exchange_rate
    print(price_cad)
    return round(price_cad, 2)  # Assuming you want to round to 2 decimal places

def get_convert_price_to_indian(price_usd):
    exchange_rate = 83.60
    price_inr = price_usd * exchange_rate
    print(price_inr,"INR PRICE")
    return round(price_inr, 2)