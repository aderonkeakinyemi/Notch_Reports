from pymongo import MongoClient
from NotchReports import getCollectionsByOrg


orgTxns = getCollectionsByOrg.mongo_connection("mongodb://appuser:NotchCXPass%40word1@178.62.21.116:27017/notch_sales_clients_test?authSource=admin",
                                     "notch_sales_clients_test","transactions", 16400)






