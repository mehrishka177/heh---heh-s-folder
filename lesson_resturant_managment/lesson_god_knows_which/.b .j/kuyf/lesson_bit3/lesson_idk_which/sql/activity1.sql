create table supplier(
    sno text primary,
    sname text,
    statuus1 integer,
    city text

);
insert into supplier(sno,sname,status1,city)
values('s1','Smith',20,'London'),
('s2','Jones',10,'Paris'),
('s3','Blake',30,'Paris'),
('s4','Clark',20,'London'),
('s5','Adams',30,'Athens');

select * from supplier;
