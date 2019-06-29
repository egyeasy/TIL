import sqlite3

conn = sqlite3.connect("datafile")
cursor = conn.cursor()
cursor.execute("drop table test")
cursor.execute("create table test (name text,count integer)")
cursor.execute("insert into test(name,count) values('Terry',1)")
cursor.execute("insert into test(name,count) values('Cath',2)")

conn.commit()

result = cursor.execute("select * from test")

alist = []

while True:
    row = result.fetchone()
    alist.append(result.fetchone())
    if row == None:
        break
    print(row)
    print(alist)

conn.close()