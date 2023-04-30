from user import User
from hotel import Hotel
from ticket import ReservationTicket
import pandas as pd

df = pd.read_csv('hotels.csv', dtype={"id": str})

print(df)
user_hotel_id = input('Enter the id of the hotel: ')
hotel = Hotel(hotel_id=user_hotel_id, dataframe=df)

if hotel.available():
    hotel.book()
    name = input('Enter your name: ')
    reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
    ticket_message = reservation_ticket.generate()
    print(ticket_message)
else:
    print(f"Hotel with ID '{user_hotel_id}' is not free")
