from NotchReports import  mySqlConnection
from NotchReports import getCollectionsByOrg
from datetime import datetime

#Connect to mySql to get report configuration
#orgId = 16400
#new_company_days, new_contact_days, new_deal_days, new_deal_won_days, new_invoice_days, new_lead_days, orgid, deal_unchanged_days



#Get growth records
def age_in_seconds(column_name, org_id):
    query = "SELECT {} FROM notch_crm.reports_configuration where orgid ={};".format(column_name,org_id)
    new_company_definition = mySqlConnection.read_query(mySqlConnection.connection, query)
    new_company_definition = new_company_definition[0][0]
    return new_company_definition* 86400

report_config = age_in_seconds("new_company_days", 16400)

#Get companies records from Mongo
company_collection  = getCollectionsByOrg.mongo_connection("notch_sales_clients_test", "companies", 16400)

#Get New company count
def get_count(collection):
    count = 0
    for each in  collection:
        date_created = each['createdAt']
        date_created = date_created /1000
        date_created = datetime.fromtimestamp(date_created) # Convert float to a a datetime object in timestamp

        date_now = datetime.now()
        day = date_now - date_created
        day2 = day.total_seconds()
        if day2 <= report_config:
            count += 1
        else: pass
    return 'The number of items that are new are {}'.format(count)

#print(get_count(company_collection))
#print(data)
#print(ew_comp)

