from NotchReports import mySqlConnection
from datetime import datetime, date, time


a_query = "SELECT * FROM notch_crm.activity_log where orgid = 16400 and creatorid = 16364;"

#for a in
d_year =  2020
t_query =  "SELECT * FROM notch_crm.activity_log where teamid = 16405 and creatorid = 16364"
a = mySqlConnection.read_query(mySqlConnection.connection, a_query)

result = {}
for each in a:
    datee = each[5]
    datee =  datetime.strptime(datee, "%d/%m/%Y %H:%M:%S")
    Yr = datee.year
    if Yr == 2020:
        typpe = each[15]
        if typpe in result:
            result[typpe] += 1
        else: result[typpe] = 1
    else: pass


print(result)






