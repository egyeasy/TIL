-- 1.
CREATE TABLE movies (
    영화코드 INT PRIMARY KEY,
    영화이름 TEXT,
    관람등급 TEXT,
    감독 TEXT,
    개봉연도 INTEGER,
    누적관객수 INTEGER,
    상영시간 INTEGER,
    제작국가 TEXT,
    장르 TEXT
    );
    
-- 2.
.mode csv
.headers on
    
-- 3.
SELECT * FROM movies;