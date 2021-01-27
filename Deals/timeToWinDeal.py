from NotchReports import mySqlConnection
from datetime import datetime
from datetime import  date
from math import floor
import calendar
from pprint import pprint

t_query = "SELECT * FROM notch_crm.deals where orgid = 16400 and creatorid = 16364 and curr_stage = 'Won';"
new_query = "SELECT * FROM notch_crm.deals where orgid = 16400 and creatorid = 16364 and curr_stage = 'Won' and actual_closed_date between '2021-01-01' and '2021-19-01';"


all_data = mySqlConnection.read_query(mySqlConnection.connection, new_query)
win_lists = []
if len(all_data) < 1:
    print('no data was returned for the query sent')
else:

    print('There are ', len(all_data), 'records in this list \n')

    for each in all_data:
        time_to_win = {}
        d_code = each[0]
        cr_date = each[8]
        cl_date = each[31]
        deal_name = each[16]

        y = datetime.strptime(cr_date, "%Y-%m-%d %H:%M:%S")
        z = calendar.timegm(y.utctimetuple())

        x = datetime.strptime(cl_date, "%Y-%m-%d %H:%M:%S")
        m = calendar.timegm(x.utctimetuple())
        result = m - z

        age = floor(result/86400)
        time_to_win.update({'deal code': d_code, 'deal_name': deal_name, 'age': age, 'created date': cr_date, 'actual_closed_date': cl_date})
        win_lists.append(time_to_win)

print(win_lists)