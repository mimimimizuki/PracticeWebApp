from flask import Flask,jsonify,request,render_template
import json
import pymysql
from flask_cors import CORS

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Integer
from sqlalchemy.types import String
from sqlalchemy.types import Text


app = Flask(__name__)
CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///intern.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)

class Intern(db.Model):
  __tablename__ = "companies"

  company_id = db.Column(db.Integer,primary_key=True)
  company_name = db.Column(db.Text,nullable=False)
  company_logo = db.Column(db.Text,nullable=False)
  courses = db.Column(db.Text,nullable=False)
  requirements = db.Column(db.Text,nullable=False)
  place = db.Column(db.Text,nullable=False)
  salary = db.Column(db.Text,nullable=False)
  term = db.Column(db.Text,nullable=False)
  deadline = db.Column(db.Text,nullable=False)

  def __init__(self,company_name,company_logo,courses,requirements,place,salary,term,deadline):
     self.company_name = company_name
     self.company_logo = company_logo
     self.courses = courses
     self.requirements = requirements
     self.place = place
     self.salary = salary
     self.term = term
     self.deadline = deadline




@app.route("/intern", Methods = ["GET"])
def view_intern():
  return 
  
  
  #{"companies":["楽天株式会社", "LINE株式会社", "株式会社VOYAGE", "メルカリ"],
  #        "siteURLs":["","","https://voyagegroup.snar.jp/",""],
  #        "internURLs":["","","","https://mercan.mercari.com/articles/28040/"]}


if __name__ == "__main__":
  db.create_all()
  app.run(host="0.0.0.0",port = 5000, debug =True)