import sqlite3

class DataController:
    def _init_(self, db_path):
        self.db_path = db_path

    def connect(self):
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()

    def disconnect(self):
        self.conn.close()

    def fetch_data(self, query, params=()):
        self.connect()
        self.cursor.execute(query, params)
        data = self.cursor.fetchall()
        self.disconnect()
        return data
    
# Example usage:
# db_controller = DatabaseController('path/to/database.db')
# data = db_controller.fetch_data('SELECT * FROM table_name')
# print(data)
# Ini contoh saja ya, belum tentu bener untuk .db