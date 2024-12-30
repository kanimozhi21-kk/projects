show databases; 
create database kmooz;
use kmooz;
create table emp1(eno int not null auto_increment primary key,ename varchar(20),etime varchar(5),eage int);
insert into emp1 values(1,"mano","10.00",32);
insert into emp1 values(2,"madhu","09.00",30);
insert into emp1 values(3,"pranav","11.00",28);
insert into emp1 values(4,"saro","10.24",26);
insert into emp1 values(5,"priya","10.11",27);
select * from emp1;

update emp1 set ename="aruna" where eno=5;
select *from emp1;
delete from emp1 where eno=5;
select *from emp1;
select ename from emp1 where eno=3;


