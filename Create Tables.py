import sqlite3
conn = sqlite3.connect('database name')
print("Opened database successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS QUERY_TABLE
       (Q_ID INT    NOT NULL   ,
       Q_STRING          VARCHAR(40) PRIMARY KEY   );''')
print("Table created successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS RESULT_TABLE
       (Q_ID INT      NOT NULL,
       TITLE          VARCHAR(80) ,
       URL            VARCHAR(1024) ,
       SNIPPET       VARCHAR(256));''')
print("Table created successfully")

conn.execute('''CREATE TABLE IF NOT EXISTS ENTITY_TABLE
       (Q_ID INT     NOT NULL,
       ENTITY          VARCHAR(40),
       ENTITY_TYPE     VARCHAR(60)  );''')
print("Table created successfully")
#(SELECT max(a)FROM t1)+1)
conn.close()
