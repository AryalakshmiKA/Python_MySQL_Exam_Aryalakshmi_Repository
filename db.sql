create database shop_db;
use shop_db;
create table product(id int primary key auto_increment, name varchar(100), category varchar(50), price decimal(10,2), quantity int, manufacturer varchar(100));