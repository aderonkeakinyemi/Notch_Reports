from NotchReports import mySqlConnection

def get_org_deals(orgId):

    all_deals_query = "SELECT * FROM notch_crm.deals where orgid = {};".format(orgId)
    all_deals = mySqlConnection.read_query(mySqlConnection.connection, all_deals_query)
    return all_deals

def get_user_deals(org_id, user_id):
    all_deals_query = "SELECT * FROM notch_crm.deals where orgid = {} and creatorid = {}".format(org_id,user_id)
    all_deals = mySqlConnection.read_query(mySqlConnection.connection, all_deals_query)
    return  all_deals


