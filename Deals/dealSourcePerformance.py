from NotchReports.Deals import getAllDeals
from datetime import datetime

date1 = "2021-01-01 00:00:00"
date2 = "2021-01-31 23:59:59"
creator = 16364
orgid = 16400

#created_date = 0
#src_name = 1
#curr_stage = 2

query = "SELECT created_date, src_name, curr_stage FROM notch_crm.deals where orgid = {} and creatorid = {} and created_date between '{}' and '{}';".format(orgid, creator, date1,date2)
print(query)

a = getAllDeals.mySqlConnection.read_query(getAllDeals.mySqlConnection.connection, query)

source = {}

for each in a:
    date_created = each[0]
    date_created =  datetime.fromisoformat(date_created)
    month_created = date_created.month
    s_name = each[1]

    if s_name in source:
        source[s_name].append(each)
    else:
        source[s_name] = []
        source[s_name].append(each)
print(len(a))
print(source)



final = []
for each in source.keys():
    won = 0
    lost = 0
    mini = {}
    total = len(source[each])
    for eac in source[each]:
        stt = eac[2]
        if stt == 'Won':
            won += 1
        elif stt == 'Lost':
            lost += 1
        else: pass
    mini[each] = {'Total': total, 'Lost': lost, 'Won': won}
    final.append(mini)
print(final)





