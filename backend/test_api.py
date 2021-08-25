from flask import Flask,jsonify,request
import json
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column,Integer,String,Text
from flask_marshmallow import Marshmallow
from flask_marshmallow.fields import fields
from sqlalchemy.sql.schema import PrimaryKeyConstraint


#default config
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test_api.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['JSON_AS_ASCII'] = False
CORS(app)


#make database
db = SQLAlchemy(app)

class User(db.Model):
  id   = db.Column(db.Integer,primary_key=True,autoincrement=True)
  name = db.Column(db.Text)
  age  = db.Column(db.Integer)

  def __init__(self,name,age):
    self.name = name
    self.age  = age


def insert_into_database():
  user1 = User("John",18)
  db.session.add(user1)
  db.session.commit()

#set marshmallow
ma = Marshmallow()
class UserSchema(ma.Schema):
    class Meta:
        model = User    
    name = fields.String()
    age  = fields.Integer()

@app.route("/")
def view_intern():
  db.drop_all()
  db.create_all()
  insert_into_database()
  user = User.query.all()
  return jsonify({"User":UserSchema().dump(user[0])})

#app.pyをターミナルから直接呼び出した時だけ、app.run()を実行する
if(__name__ == "__main__"):
  app.run(host="0.0.0.0",port = 5000, debug =True)