# TODO list

This program can create and manage agenda for a month.

Agendas for multiple months can be created worked upon.



> install necessary packages

```bash
pip install mysql-connector-python
pip install datetime
pip install tabulate
```

> sql commands

```sql
-- create database
create database agenda;
use agenda
```

```sql
-- Create table
create table month1(
    tid int(5) primary key auto_increment,
    status varchar(20) default "NOT COMPLETED",
    name varchar(20) not null,
    time datetime,
    place varchar(20)
);

-- insert into table
insert into month1(name,time,place) values('shopping','2022-04-25 12:30','mall');
insert into month1(tid,name,time,place) values('homework','2022-04-22 15:30','home');
insert into month1(name,time,place) values('play','2022-04-22 17:30','park');
insert into month1(name,time,place) values('clean','2022-04-29 7:30','terrace');
insert into month1(name,time,place) values('youtube','2022-04-25 20:30','home');
insert into month1(name,time,place) values('cycling','2022-04-22 17:30','track');

-- display
select * from month1;

-- exit
exit

```

> date format

```py
date = datetime(2021, 8, 22, 11, 2)
```


