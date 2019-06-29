# SQL.pdf

## 기본 세팅

```sqlite
sqlite> .mode csv
sqlite> .import hellodb.csv examples

sqlite> SELECT * FROM examples;

sqlite> .headers on
sqlite> .mode column

## bash에서 실행
$ sqlite3 tutorial.sqlite3
##

sqlite> .databases

sqlite> .tables
sqlite> .schema classmates

sqlite> DROP TABLE classmates;
sqlite> .tables
```



## Create Table

```sql
CREATE TABLE classmates (
id INT PRIMARY KEY,
name TEXT,
age INT,
address TEXT
);
```



## CRUD

```sqlite
# INSERT
sqlite> INSERT INTO classmates (name, age)
 ...> VALUES ('홍길동', 23);
sqlite> INSERT INTO classmates VALUES (2, '홍길동', 50, ‘서울’);  # column 명시안해주고 모든 값들을 채워주는 것도 가능


# 테이블 재생성
sqlite> DROP TABLE classmates;
sqlite> CREATE TABLE classmates (
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT NOT NULL,
age INT NOT NULL,
address TEXT NOT NULL
);


sqlite> SELECT id, name FROM classmates;
sqlite> SELECT id, name FROM classmates LIMIT 1;
sqlite> SELECT id, name FROM classmates LIMIT 1 OFFSET 2;  # 맨 위에서 2개 건너뛰고 3번째 값만 가져오기


sqlite> SELECT id, name FROM classmates WHERE address="서울";


# UPDATE
sqlite> UPDATE classmates
 ...> SET name="홍길동", address="제주도"
 ...> WHERE id=4;
 
 
# DELETE
sqlite> DELETE FROM classmates
 ...> WHERE id=3;
```



## Expressions

```sqlite
sqlite> SELECT * FROM users WHERE age >= 30;

sqlite> SELECT first_name FROM users WHERE age >= 30;

sqlite> SELECT age, last_name FROM users WHERE age >= 30 and
last_name=“김”;

# users 테이블 내의 레코드 개수(= row 수)
sqlite> SELECT COUNT(*) FROM users;

# users에서 계좌 잔액(balance)이 가장 높은 사람과 액수는?
sqlite> SELECT first_name, MAX(balance) FROM users;

# users에서 30살 이상인 사람의 계좌 평균 잔액은?
sqlite> SELECT AVG(balance) FROM users WHERE age >= 30; 
```



### LIKE

정확한 값에 대한 비교가 아닌, 패턴을 확인하여 해당하는 값을 반환한다.

```sqlite
# users에서 20대인 사람의 테이블은?
sqlite> SELECT * FROM users WHERE age LIKE ‘2%’;
```



![스크린샷 2019-04-21 오후 11.31.56](./스크린샷 2019-04-21 오후 11.31.56.png)



## 정렬(ORDER)

```sqlite
Q. users에서 나이순으로 오름차순 정렬하여 상위 10개만 뽑아보면?
sqlite> SELECT * FROM users ORDER BY age ASC LIMIT 10;

Q. users에서 나이순, 성 순으로 오름차순 정렬하여 상위 10개만 뽑아보면?
sqlite> SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;

Q. users에서 계좌잔액순으로 내림차순 정렬하여 해당하는 사람이름 10개만 뽑아보면?
sqlite> SELECT first_name, last_name FROM users ORDER BY balance
DESC LIMIT 10;
```



# orm.pdf

```sql
CREATE TABLE flights (
    id SERIAL PRIMARY KEY,
    origin VARCHAR NOT NULL,
    destination VARCHAR NOT NULL,
    duration INTEGER NOT NULL
);


INSERT INTO flights
    (origin, destination, duration)
    VALUES ('New York', 'Paris', 540);


SELECT * FROM flights;
    
    
SELECT * FROM flights
    WHERE origin = 'Paris';
    
    
SELECT * FROM flights
    WHERE origin = 'Paris' LIMIT 1;
    
    
SELECT COUNT(*) FROM flights
    WHERE origin = 'Paris';
    
    
SELECT * FROM flights WHERE id = 28;


UPDATE flights SET duration = 280
    WHERE id = 6;
    
    
DELETE FROM flights WHERE id = 28;


SELECT * FROM flights
    ORDER BY origin;


SELECT * FROM flights
    ORDER BY origin DESC;


SELECT * FROM flights
    WHERE origin != "Paris"
    
  
SELECT * FROM flights
    WHERE origin LIKE "%a%"


SELECT * FROM flights
    WHERE origin IN ('Tokyo', 'Paris');


# = 하나만 써도 된다
SELECT * FROM flights
    WHERE origin = "Paris"
    AND duration > 500;


SELECT * FROM flights
    WHERE origin = "Paris"
    OR duration > 500;


SELECT * FROM flights JOIN passengers
    ON flights.id = passengers.flight_id;
```











