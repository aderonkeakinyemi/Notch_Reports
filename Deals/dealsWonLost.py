from NotchReports import mySqlConnection
from pprint import pprint
import math

getDealsquery = "SELECT * FROM notch_crm.deals where orgid = 16400;"

org_deals = mySqlConnection.read_query(mySqlConnection.connection,getDealsquery)
get_all_deals = mySqlConnection.read_query(mySqlConnection.connection, getDealsquery)

#SELECT * FROM notch_crm.deals where orgid = 16400
#SELECT * FROM notch_crm.deals where orgid = 16400 and creatorid = 16364 and created_date like '2020%';
#SELECT * FROM notch_crm.deals where orgid = 16400 and creatorid = 16364 and created_date like '2020%' and curr_stage = 'Lost';
#SELECT * FROM notch_crm.deals where orgid = 16400 and creatorid = 16364 and created_date like '2020%' and curr_stage = 'Won';

#ownername = 23
#ownerId: 9
#actual_date =
#created_date = 8
#currstage = 10
#owners [16364, 16376]
#teams []

owner = "16376"
mydeals = []
for each in org_deals:
    owner_id = each[9]
    if owner_id == owner:
        mydeals.append(each)
    else: pass

dealinfo = {}
this_year = '2021'


for each in mydeals:
    created_date = each[8]
    year = created_date[:4]
    month = created_date[5:7]

    if year == this_year:
        if month in dealinfo:
            dealinfo[month].append(each)

        else:
            dealinfo[month] = []
            dealinfo[month].append(each)
    else: pass

dt = {}
for k in dealinfo.keys():
    final_thing = {}
    final_thing['Month'] = k
    final_thing['total_deals'] = 0
    final_thing['total_won'] = 0
    final_thing['total_lost'] =  0
    for each in dealinfo[k]:
        final_thing['total_deals'] +=1
        if each[10] == 'Won':
            final_thing['total_won'] += 1
        elif each[10] == 'Lost':
            final_thing['total_lost'] += 1
        else: pass

    dt.update({k:final_thing})


for each in dt.keys():
    dt[each]['percentage won'] = 0
    dt[each]['percentage lost'] = 0
    total_deals = dt[each]['total_deals']
    total_won = dt[each]['total_won']
    total_loss = dt[each]['total_lost']
    p_won = total_won/total_deals * 100
    p_won = round(p_won, 2)
    p_loss = (total_loss / total_deals) * 100
    p_loss = round(p_loss,2)
    dt[each]['percentage won'] = p_won
    dt[each]['percentage lost'] = p_loss



# adex {'01': {'Month': '01', 'total_deals': 11, 'total_won': 3, 'total_lost': 2}}
# aderonke {'01': {'Month': '01', 'total_deals': 1, 'total_won': 0, 'total_lost': 0}}

#Connection is successful
#{'01': {'Month': '01', 'total_deals': 11, 'total_won': 3, 'total_lost': 2}}
#{'01': {'Month': '01', 'total_deals': 11, 'total_won': 3, 'total_lost': 2, 'percentage won': 27.27, 'percentage lost': 18.18}}

print(dt)