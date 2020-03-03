
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify,request, render_template
from flask_cors import CORS


#################################################
# Database Setup
#################################################
engine = create_engine('postgres+psycopg2://postgres:password@localhost:5432/project2_db')

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
CORS(app)
#################################################
# Flask Routes
#################################################
@app.route("/")
def home():
    
    return render_template("index.html")

@app.route("/api/population/")
def population():
    # Create our session (link) from Python to the DB
    
    
    results =[]
    results = engine.execute("select  id_year,state,population from population_table")
    all_state=[]
    for id_year,state,population in results:
        population_dict = {}
        
        population_dict["id_year"]=id_year
        population_dict["state"]=state
        population_dict["population"]=population
        all_state.append(population_dict)
     
    return jsonify(all_state)
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
