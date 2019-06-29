# workshop

```sql
-- 칼럼 추가 
ALTER TABLE bands
ADD members INTEGER;

UPDATE bands
SET members = 4
WHERE id == 1;

UPDATE bands
SET members = 5
WHERE id == 2;

UPDATE bands
SET members = 9
WHERE id == 3;


-- members 수정
UPDATE bands
SET members = 5
WHERE id == 3;

-- 레코드 삭제
DELETE FROM bands
WHERE id == 2;
```







# homework

```sql
-- 테이블 생성
CREATE TABLE friends (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL
);

-- 데이터 입력
INSERT INTO friends (name, location)
VALUES ("Justin", "Seoul");
INSERT INTO friends (name, location)
VALUES ("Simon", "New York");
INSERT INTO friends (name, location)
VALUES ("Chang", "Las Vegas");
INSERT INTO friends (name, location)
VALUES ("John", "Sydney");

-- 스키마 변경
ALTER TABLE friends
ADD married INTEGER;

-- 데이터 추가
UPDATE friends
SET married = 0;

UPDATE friends
SET married = 1
WHERE id == 1 OR id == 4;

-- 데이터 삭제
DELETE FROM friends
WHERE married == 0;

-- 테이블 삭제
DROP TABLE friends;
```

