from datetime import timedelta, datetime
from time import time
from sqlalchemy.exc import IntegrityError

from server.common.managers import SuperManager
from .models import *

class CustomerManager(SuperManager):
    def __init__(self, db):
        super().__init__(Customer, db)

    # def get_groupsByFamily(self, family):
    #     return self.db.query(Product).filter(Product.fk_family == family)

    def insert(self, customer):
        return super().insert(customer)
