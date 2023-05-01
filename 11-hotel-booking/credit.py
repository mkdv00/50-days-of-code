import pandas as pd


class CreditCard:

    def __init__(self, card_number, expiration, holder, cvc):
        self.card_number = card_number
        self.expiration = expiration
        self.holder = holder
        self.cvc = cvc
        self.credit_df = pd.read_csv('cards.csv', dtype=str).to_dict(orient='records')

    def get_card_info(self):
        card_info = f"Card number: {self.card_number}. Expiration: {self.expiration}. Holder: {self.holder}. " \
                    f"CVC: {self.cvc}."
        return card_info

    def validate(self):
        card_data = {'number': self.card_number, 'expiration': self.expiration,
                     'cvc': self.cvc, 'holder': self.holder}

        for item in self.credit_df:
            del item['balance']

        if card_data in self.credit_df:
            return True
        return False
