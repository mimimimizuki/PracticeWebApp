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
CORS(app)


#make database
db = SQLAlchemy(app)
class Company(db.Model):
  __tablename__ = "companies"
  
  id           = db.Column(db.Integer,primary_key=True,autoincrement=True)
  name         = db.Column(db.Text,nullable=False)
  logo         = db.Column(db.Text,nullable=False)
  courses      = db.Column(db.Text,nullable=False)
  requirements = db.Column(db.Text,nullable=False)
  place        = db.Column(db.Text,nullable=False)
  salary       = db.Column(db.Text,nullable=False)
  term         = db.Column(db.Text,nullable=False)
  deadline     = db.Column(db.Text,nullable=False)
  homepage     = db.column(db.Text)

  def __init__(self,name,logo,courses,requirements,place,salary,term,deadline,homepage):
    self.name        = name
    self.logo        = logo
    self.courses     = courses
    self.requrements = requirements
    self.place       = place
    self.salary      = salary
    self.term        = term
    self.deadline    = deadline
    self.homepage    = homepage

#class User(db.Model):
#  id   = db.Column(db.Integer,primary_key=True,autoincrement=True)
#  name = db.Column(db.String(120))
#  age  = db.Column(db.Integer)

#  def __init__(self,name,age):
#    self.name = name
#    self.age  = age


def insert_into_database():
  yahoo = Company("Yahoo株式会社","./logos/yohoo_logo.jpg","バックエンド","Java or Python","オンライン","1300円/h","8/30〜9/5","6/18 12:00","https://about.yahoo.co.jp/hr/internship/")
  line  = Company("株式会社LINE" ,"./logos/line_logo.jpg" ,"バックエンド","JavaScript" ,"オンライン","1500円/h","9/8～9/17","6/18 12:00","https://linecorp.com/ja/career/newgrads/internship/")
  #user1 = User("John",18)

  db.session.add(yahoo)
  db.session.add(line)
  #db.session.add(user1)
  
  db.session.commit()

#set marshmallow
ma = Marshmallow()
class CompanySchema(ma.Schema):
    class Meta:
        model = Company
    
    name         = fields.String()
    logo         = fields.String()
    courses      = fields.String()
    requirements = fields.String()
    place        = fields.String()
    salary       = fields.String()
    term         = fields.String()
    deadline     = fields.String()
    homepage     = fields.String()

#簡単なデータに対して実行(成功した)
#class UserSchema(ma.Schema):
#    class Meta:
#        model = User    
#    name = fields.String()
#    age  = fields.Integer()

@app.route("/")
def view_intern():
  db.create_all()
  insert_into_database()
  companies = Company.query.all()
  #user = User.query.all()
  #return jsonify({"User":UserSchema().dump(user[0])})
  return jsonify({"Companies":CompanySchema.dump(companies).data})

#app.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if(__name__ == "__main__"):
  app.run(host="0.0.0.0",port = 5000, debug =True)