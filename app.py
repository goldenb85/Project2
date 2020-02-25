
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




#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    popul_data = []
    return render_template("index.html", popul_data=popul_data)

@app.route("/api/population/")
def population():
    df_query = pd.read_sql_query("select id_state,state,id_year as year,population from population_table", con=engine)
    popul_data = df_query.to_json()
    return popul_data
   
# @app.route("/api/population/2013")
# def population2013():
#     df_query = pd.read_sql_query("select * from population_table where id_year=2013", con=engine)
#     popul_data = df_query.to_json()
#     return popul_data
# @app.route("/api/population/2014")
# def population2014():
#     df_query = pd.read_sql_query("select * from population_table where id_year=2014", con=engine)
#     popul_data = df_query.to_json()
#     return popul_data
# @app.route("/api/population/2015")
# def population2015():
#     df_query = pd.read_sql_query("select * from population_table where id_year=2015", con=engine)
#     popul_data = df_query.to_json()
#     return popul_data
# @app.route("/api/population/2016")
# def population2016():
#     df_query = pd.read_sql_query("select * from population_table where id_year=2016", con=engine)
#     popul_data = df_query.to_json()
#     return popul_data
# @app.route("/api/population/2017")
# def population2017():
#     df_query = pd.read_sql_query("select * from population_table where id_year=2017", con=engine)
#     popul_data = df_query.to_json()
#     return popul_data
# @app.route("/api/population/2018")
# def population2018():
#     df_query = pd.read_sql_query("select * from population_table where id_year=2018", con=engine)
#     popul_data = df_query.to_json()
#     return popul_data
if __name__ == '__main__':
    app.run()
