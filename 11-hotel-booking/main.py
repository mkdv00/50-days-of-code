from user import User
from hotel import Hotel
from ticket import ReservationTicket
from secure_credit import SecureCreditCard
import database

print('All hotels:')
result = database.get_data_from_db(table_name='hotel')
for row in result:
    print(row)

user_hotel_id = input('Enter the id of the hotel: ')
hotel = Hotel(hotel_id=user_hotel_id)

if hotel.available():
    card_number = input("Enter credit card number: ")
    expiration = input("Enter expiration of the card: ")
    holder = input("Enter card holder: ")
    cvc = input("Enter card cvc: ")

    credit_card = SecureCreditCard(card_number=card_number, expiration=expiration, holder=holder, cvc=cvc)
    if credit_card.validate():
        password = input("Enter credit card password: ")

        if credit_card.authenticate(given_password=password):
            hotel.book()
            name = input('Enter your name: ')
            reservation_ticket = ReservationTicket(customer_name=name, hotel_object=hotel)
            ticket_message = reservation_ticket.generate()
            print(ticket_message)
        else:
            print("Credit card authentication failed!")
    else:
        print(f"Card is not valid. {credit_card.get_card_info()}")
else:
    print(f"Hotel with ID '{user_hotel_id}' is not free")
