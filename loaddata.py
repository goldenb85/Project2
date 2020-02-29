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
# pull in .json data
# ----------------------------------
json_file = "Resources/population.json"
data = json.load(json_file)
from pandas.io.json import json_normalize
df=json_normalize(data['data']) 

df.rename(columns={"ID State": "id_state", "State": "state",
                   "ID Year":"id_year","Year":"year",
                   "Population":"population","Slug State":"slug_state"})

# Create Database Connection
# ----------------------------------
# Creates a connection to our DB using the database Connect Engine

engine = create_engine('postgres+psycopg2://postgres:password@localhost:5432/project2_db')
df.to_sql(name='population_table',con=engine,if_exists='replace',index=False)