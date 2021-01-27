from pymongo import MongoClient
from NotchReports import getCollectionsByOrg


orgTxns = getCollectionsByOrg.mongo_connection("notch_sales_clients_test","transactions", 16400)






