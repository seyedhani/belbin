import sqlite3

def create_database(db_name):
    """Create a SQLite database and return the connection and cursor."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    return conn, cursor

def create_tables(cursor):
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS main_questions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT
    )
    ''')

    for i in range(1, 8):
        cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS questions{i} (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT
        )
        ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        summary TEXT,
        feature TEXT,
        weaknesses TEXT,
        incentives TEXT
    )
    ''')
def insert_results(cursor, data):
    """Insert data into results table."""
    for entry in data:
        cursor.execute('INSERT INTO results (summary, feature, weaknesses, incentives) VALUES (?, ?, ?, ?)', entry)    
def process_data(lines):
    """Process lines into tuples of (summary, feature, weaknesses, incentives)."""
    data = []
    for i in range(64, 96, 4):  
        if i + 3 < len(lines):  
            summary = lines[i].strip()
            feature = lines[i + 1].strip()
            weaknesses = lines[i + 2].strip()
            incentives = lines[i + 3].strip()
            data.append((summary, feature, weaknesses, incentives))
    return data   
def insert_main_questions(cursor, lines):
    """Insert the first 7 lines into the main_questions table."""
    for line in lines[:7]:
        cursor.execute('INSERT INTO main_questions (question) VALUES (?)', (line.strip(),))

def insert_questions(cursor, lines):
    """Insert subsequent lines into questions1 to questions7 tables."""
    for i in range(7):
        for j in range(8):
            index = 7 + i * 8 + j
            if index < len(lines):
                cursor.execute(f'INSERT INTO questions{i+1} (question) VALUES (?)', (lines[index].strip(),))

def read_data(file_name):
    """Read data from a text file and return the lines."""
    with open(file_name, 'r', encoding='utf-8') as file:
        return file.readlines()

def main():
    db_name = 'questions.db'
    file_name = 'all_Q.txt'
    lines = read_data(file_name)
    data = process_data(lines)
    conn, cursor = create_database(db_name)
    create_tables(cursor)
    insert_main_questions(cursor, lines)
    insert_questions(cursor, lines)
    insert_results(cursor, data)
    conn.commit()
    conn.close()
if __name__ == "__main__":
    main()

    