# ----------------------------------
# Dependencies
# ----------------------------------

import datetime
import pandas as pd
import numpy as np
import json
# Imports the method used for connecting to DBs
from sqlalchemy import create_engine

# Imports the methods needed to abstract classes into tables
from sqlalchemy.ext.declarative import declarative_base

# Allow us to declare column types
from sqlalchemy import Column, Integer, String, Float, DateTime



# ----------------------------------
# pull in txt data
# ----------------------------------
json_file = "Resources/population.json"
data = json.load(json_file)
from pandas.io.json import json_normalize
df=json_normalize(data['data']) 
df.reindex(index=range(0,312))
# ----------------------------------
# Create Class
# ----------------------------------

# Sets an object to utilize the default declarative base in SQL Alchemy
Base = declarative_base()

# Creates Classes which will serve as the anchor points for our Tables
class popul(Base):
    __tablename__ = 'population_table'
    id = Column(Integer, primary_key=True)
    ID_State = Column(String(255))
    State = Column(String(255))
    ID_Year = Column(DateTime)
    Year = Column(DateTime)
    Population = Column(Integer)
    Slug_State = Column(String(255))

# Create Database Connection
# ----------------------------------
# Creates a connection to our DB using the database Connect Engine

engine = create_engine('postgres+psycopg2://postgres:password@localhost:5432/project2_db')
df.to_sql(name='population_table',con=engine,if_exists='replace',index=False)