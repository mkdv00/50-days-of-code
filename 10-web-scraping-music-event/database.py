import sqlite3


class Data:

    def __init__(self):
        self.get_data_db = "SELECT * FROM events"
        self.store_data_db = "INSERT INTO events VALUES(?,?,?)"
        self.connection = sqlite3.connect('data.db')

    def get_data(self):
        cursor = self.connection.cursor()
        cursor.execute(self.get_data_db)
        result = cursor.fetchall()
        return result

    def store_data(self, extracted_data):
        row_data = extracted_data.split(', ')
        row_data = [item.strip() for item in row_data]
        cursor = self.connection.cursor()
        cursor.execute(self.store_data_db, row_data)
        self.connection.commit()
