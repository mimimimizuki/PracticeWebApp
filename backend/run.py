from execute_database import insert_into_database
from api import app
from execute_database import inseert_into_database


if __name__ == "__main__":
  insert_into_database()
  app.run(host="0.0.0.0",port = 5000, debug =True)