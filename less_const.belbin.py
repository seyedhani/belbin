import sqlite3
def sql_connector(path):
    con = sqlite3.connect(path)
    cur = con.cursor()
    return con , cur
def creat_table(command , con , cur):
    cur.execute(command)
    con.commit()
def insert(com , con , cur, entity):
    cur.execute(com, entity)
    con.commit()
def read_specific_lines(filename, line_numbers):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        selected_lines = [lines[i ].strip() for i in line_numbers]
    return selected_lines 
def uniq(x, y):
    file_path = 'all_Q.txt'
    line_numbers_to_read = list(range(x, y))
    return read_specific_lines(file_path, line_numbers_to_read)   
def qoues(i):
    return uniq(i, i+1)[::-1] 
def fileToStr():
    qouestions = [ ]
    for i in range(7):
        q = qoues(i)
        qouestions.append(q)
    return qouestions
def strToData(com , con , cur , arr):
    for i in range(7):
        numb = i + 1
        txt = str(arr[i ])
        entity = (numb , txt )
        insert(com ,con , cur , entity)
comm_a = "CREATE TABLE IF NOT EXISTS main_qousetions (id integer PRIMARY KEY , qoustin text )"
com_a = "INSERT INTO main_qousetions  VALUES(? , ? )" 
con , cur = sql_connector("alldata.db")
creat_table(comm_a, con,cur)
q = fileToStr()
strToData(com_a,con , cur , q)
comm_b = "CREATE TABLE IF NOT EXISTS qousetions (id integer PRIMARY KEY , qoustin text )"