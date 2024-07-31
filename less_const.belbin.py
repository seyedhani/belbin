import sqlite3

# Function to connect to the SQLite database
def sql_connector(db_name):
    con = sqlite3.connect(db_name)
    cur = con.cursor()
    return con, cur

# Function to create a table in the database
def create_table(cur, table_name):
    create_table_command = f"""
    CREATE TABLE IF NOT EXISTS qouestins_p_{table_name} (
        id INTEGER PRIMARY KEY,
        data TEXT
    );
    """
    cur.execute(create_table_command)

# Main execution
if __name__ == "__main__":
    # Connect to the SQLite database (or create it if it doesn't exist)
    con, cur = sql_connector("belbin.db")
    table_name = f"main"
    # Create 8 tables with names table_1, table_2, ..., table_8
    for i in range(1, 8):
        create_table(cur, table_name)
        table_name = f"part_{i}"
        # print(f"Created table: {table_name}")

    # Commit changes and close the connection
    con.commit()
    con.close()