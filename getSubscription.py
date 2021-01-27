from pymongo import MongoClient
from datetime import date
from NotchReports import getTransactions
from NotchReports import getCollectionsByOrg

import pprint
import datetime
#CreatedAT = date sub was created, unused
#createdOn = sub start date - used
#owner = 16364
#teamId = 16405
#orgId = 16400
#periodCount:
#'isExpired': False,
#'isSuspended': False,
#'isTerminated': False,
#endDate
#createdOn
#print subs created by aderonke in 2021
#ownerName: "Adex Adex"
#clientID: 14 - living yield
#{'orgId':16400, 'owner':16364, 'createdOn': {$gte: 1577833200000, $lte: 1609369200000}}

# fetch all subscription reports for an org
sub_list = getCollectionsByOrg.mongo_connection("notch_sales_clients_test", "subscriptions", 16400)
org_txns = getTransactions.orgTxns
sub_txn_count = 0

sub_txn_list = []
for each in org_txns:
    if each['itemType'] == 'subscription':
        sub_txn_list.append(each)
        sub_txn_count += 1
        #print(each['equivalents']['USD'])



#transaction: each['itemId'] or id
#each['equivalents']['USD']
#sub : each['id]
#SUB-16400-0000044


sub_output = {}
this_year, this_owner, this_client  = 2020, 16364, 41

cur_year_sub = []

def count_subscription(year, owner_id, client_id):

    monthlySub = {}
    for each in sub_list:
        owner = each['owner']
        clientId = each['clientId']
        createddate = each['createdOn'] /1000
        date_convert = date.fromtimestamp(createddate)

        intYr = date_convert.year
        each['intYr'] = intYr
        intMnth = date_convert.month
        each['intMnth'] = intMnth
        if intYr == year and owner == owner_id and clientId == client_id:
            cur_year_sub.append(each)

            if intMnth in monthlySub:
                monthlySub[intMnth] += 1
            else:
                monthlySub[intMnth] = 1
        else: pass

    sub_output.update(
        {'sub_owner': owner_id, 'client': client_id, 'sub_year': year, 'monthly_sub_count': monthlySub})
    return sub_output

def subsription_amount(year, owner, client):
    sub_amount = {}

    sub_amt_date = {}
    print('hi')
    for x in cur_year_sub:
        sub_id_s = x['id']
        for y in sub_txn_list:
            sub_id_t = y['itemId']
            if sub_id_s == sub_id_t[-1]:
                print('hi')
                print(sub_id_s, sub_id_t)
            else: pass



a = count_subscription(this_year,this_owner,this_client)
print(sub_txn_count)
print(a)

