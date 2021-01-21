from NotchReports import dealsWonLost
from NotchReports.GrowthReports import new_companies
from datetime import datetime

report_config = new_companies.age_in_seconds('new_deal_days', 16400)
get_deals = dealsWonLost.new_deals_query

def get_count(collection):
    count = 0
    for each in  collection:
        date_created = each[8]
        date_created = datetime.fromisoformat(date_created)

        date_now = datetime.now()
        day = date_now - date_created
        day2 = day.total_seconds()
        if day2 <= report_config:
            count += 1
        else: pass
    return 'The number of items that are new are {}'.format(count)

print(get_count(get_deals))