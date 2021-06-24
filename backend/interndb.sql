CREATE DATABASE IF NOT EXISTS intern_db;
USE intern_db;

CREATE TABLE intern_db.companies(
  company_id int primary key,
  company_name text,
  company_logo  text,
  courses text,
  requirements text,
  place text,
  salary text,
  term  text,
  deadline text
);

INSERT INTO companies VALUES(1,"LINE株式会社","link", "バックエンドエンジニア", "JavaScript","オンライン","1500/h","9/6~9/17","6/14");
