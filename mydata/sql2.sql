show databases;
use kani;
create table std5 (sno int primary key,sname varchar(20),place varchar(20),mark1 int,mark2 int,mark3 int);
insert into std5 values(1,"kani",'mailai',56,54,43);
insert into std5 values(2,"mani",'sembai',78,98,90);
insert into std5 values(3,"pavi",'sembai',78,98,87);
select * from std5;


