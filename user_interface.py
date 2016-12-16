import sqlite3
conn = sqlite3.connect('database name')
c=conn.cursor()
c.execute("select * from QUERY_TABLE")
for i in c.fetchall():
    print(*i)
print("choose the topic index to get the entities of the query  eg 1,2 etc...")
c=conn.cursor()
c.execute("select ENTITY,ENTITY_TYPE from ENTITY_TABLE WHERE Q_ID=(?) ORDER BY ENTITY ASC",(input()))
for i in c.fetchall():
    if  str(i[0]).isalpha():
        print(*i)
