import pandas as pd
import sqlite3
import database


class Hotel:

    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.hotel_name = None

    def book(self):
        """
        Book a hotel by changing it's available to no
        :return: None
        """
        result = database.get_data_from_db(table_name='hotel')

        for item in result:
            if item[0] == int(self.hotel_id):
                hotel_id = item[0]
                self.hotel_name = item[1]
                availability = 'no'

                with sqlite3.connect('data.db') as connection:
                    cursor = connection.cursor()
                    cursor.execute('''UPDATE hotel SET available = ? WHERE id = ?''', (availability, hotel_id))
                    connection.commit()

    def available(self):
        """
        Check if the hotel is available.
        :return: True if the hotel is available for booking and False if not.
        """
        result = database.get_data_from_db(table_name='hotel')

        availability = None
        for item in result:
            if item[0] == int(self.hotel_id):
                availability = item[4]

        if availability == 'yes':
            return True
        return False
