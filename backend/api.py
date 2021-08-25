from flask import Flask,jsonify,request,render_template
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,Text
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from sqlalchemy.sql.schema import PrimaryKeyConstraint


#default config
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///intern.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JSON_AS_ASCII'] = False
CORS(app)


#make database
db = SQLAlchemy(app)
class Company(db.Model):
  __tablename__ = "companies"
  
  id            = db.Column(db.Integer,primary_key=True,autoincrement=True)
  name          = db.Column(db.Text)
  logo          = db.Column(db.Text)
  course        = db.Column(db.Text)
  requirement   = db.Column(db.Text) 
  place         = db.Column(db.Text)
  salary        = db.Column(db.Text)
  term          = db.Column(db.Text)
  deadline      = db.Column(db.Text)

  def __init__(self,name,logo,course,requirement,place,salary,term,deadline):
    self.name         = name
    self.logo         = logo
    self.course       = course
    self.requirement  = requirement
    self.place        = place
    self.salary       = salary
    self.term         = term
    self.deadline     = deadline


def insert_into_database():
  yahoo   = Company("Yahoo株式会社"       ,"../logos/yohoo_logo.jpg"  ,"バックエンド"              ,"JavaもしくはPythonの経験","オンライン" ,"1300円/h"  ,"8/30〜9/5","6/18 12:00")
  line    = Company("株式会社LINE"        ,"../logos/line_logo.jpg"   ,"バックエンド"              ,"JavaScriptの経験"       ,"オンライン" ,"1500円/h"  ,"9/8～9/17","6/18 12:00")
  voyage  = Company("株式会社voyage group","../logos/voyage_logo.jpg" ,"バックエンド"              ,"goでの開発経験"          ,"オンライン" ,"1300円/day","8/6～8/27","5/31")
  rakuten = Company("楽天グループ株式会社"  ,"../logos/rakuten_logo.jpg","バックエンド/データサイエンス","JavaScriptの経験"       ,"東京本社"  ,"1100円/h"  ,"9/21～9/29","6/22")

  db.session.add(yahoo)
  db.session.add(line)
  db.session.add(voyage)
  db.session.add(rakuten)
  db.session.commit()

def make_database():
  db.drop_all()
  db.create_all()
  insert_into_database()
  
#結局marshmallow使わんかった
#set marshmallow
#ma = Marshmallow()
#class CompanySchema(ma.Schema):
#    class Meta:
#        model = Company
#    name          = fields.String()
#    logo          = fields.String()
#    course        = fields.String()
#    requirement   = fields.String()
#    place         = fields.String()
#    salary        = fields.String()
#    term          = fields.String()
#    deadline      = fields.String()

make_database()
@app.route("/")
def view_intern():
  companies = Company.query.all()
  names        = []
  logos        = []
  courses      = []
  requirements = []
  places       = []
  salarys      = []
  terms        = []
  deadlines    = []
  for company in companies:
    names.append(company.name)
    logos.append(company.logo)
    courses.append(company.course)
    requirements.append(company.requirement)
    places.append(company.place)
    salarys.append(company.salary)
    terms.append(company.term)
    deadlines.append(company.deadline)
  return jsonify({"names":names,"logos":logos,"courses":courses,"requirements":requirements,"places":places,"salarys":salarys,"terms":terms,"deadlines":deadlines})
  #return jsonify({CompanySchema().dump(companies[3])})


#app.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if(__name__ == "__main__"):
  app.run(host="0.0.0.0",port = 5000, debug =True)