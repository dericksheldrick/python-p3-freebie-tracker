#!/usr/bin/env python3

# Script goes here!
import sys
import os
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from lib.models import Company, Dev, Freebie, Base

engine = create_engine("sqlite:///freebies.db")
Session = sessionmaker(bind=engine)
session = Session()

# Company
company1 = Company(name="Jagedo", founding_year=2021)
company2 = Company(name="Shelcy", founding_year=2015)

#Dev
dev1 = Dev(name="Devshel")
dev2 = Dev(name="Musa")

#freebies
freebie1 = Freebie(item_name="T-Shirt", value=20, dev=dev1, company=company1)
freebie2 = Freebie(item_name="Water Bottle", value=10, dev=dev2, company=company2)

session.add_all([company1, company2, dev1, dev2, freebie1, freebie2])
session.commit()

