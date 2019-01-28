CREATE TABLE bands (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    debut INTEGER NOT NULL
);

INSERT INTO bands (name, debut) VALUES ('Queen', 1973);
INSERT INTO bands (name, debut) VALUES ('Coldplay', 1998);
INSERT INTO bands (name, debut) VALUES ('MCR', 2001);

SELECT id, name FROM bands;

SELECT name FROM bands WHERE debut < 2000;