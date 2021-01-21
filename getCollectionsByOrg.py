from pymongo import MongoClient

def mongo_connection(db_name,collection_name,org_id):
    client = MongoClient("mongodb://appuser:NotchCXPass%40word1@178.62.21.116:27017/notch_sales_clients_test?authSource=admin")
    db = client[db_name]
    collection = db[collection_name]
    all_sub = collection.find({'orgId': org_id})
    return all_sub


