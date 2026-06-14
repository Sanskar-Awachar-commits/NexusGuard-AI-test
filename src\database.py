from sqlalchemy import text

def execute_query(db_session, query, params=None):
    if params is None:
        params = {}
    query_text = text(query)
    result = db_session.execute(query_text, params)
    return result