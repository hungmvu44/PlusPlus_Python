-- create database "student_cms_plusplus"
create schema student_cms_plusplus;

-- create student, class and student_class table
create table student_cms_plusplus.student(
id INT primary key,
full_name varchar(45) NULL,
mssv INT NULL,
password1 varchar(20) NOT NULL,
phone int NULL,
email varchar(45) NULL,
created_timstamp timestamp default current_timestamp,
last_update_timestamp timestamp default current_timestamp
);

create table student_cms_plusplus.class(
id INT primary key,
full_name varchar(45) NULL,
major varchar(45) NULL,
total_student int NOT NULL,
teacher_name varchar(45) NULL,
teacher_phone int(10) NULL,
created_timstamp timestamp default current_timestamp,
last_update_timestamp timestamp default current_timestamp

);

create table student_cms_plusplus.student_class(
student_id int,
class_id int
);