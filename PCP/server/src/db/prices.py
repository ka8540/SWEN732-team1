try:
    from src.utilities.swen_344_db_utils import exec_get_all
except ImportError:
    from utilities.swen_344_db_utils import exec_get_all
    
def get_prices_by_product(product_id):
    sql = """
    SELECT Prices.*, Retailers.RetailerName, Retailers.WebsiteURL
    FROM Prices
    JOIN Retailers ON Prices.RetailerID = Retailers.RetailerID
    WHERE ProductID = %s;
    """
    return exec_get_all(sql, (product_id,))

def get_all_prices():
    sql = """
    SELECT Prices.*, Retailers.RetailerName, Retailers.WebsiteURL
    FROM Prices
    JOIN Retailers ON Prices.RetailerID = Retailers.RetailerID;
    """
    return exec_get_all(sql)
