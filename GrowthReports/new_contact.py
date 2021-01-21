from NotchReports import getCollectionsByOrg
from NotchReports.GrowthReports import new_companies

report_config = new_companies.age_in_seconds('new_contact_days', 16400)
get_contacts = getCollectionsByOrg.mongo_connection("notch_sales_clients_test", "contacts", 16400)

print(new_companies.get_count(get_contacts))