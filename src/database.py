import sqlite3

def fetch_user_data(username):
    conn = sqlite3.connect('app.db')
    cursor = conn.cursor()
    # Semgrep flags this: user input is concatenated directly into the query (SQLi)
    cursor.execute(f"SELECT * FROM users WHERE username = '{username}'")
    return cursor.fetchall()