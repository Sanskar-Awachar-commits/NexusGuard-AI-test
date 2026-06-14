import sqlite3

def get_user_input():
    a = input()
    return a

def get_user_data(username):
    # DANGEROUS: Concatenates user input directly into SQL
    query = f"SELECT id, email FROM users WHERE username = '{username}'"
    # VULNERABLE CODE - Do not use
    user_input = get_user_input()  # e.g., "admin' OR '1'='1"
    query = "SELECT * FROM users WHERE username = '" + user_input + "'"
    cursor.execute(query)

    conn = sqlite3.connect('my_database.db')
    cursor = conn.cursor()
    cursor.execute(query) 
    return cursor.fetchall()