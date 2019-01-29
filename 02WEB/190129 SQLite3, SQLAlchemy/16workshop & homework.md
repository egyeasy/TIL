# workshop

```sql
CREATE TABLE friends (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    location TEXT NOT NULL
);

INSERT INTO friends (name, location)
VALUES ("Justin", "Seoul");
INSERT INTO friends (name, location)
VALUES ("Simon", "New York");
INSERT INTO friends (name, location)
VALUES ("Chang", "Las Vegas");
INSERT INTO friends (name, location)
VALUES ("John", "Sydney");

SELECT * FROM friends;

ALTER TABLE friends
ADD married INTEGER;

SELECT * FROM friends;

UPDATE friends
SET married = 0;

UPDATE friends
SET married = 1
WHERE id == 1 OR id == 4;

SELECT * FROM friends;

DELETE FROM friends
WHERE married == 0;

SELECT * FROM friends;


-- workshop
ALTER TABLE bands
ADD debut INTEGER;


UPDATE bands
SET members = 4
WHERE id == 1;

UPDATE bands
SET members = 5
WHERE id == 2;

UPDATE bands
SET members = 9
WHERE id == 3;



UPDATE bands
SET members = 5
WHERE id == 3;


DELETE FROM bands
WHERE id == 2;
```







# homework

