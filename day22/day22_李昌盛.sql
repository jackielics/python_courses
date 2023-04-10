create database day22 charset=utf8;
use day22;
/* 1、根据上课给的sql历史记录，完成数据库的创建，班级，学生表的创建，表的增删查改操作 */
create table students(
    id int unsigned primary key auto_increment not null,
    name varchar(20) default '',
    age tinyint unsigned default 0,
    height decimal(5,2),
    gender enum('男','女','中性','保密') default '保密',
    cls_id int unsigned default 0,
    is_delete bit(1) default 0
);

-- classes 表
create table classes (
id int unsigned auto_increment primary key not null,
name varchar(30) not null
);

insert into classes values (0, "python_01 期"), (0, "python_02 期");

INSERT INTO students(name,age,height,gender,cls_id,is_delete)   -- 向students表中插入数据
VALUES
	( '小明', 18, 180.00, 2, 1, 0 ),
	( '小月月', 18, 180.00, 2, 2, 1 ),
	( '彭于晏', 29, 185.00, 1, 1, 0 ),
	( '刘德华', 59, 175.00, 1, 2, 1 ),
	( '黄蓉', 38, 160.00, 2, 1, 0 ),
	( '凤姐', 28, 150.00, 4, 2, 1 ),
	( '王祖贤', 18, 172.00, 2, 1, 1 ),
	( '周杰伦', 36, NULL, 1, 1, 0 ),
	( '程坤', 27, 181.00, 1, 2, 0 ),
	( '刘亦菲', 25, 166.00, 2, 2, 0 ),
	( '金星', 33, 162.00, 3, 3, 1 ),
	( '静香', 12, 180.00, 2, 4, 0 ),
	( '郭靖', 12, 170.00, 1, 4, 0 ),
	( '周杰', 34, 176.00, 2, 5, 0 );

SELECT * FROM students WHERE id=18;  -- 查询

DELETE FROM students WHERE id=18;   -- 删除

UPDATE students SET height=199 WHERE id=36; -- 修改

/* 2、能够备份数据库，删除数据库后，能够恢复数据库 */
--备份数据库
mysqldump -uroot -p day22 > day22.SQL	--终端备份数据库
--删除数据库
drop database day22;	--MySQL删除数据库
--恢复数据库
mysql -uroot -p day22 < day22.sql	--终端恢复数据库

/* 3、完成条件，排序，聚合，分组等操作，与上课一致 */
select * from students where id > 3;    -- 条件

select * from students where gender=1 and is_delete=0 order by id desc; -- 排序

SELECT COUNT(*) AS num_ids,
        MIN(id) AS id_min,
        MAX(id) AS id_max,
        AVG(id) AS id_avg
FROM students;  -- 聚合
/* 4、完成内连接，左连接，右连接的练习 */
select * from students inner join classes on students.cls_id = classes.id;  -- 内连接

select * from students as s left join classes as c on s.cls_id = c.id;  -- 左连接

select * from students as s right join classes as c on s.cls_id = c.id;  -- 右连接

/* 5、完成自关联，子查询的练习 */

-- 自关联：一个表与自己进行关联，一般用于查询同一张表中的数据
select * from students as s1 inner join students as s2 on s1.cls_id = s2.cls_id;
-- 子查询：在一个查询语句中，嵌套了另一个查询语句，一般用于查询不同表中的数据
select name from classes where id in (select cls_id from students);

/* 6、完成外键添加与删除练习 */
-- 外键：在表中添加一个字段，该字段的值必须是另一个表中的主键值
-- 外键的作用：保证数据的完整性，避免数据的冗余
ALTER TABLE students ADD CONSTRAINT fk_students_classes FOREIGN KEY (cls_id) REFERENCES classes(id);
