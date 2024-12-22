import mysql.connector

config = {
    'user': 'root',
    'password': 'Hrhk@9090',
    'host': 'localhost',
    'database': 'grocery_store'
}

class DatabaseManager:
    def __init__(self, config):
        # Correctly unpack the config dictionary
        self.db_connection = mysql.connector.connect(**config)
        self.db_cursor = self.db_connection.cursor()

    def find_bill(self, bill_number, customer_name):
        select_query = "SELECT * FROM bills WHERE bill_number = %s AND customer_name = %s"
        self.db_cursor.execute(select_query, (bill_number, customer_name))
        return self.db_cursor.fetchone()

    def close(self):
        self.db_cursor.close()
        self.db_connection.close()