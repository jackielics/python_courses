create table classes(
    id int unsigned auto_increment primary key not null ,
    name varchar(10)
);


insert into classes values(0,'python7');  

create table students(
    id int unsigned primary key auto_increment not null,
    name varchar(20) default '',
    age tinyint unsigned default 0,
    height decimal(5,2),
    gender enum('男','女','保密'),
    cls_id int unsigned default 0
);

insert into students values(0,'郭靖',18,181,'男',1);

select * from mysql;