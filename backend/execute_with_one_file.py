from flask import Flask,jsonify,request,render_template
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.types import Integer
from sqlalchemy.types import String
from sqlalchemy.types import Text
from flask_marshmallow import Marshmallow
#from marshmallow_sqlalchemy import ModelSchema

#default config
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///intern.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
CORS(app)


#make database
db = SQLAlchemy(app)
class Company(db.Model):
  __tablename__ = "companies"

  id           = db.Column(db.Integer,primary_key=True)
  name         = db.Column(db.Text,nullable=False)
  logo         = db.Column(db.Text,nullable=False)
  courses      = db.Column(db.Text,nullable=False)
  requirements = db.Column(db.Text,nullable=False)
  place        = db.Column(db.Text,nullable=False)
  salary       = db.Column(db.Text,nullable=False)
  term         = db.Column(db.Text,nullable=False)
  deadline     = db.Column(db.Text,nullable=False)

  def __init__(self,id,name,logo,courses,requirements,place,salary,term,deadline):
    self.id          = id
    self.name        = name
    self.logo        = logo
    self.courses     = courses
    self.requrements = requirements
    self.place       = place
    self.deadline    = deadline

def insert_into_database():
  yahoo = Company(1,"Yahoo株式会社","./logos/yahoo_logo.jpg","バックエンド", "JavaもしくはPythonの経験","オンライン","1300円/h","8/30～9/5","6/18 12:00")
  line = Company(2,"株式会社LINE","./logos/line_logo.jpg","バックエンド", "JavaScript経験","オンライン","1500円/h","9/8～9/17","6/18 12:00")

  db.session.add(yahoo)
  db.session.add(line)
  db.session.commit()

#set marshmallow
ma = Marshmallow()
class CompanySchema(ma.Schema):
    class Meta:
        model = Company


@app.route("/intern", methods=["GET"])
def view_intern():
  db.create_all()
  insert_into_database()
  companies = Company.quary.all()
  #for company in companies:
  #  print(company.id,company.name,company.logo,company.courses,company.requirements,company.place,company.salary,company.term,company.deadline) 
  return jsonify({"Companies":CompanySchema.dump(companies).data})

if(__name__ == "__main__"):
  app.run(host="0.0.0.0",port = 5000, debug =True)