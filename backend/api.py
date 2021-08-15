from flask import Flask,jsonify,request,render_template
import json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from init_database import Company

app = Flask(__name__)
db = SQLAlchemy(app)

CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///intern.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

@app.route("/intern")
def view_intern():
  companies = Company.quary.all()

  for company in companies:
    print(company.id,company.name,company.logo,company.courses,company.requirements,company.place,company.salary,company.term,company.deadline) 
    
  #{"companies":["楽天株式会社", "LINE株式会社", "株式会社VOYAGE", "メルカリ"],
  #        "siteURLs":["","","https://voyagegroup.snar.jp/",""],
  #        "internURLs":["","","","https://mercan.mercari.com/articles/28040/"]}
