from flask_restful import Resource
from flask import jsonify

try:
    from src.db.retailers import get_all_retailers, get_retailer_by_id
except:
    from db.retailers import get_all_retailers, get_retailer_by_id
    
    
class Retailers(Resource):
    def get(self):
        retailers = get_all_retailers()
        return jsonify([{'RetailerID': ret[0], 'RetailerName': ret[1], 'WebsiteURL': ret[2]} for ret in retailers])

class RetailerById(Resource):
    def get(self, retailer_id):
        retailer = get_retailer_by_id(retailer_id)
        if retailer:
            return jsonify({'RetailerID': retailer[0], 'RetailerName': retailer[1], 'WebsiteURL': retailer[2]})
        else:
            return {'message': 'Retailer not found'}, 404
