import pandas as pd
from credit import CreditCard


class SecureCreditCard(CreditCard):

    def __init__(self, card_number, expiration, holder, cvc):
        super().__init__(card_number, expiration, holder, cvc)
        self.secure_credit_df: pd.DataFrame = pd.read_csv('card_security.csv', dtype=str)

    def authenticate(self, given_password):
        password = self.secure_credit_df.loc[self.secure_credit_df['number'] == self.card_number, 'password'].squeeze()

        if password == given_password:
            return True
        return False
