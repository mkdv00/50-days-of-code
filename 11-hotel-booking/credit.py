import database


class CreditCard:

    def __init__(self, card_number, expiration, holder, cvc):
        self.card_number = card_number
        self.expiration = expiration
        self.holder = holder
        self.cvc = cvc

    def get_card_info(self):
        card_info = f"Card number: {self.card_number}. Expiration: {self.expiration}. Holder: {self.holder}. " \
                    f"CVC: {self.cvc}."
        return card_info

    def validate(self):
        result = database.get_data_from_db(table_name='cards')

        card_data = {'card_number': self.card_number, 'expiration': self.expiration,
                     'cvc': self.cvc, 'holder': self.holder}

        for item in result:
            if self.card_number == item[1]:
                current_card_data = {'card_number': item[1], 'expiration': item[2], 'cvc': item[3], 'holder': item[4]}

                print(f"Card data: {card_data}")
                print(f"Card data from DB: {current_card_data}")

                if card_data == current_card_data:
                    return True
                return False
