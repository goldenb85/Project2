
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify,request, render_template


#################################################
# Database Setup
#################################################
engine = create_engine('postgres+psycopg2://postgres:password@localhost:5432/project2_db')

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

# # reflect an existing database into a new model
# Base = automap_base()
# # reflect the tables
# Base.prepare(engine, reflect=True)

# # Save references to each table
# popul = Base.classes.popul


#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"Welcome to the USA population API!<br/>"
        f"Available Routes:<br/>"
        f"/api/population/<br/>"        
        f"/api/population/2013<br/>"
        f"/api/population/2014<br/>"
        f"/api/population/2015<br/>"
        f"/api/population/2016<br/>"
        f"/api/population/2017<br/>"
        f"/api/population/2018<br/>"
    )
@app.route("/api/population/")
def population():
    df_query = pd.read_sql_query("select * from population_table", con=engine)
    popul_data = df_query.to_json()
    return popul_data
        # Create our session (link) from Python to the DB
    # session = Session(engine)

    # """Return a list of all Precipitation Data"""
    # # Query all Precipitation
    # results = session.query(popul.id_state, popul.state,popul.id_year,popul.year,popul.population,popul.slug_state).all()

    # session.close()
 
    # # Convert the list to Dictionary
    # all_popul = []
    # for id_state,state,id_year,year,population,slug_state  in results:
    #     popul_dict = {}
    #     popul_dict["id_state"] = id_state
    #     popul_dict["state"] = state
    #     popul_dict["id_year"] = id_year
    #     popul_dict["year"] = year
    #     popul_dict["population"] = population
    #     popul_dict["slug_state"] = slug_state       
    #     all_popul.append(popul_dict)

    # return jsonify(all_popul)
@app.route("/api/population/2013")
def population2013():
    df_query = pd.read_sql_query("select * from population_table where id_year=2013", con=engine)
    popul_data = df_query.to_json()
    return popul_data
@app.route("/api/population/2014")
def population2014():
    df_query = pd.read_sql_query("select * from population_table where id_year=2014", con=engine)
    popul_data = df_query.to_json()
    return popul_data
@app.route("/api/population/2015")
def population2015():
    df_query = pd.read_sql_query("select * from population_table where id_year=2015", con=engine)
    popul_data = df_query.to_json()
    return popul_data
@app.route("/api/population/2016")
def population2016():
    df_query = pd.read_sql_query("select * from population_table where id_year=2016", con=engine)
    popul_data = df_query.to_json()
    return popul_data
@app.route("/api/population/2017")
def population2017():
    df_query = pd.read_sql_query("select * from population_table where id_year=2017", con=engine)
    popul_data = df_query.to_json()
    return popul_data
@app.route("/api/population/2018")
def population2018():
    df_query = pd.read_sql_query("select * from population_table where id_year=2018", con=engine)
    popul_data = df_query.to_json()
    return popul_data
if __name__ == '__main__':
    app.run()
