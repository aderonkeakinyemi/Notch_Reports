from NotchReports.Deals import getAllDeals
from NotchReports import mySqlConnection

#SELECT * FROM notch_crm.deals where orgid = 16400 and creatorid = 16364 and actual_closed_date between '2020-01-01 00:00:00' and '2020-12-31 23:59:59' and curr_stage = 'Lost';

def all_deals_lost_yearly(orgid, creatorid,year):
    all_deals_lost_yearly = "SELECT creatorid, actual_closed_date, created_date, comment FROM notch_crm.deals where orgid = {} and creatorid = {} " \
     "and curr_stage = 'Lost' and actual_closed_date like '{}%';".format(orgid, creatorid,year)
    all_deals = mySqlConnection.read_query(mySqlConnection.connection, all_deals_lost_yearly)
    return len(all_deals)


def all_deals_lost_yearly_grouped(orgid, creatorid,year):
    all_deals_lost_yearly = "SELECT count(comment), comment FROM notch_crm.deals where orgid = {} and creatorid = {} " \
     "and curr_stage = 'Lost' and actual_closed_date like '{}%' group by comment;".format(orgid, creatorid,year)
    all_deals = mySqlConnection.read_query(mySqlConnection.connection, all_deals_lost_yearly)
    return all_deals

print(all_deals_lost_yearly_grouped(16400, 16364, 2021))