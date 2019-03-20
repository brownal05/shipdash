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

@app.route("/fixtures/<fixture>")
def fixture_data(fixture):
    sel = [
        Fixtures.Charterer,
        Fixtures.Comment,
        Fixtures.Date,
        Fixtures.Disch,
        Fixtures.Grade,
        Fixtures.Load,
        Fixtures.Owner,
        Fixtures.Rate,
        Fixtures.Size,
        Fixtures.Status,
        Fixtures.Vessel,
        Fixtures.Year
    ]
    results = db.session.query(*sel).filter(Fixtures.Charterer == fixture).all()
    fixtures = {}
    for result in results:
        fixtures["Vessle"] = result[10]
        fixtures["Size"] = result[8]
        fixtures["Grade"] = results[4]
        fixtures["Load"] = results[5]
        fixtures["Discharge"] = results[3]
        fixtures["Rate"] = results[7]
        fixtures["Laycan"] = results[2]
        fixtures["Owner"] = results[6]
        fixtures["Comments"] = results[1]
        fixtures["Charterer"] = results[0]

    print(fixtures)
    return jsonify(fixtures)

if __name__ == "__main__":
    app.run()