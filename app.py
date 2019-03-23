import os
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data/lr.sqlite"
db = SQLAlchemy(app)
Base = automap_base()
Base.prepare(db.engine, reflect = True)
Fixtures = Base.classes.fixtures

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/charterers")
def names():

    stmt = db.session.query(Fixtures).statement
    df = pd.read_sql_query(stmt, db.session.bind)

    return jsonify(list(df.Charterer.unique()))

@app.route("/Charterers/<chrtr>")
def fixture_data(fixture):
    stmt = db.session.query(Fixtures).statement
    results = session.query(Fixtures).all()
    all_fixtures = []
    for fixtures in results:
        fixture_dict = {}
        fixture_dict["Vessel"] = fixtures.Vessel
        fixture_dict["Size"] = fixtures.Size
        fixture_dict["Grade"] = fixtures.Grade
        fixture_dict["Load"] = fixtures.Load
        fixture_dict["Discharge"] = fixtures.Disch
        fixture_dict["Date"] = fixtures.Date
        fixture_dict["Charterer"] = fixtures.Charterer
        fixture_dict["Owner"] = fixtures.Owner
        all_fixtures.append( fixture_dict)

    print(all_fixtures)
    return jsonify(all_fixtures)

if __name__ == "__main__":
    app.run()


    # sel = [
    #     Fixtures.Charterer,
    #     Fixtures.Comment,
    #     Fixtures.Date,
    #     Fixtures.Disch,
    #     Fixtures.Grade,
    #     Fixtures.Load,
    #     Fixtures.Owner,
    #     Fixtures.Rate,
    #     Fixtures.Size,
    #     Fixtures.Status,
    #     Fixtures.Vessel,
    #     Fixtures.Year
    # ]
    # 