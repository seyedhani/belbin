import sqlite3
def create_database(db_name):
    """Create a SQLite database and return the connection and cursor."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    return conn, cursor
def read_specific_data(cursor, condition):
    """Read specific data from the results table based on a condition."""
    query = f'SELECT summary FROM results WHERE id={condition}'
    cursor.execute(query)
    return cursor.fetchall()
db_name = 'questions.db'
con , cur = create_database(db_name)
for i in range(8):
    cond = i
    print(read_specific_data(cur,cond))
