from api import db
from sqlalchemy.types import Integer
from sqlalchemy.types import String
from sqlalchemy.types import Text
                              

class Company(db.Model):
  __tablename__ = "companies"

  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.Text,nullable=False)
  logo = db.Column(db.Text,nullable=False)
  courses = db.Column(db.Text,nullable=False)
  requirements = db.Column(db.Text,nullable=False)
  place = db.Column(db.Text,nullable=False)
  salary = db.Column(db.Text,nullable=False)
  term = db.Column(db.Text,nullable=False)
  deadline = db.Column(db.Text,nullable=False)

  def __init__(self,id,name,logo,courses,requirements,place,salary,term,deadline):
    self.id = id
    self.name = name
    self.logo = logo
    self.courses = courses
    self.requrements = requirements
    self.place = place
    self.deadline = deadline

db.create_all()