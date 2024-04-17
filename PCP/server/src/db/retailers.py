try:
    from src.utilities.swen_344_db_utils import exec_get_all, exec_get_one
except:
    from utilities.swen_344_db_utils import exec_get_all, exec_get_one
    

def get_all_retailers():
    sql = "SELECT * FROM Retailers;"
    return exec_get_all(sql)

def get_retailer_by_id(retailer_id):
    sql = "SELECT * FROM Retailers WHERE RetailerID = %s;"
    return exec_get_one(sql, (retailer_id,))
