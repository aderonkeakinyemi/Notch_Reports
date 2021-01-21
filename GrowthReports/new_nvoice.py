from NotchReports import getCollectionsByOrg
from NotchReports.GrowthReports import new_companies
from _datetime import datetime

report_config = new_companies.age_in_seconds('new_invoice_days', 16400)
get_invoices = getCollectionsByOrg.mongo_connection("notch_sales_clients_test", "invoices", 16400)

#CAVEAT: invoices report uses createdON instead of created at which everybody else uses


def get_count(collection):
    count = 0
    for each in  collection:
        date_created = each['createdOn']
        date_created = date_created /1000
        date_created = datetime.fromtimestamp(date_created) # Convert float to a a datetime object in timestamp

        date_now = datetime.now()
        day = date_now - date_created
        day2 = day.total_seconds()
        if day2 <= report_config:
            count += 1
        else: pass
    return 'The number of items that are new are {}'.format(count)

print(get_count(get_invoices))