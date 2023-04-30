import pandas as pd


class Hotel:

    def __init__(self, hotel_id, dataframe: pd.DataFrame):
        self.hotel_id = hotel_id
        self.df = dataframe
        self.hotel_name = self.df.loc[self.df['id'] == hotel_id, 'name'].squeeze()

    def book(self):
        """
        Book a hotel by changing it's available to no
        :return: None
        """
        self.df.loc[self.df['id'] == self.hotel_id, 'available'] = 'no'
        self.df.to_csv('hotels.csv', index=False)

    def available(self):
        """
        Check if the hotel is available.
        :return: True if the hotel is available for booking and False if not.
        """
        availability = self.df.loc[self.df['id'] == self.hotel_id, 'available'].squeeze()

        if availability == 'yes':
            return True
        return False
