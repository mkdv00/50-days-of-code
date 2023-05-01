from credit import CreditCard
import database


class SecureCreditCard(CreditCard):

    def __init__(self, card_number, expiration, holder, cvc):
        super().__init__(card_number, expiration, holder, cvc)

    def authenticate(self, given_password):
        result = database.get_data_from_db(table_name='secure_cards')

        for item in result:
            if self.card_number == item[1]:
                if item[2] == given_password:
                    return True
                return False
