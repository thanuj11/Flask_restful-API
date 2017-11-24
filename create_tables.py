import sqlite3

conn=sqlite3.connect('data.db')
cursor=conn.cursor()

create_table="create table users(id INTEGER PRIMARY KEY, username text, password text)"
cursor.execute(create_table)

create_table="create table items(name text,price real)"
cursor.execute(create_table)

#cursor.execute("insert into items values ('test',10.99)")
conn.commit()
conn.close()