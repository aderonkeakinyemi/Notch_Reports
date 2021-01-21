import mysql.connector
from _datetime import date, time, datetime
import _strptime

# Creating a connection to the DB
def mysql_conn(host_name, user_name, password_password, port_number, database_name):
    connection = None

    try:
        connection = mysql.connector.connect(host=host_name, user=user_name, password=password_password, port=port_number,database=database_name)
        print('Connection is successful')

    except ConnectionError as err:
        print(f"Error: '{err}'")

    return connection


def read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except ConnectionError as err:
        print(f"Error: '{err}'")


connection = mysql_conn(host_name='notch-db-do-user-6629666-0.db.ondigitalocean.com', user_name='appuser',
                        password_password='Pass@word1', port_number=25060,database_name='notch_crm')