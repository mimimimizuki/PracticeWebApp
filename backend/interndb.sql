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

INSERT INTO companies VALUES(1,"LINE株式会社","link","フロントエンド/バックエンド","JavaScriptでの開発経験","オンライン","1500/h","9/6～9/17","6/14");

INSERT INTO companies VALUES(2,"株式会社Yahoo","link","バックエンド","Javaでの開発経験","オンライン","1200/h","8/30～9/5","6/18");

INSERT INTO companies VALUES(3,"株式会社voyage group","link","バックエンド","goでの開発経験","オンライン","1300/day","8/6～8/27","5/31");

INSERT INTO companies VALUES(4,"楽天グループ株式会社","link","バックエンド/データサイエンス","JavaScript","東京本社","1100/h","9/21～9/29","6/22");
