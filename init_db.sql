create table company (
    company_id int primary key,
    company_name text not null,
);

create table internship (
    intern_id int, 
    company_id int,
    course_day date,
    requirement text, -- skill など
    salary int, --1500
    work_location text,
    foreign key company_id(internship) references from company_id(company)
);

insert into company(company_name) values 1, 'rakuten';
-- react to python 
{
    company_name : "LINE", 
}
select * from company; 
select * from internship where company_id = 4;
JSON形式
'http://localhost:8080/get_internship/1'

reponse = {
    "intern_id" : 1, 
    "company_id" : "LINE",
    "course_day" : 
}
reactでは、
response["intern_id"]