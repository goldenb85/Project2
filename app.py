
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
def welcome():
    return (
        f"Welcome to the USA population API!<br/>"
        f"Available Routes:<br/>"
        f"/api/population<br/>"

    )
@app.route("/api/population/")
def some_function():
    df_query = pd.read_sql_query("select * from population_table", con=engine)
    popul_data = df_query.to_json()
    return popul_data



# @app.route("/api/v1.0/precipitation")
# def precipitation():
#     """Return the precipitation data for the last year"""
#     # Calculate the date 1 year ago from last date in database
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

#     # Query for the date and precipitation for the last year
#     precipitation = session.query(Measurement.date, Measurement.prcp).\
#         filter(Measurement.date >= prev_year).all()

#     # Dict with date as the key and prcp as the value
#     precip = {date: prcp for date, prcp in precipitation}
#     return jsonify(precip)


# @app.route("/api/v1.0/stations")
# def stations():
#     """Return a list of stations."""
#     results = session.query(Station.station).all()

#     # Unravel results into a 1D array and convert to a list
#     stations = list(np.ravel(results))
#     return jsonify(stations)


# @app.route("/api/v1.0/tobs")
# def temp_monthly():
#     """Return the temperature observations (tobs) for previous year."""
#     # Calculate the date 1 year ago from last date in database
#     prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

#     # Query the primary station for all tobs from the last year
#     results = session.query(Measurement.tobs).\
#         filter(Measurement.station == 'USC00519281').\
#         filter(Measurement.date >= prev_year).all()

#     # Unravel results into a 1D array and convert to a list
#     temps = list(np.ravel(results))

#     # Return the results
#     return jsonify(temps)


# @app.route("/api/v1.0/temp/<start>")
# @app.route("/api/v1.0/temp/<start>/<end>")
# def stats(start=None, end=None):
#     """Return TMIN, TAVG, TMAX."""

#     # Select statement
#     sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

#     if not end:
#         # calculate TMIN, TAVG, TMAX for dates greater than start
#         results = session.query(*sel).\
#             filter(Measurement.date >= start).all()
#         # Unravel results into a 1D array and convert to a list
#         temps = list(np.ravel(results))
#         return jsonify(temps)

#     # calculate TMIN, TAVG, TMAX with start and stop
#     results = session.query(*sel).\
#         filter(Measurement.date >= start).\
#         filter(Measurement.date <= end).all()
#     # Unravel results into a 1D array and convert to a list
#     temps = list(np.ravel(results))
#     return jsonify(temps)


if __name__ == '__main__':
    app.run()
