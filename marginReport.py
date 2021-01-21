from NotchReports import mySqlConnection
from datetime import datetime

query = "SELECT * FROM notch_crm.sales_order where orgid = 16400 and creatorid = 16364;"

all_data = mySqlConnection.read_query(mySqlConnection.connection, query)
print(len(all_data))

allinfo = []
monthly ={}
for each in all_data:
    date = each[3]
    d = datetime.strptime(date, "%Y-%m-%d %H:%M:%S")
    yr = d.year
    mn = d.month
    margin = each[-7]
    currency = each[5]


    if yr == 2020:
        if mn in monthly.keys():
            monthly[mn] += margin
        else:
            monthly.update({mn:margin})
    else:
        pass



print(monthly)
