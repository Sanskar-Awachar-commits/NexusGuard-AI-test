import sqlite3

def get_user_data(username):
    # DANGEROUS: Concatenates user input directly into SQL
    query = f"SELECT id, email FROM users WHERE username = '{username}'"
    
    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute(query) 
    return cursor.fetchall()
