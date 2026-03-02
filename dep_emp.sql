create table departmentt(
d_id int primary key,
d_ad varchar2(20));

insert into departmentt values(&d_id,'&d_ad');
select  from departmentt;
commit;

create table iscilerr(
i_id int primary key,
ad varchar2(20),
soyad varchar2(20),
maas int,
d_id int,
foreign key (d_id) references department (d_id));

insert into iscilerr values(&i_id,'&ad','&soyad',&maas,&d_id);
select  from iscilerr;
commit;