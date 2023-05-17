"""
Test Factory to make fake objects for testing
"""
from datetime import date
from faker import Faker
from mixer.backend.django import mixer
from service.models import Account

class AccountFactory:
    """Creates fake Accounts"""

    def __init__(self):
        self.fake = Faker()

    def create_account(self):
        account = mixer.blend(Account,
                              id=self.fake.unique.random_number(digits=5),
                              name=self.fake.name(),
                              email=self.fake.email(),
                              address=self.fake.address(),
                              phone_number=self.fake.phone_number(),
                              date_joined=self.fake.date_between(start_date=date(2008, 1, 1), end_date='today'))
        return account
