from flask import Flask,jsonify,request,render_template
import json
from flask_cors import CORS

# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.types import Integer
# from sqlalchemy.types import String
# from sqlalchemy.types import DateTime

app = Flask(__name__)
CORS(app)
# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.intern"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# db = SQLAlchemy(app)

# class Intern(db.Model):
#   id = db.Column(db.Integer,primary_key=True)
#   company_name = db.Column(db.String(128),nullable=False)
#   skills = db.Column(db.String(128),nullable=False)
#   start = db.Column(db.DateTime,nullable=False)
#   end = db.Column(db.DateTime,nullable=False)

@app.route("/intern")
def index():
  return {"companies":["楽天株式会社", "LINE株式会社", "株式会社VOYAGE", "メルカリ"],
          "siteURLs":["","","https://voyagegroup.snar.jp/",""],
          "internURLs":["","","","https://mercan.mercari.com/articles/28040/"]}
  # return render_template("index.html",title = "change test")



if __name__ == "__main__":
  #db.create_all()
  app.run(host="0.0.0.0",port = 5000, debug =True)