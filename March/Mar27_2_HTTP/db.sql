-- 파싱 -> .csv(누가 지우면...?)
-- 파싱 -> DB -> 안전하게 DB에
create table kma_weather(	
	kw_when date not null,
	kw_hour number(2) not null,
	kw_temp number(3, 1) not null,
	kw_wfKor varchar2(10 char) not null
);

select * from kma_weather;
