from sqlalchemy import text

def execute_query(db_connection, user_id):
    query = text("SELECT * FROM users WHERE id = :user_id")
    result = db_connection.execute(query, {'user_id': user_id})
    return result.fetchall()