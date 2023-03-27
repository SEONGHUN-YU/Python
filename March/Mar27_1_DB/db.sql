-- OracleDB로 대표되는 RDBMS
--		테이블을 정의, 테이블간의 관계를 중심으로 해결
--		정의했던 규칙에 안 맞으면 에러
--		=> 정형데이터[기상청 날씨 같은 거] 처리(저장)하기에 좋음(웹개발 등)
-- 		=> 비정형데이터[소설책, 뉴스 같은 거] 처리하기에 부적합함(안 좋음)

-- NoSQL : MongoDB - Node.js팀에서 만든 거
--		hu(mongo)usDB
--		그렇다보니, DB를 Javascript로 제어함
--		=> 비정형데이터 처리에 적합

-- jQuery -> Node.js
--			JavaScript로 하는 back-end

-- OracleDB는 역사적으로 오래됨
-- mongoDB는 얼마 안 됨 -> 따라서, 눈치볼 거 없이 그냥 최신버젼

-- 서버 -> Linux스럽게 해보자
-- Install MongoD as a Service : 윈도우에서 제어하겠다
-- 체크해제

-- Install MongoDB Compass : MongoDB를 제어하는 GUI프로그램
-- 체크해제

create table mar27_coffee(
	c_name varchar2(10 char) primary key,
	c_price number(5) not null
);

select * from mar27_coffee;
