create table seoul_dust(
	sd_when date not null,
	sd_MSRRGN_NM char(3 char) not null,
	sd_MSRSTE_NM varchar2(4 char) not null,
	sd_PM10 number(4, 1) not null,
	sd_PM25 number(4, 1) not null,
	sd_IDEX_NM varchar2(6 char) not null
);

select * from seoul_dust;