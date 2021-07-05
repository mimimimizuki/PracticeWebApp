from init_database import Company
from api import db

yahoo = Company(1,"Yahoo株式会社","./logos/yahoo_logo.jpg","バックエンド", "JavaもしくはPythonの経験","オンライン","1300円/h","8/30～9/5","6/18 12:00")
line = Company(2,"株式会社LINE","./logos/line_logo.jpg","バックエンド", "JavaScript経験","オンライン","1500円/h","9/8～9/17","6/18 12:00")

db.session.add(yahoo)
db.session.add(line)
db.session.commit()