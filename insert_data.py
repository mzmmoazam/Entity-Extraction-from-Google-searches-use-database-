import sqlite3
conn = sqlite3.connect('database name')
c=conn.cursor()
f=open("E:\extract nouns and verbs from google search items/Albert Camus.json")

import textrazor
textrazor.api_key = "textrazor API"
client = textrazor.TextRazor(extractors=["entities", "topics"])


def insert_in_Query_table():
    try:
        c.execute("select max(Q_ID) from QUERY_TABLE")
        id=c.fetchone()
        if str(id)=="(None,)":
            id=1
        else:
            id=id[0]+1
        #print(id)
        c.execute("Insert into QUERY_TABLE(Q_ID,Q_STRING) values(?,?)",(id,o["query"]["q"]))
        conn.commit()
    except sqlite3.IntegrityError:
        print("THIS QUERY IS already in the table")
def display_QUERY_TABLE():
    c.execute("select * from QUERY_TABLE")
    for i in c.fetchall():
        print(i)
def insert_in_RESULT_TABLE():
    c.execute("select Q_ID from QUERY_TABLE WHERE Q_STRING=(?)",(o["query"]["q"],))
    id = c.fetchone()[0]
    for i in range(10):
        c.execute("insert into RESULT_TABLE(Q_ID,TITLE,URL,SNIPPET) VALUES  (?,?,?,?)",(id,o["result"][i]["title"],o["result"][i]["link"],o["result"][i]["snippet"]))
        conn.commit()
'''def insert_in_Entity_table():
    c.execute("select Q_ID from QUERY_TABLE WHERE Q_STRING=(?)", (o["query"]["q"],))
    id = c.fetchone()[0]
    for i in range(10):
        response = client.analyze(o["result"][i]["snippet"])
        for entity in response.entities():
            if str(entity.id) == "[]" or not str(entity.id).isdigit():
                c.execute("insert into  ENTITY_TABLE(Q_ID,ENTITY,ENTITY_TYPE) values(?,?,?)",
                          (id, str(entity.id), str(entity.freebase_types)))
                conn.commit()
        response = client.analyze_url(o["result"][i]["link"])
        for entity in response.entities():
            c.execute("insert into  ENTITY_TABLE(Q_ID,ENTITY,ENTITY_TYPE) values(?,?,?)",
                      (id, str(entity.id), str(entity.freebase_types)))
            conn.commit()
        '''
def insert_in_Entity_table():
    c.execute("select Q_ID from QUERY_TABLE WHERE Q_STRING=(?)", (o["query"]["q"],))
    id = c.fetchone()[0]
    entity_dict={}
    for i in range(10):
        response = client.analyze(o["result"][i]["snippet"])
        for entity in response.entities():
            if str(entity.id) == "[]" and not str(entity.id).isdigit():
                if entity.id in entity_dict:
                    entity_dict[entity.id].append(entity.freebase_types)
                else:
                    entity_dict[entity.id]=[]
                    entity_dict[entity.id].append(entity.freebase_types)
        response = client.analyze_url(o["result"][i]["link"])
        for entity in response.entities():
            if entity.id in entity_dict:
                entity_dict[entity.id].append(entity.freebase_types)
            else:
                entity_dict[entity.id] = []
                entity_dict[entity.id].append(entity.freebase_types)
    for entity1 in entity_dict:
        c.execute("insert into  ENTITY_TABLE(Q_ID,ENTITY,ENTITY_TYPE) values(?,?,?)",
                          (id, str(entity1), str(entity_dict[entity1])))
        conn.commit()
def display_result_table():
    c.execute("select * from RESULT_TABLE")
    for i in c.fetchall():
        print(i)
def display_entity_table():
    c.execute("select * from ENTITY_TABLE")
    for i in c.fetchall():
        print(i)



text=f.read()
o=eval(text)

insert_in_Query_table()
display_QUERY_TABLE()
insert_in_RESULT_TABLE()
display_result_table()
insert_in_Entity_table()
display_entity_table()
conn.close()
