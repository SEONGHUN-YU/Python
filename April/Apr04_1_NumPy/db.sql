-- 제일 더운 시간대, 최고기온
select kw_hour, avg(kw_temp) from kma_weather group by kw_hour having avg(kw_temp) = (select max(avg(kw_temp)) from kma_weather group by kw_hour);

-- 제일 추운 시간대, 최저기온
select kw_hour, avg(kw_temp) from kma_weather group by kw_hour having avg(kw_temp) = (select min(avg(kw_temp)) from kma_weather group by kw_hour);

-- 평균기온보다 더운 시간대, 기온
select kw_hour, avg(kw_temp) from kma_weather group by kw_hour having avg(kw_temp) > (select avg(avg(kw_temp)) from kma_weather group by kw_hour) order by kw_hour;

-- select 뭐 볼 건지
-- from 대상
-- where 데이터 필터링
-- group by 그룹 별로 묶을 때
-- having 그룹 바이한 거 필터링
-- order by 정렬