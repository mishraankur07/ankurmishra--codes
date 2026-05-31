create database ankur;
use ankur;
create table employee(
    id int primary key,
    name varchar(20),
    age int,
    department varchar(20)
);
insert into employee values(1, 'Ankur', 30, 'IT');
insert into employee values(2, 'Ravi', 25, 'HR');
insert into employee values(3, 'Sita', 28, 'Finance');
select * from employee;
update employee set age = 31 where id = 1;
delete from employee where id = 2;
select * from employee;
drop table employee;
desc employee;
drop database ankur;    
