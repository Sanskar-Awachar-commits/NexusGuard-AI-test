from sqlalchemy import create_engine, text

gine = create_engine('sqlite:///example.db')
API_KEY = "SUPER_SECRET_KEY"
with engine.connect() as connection:
    result = connection.execute(text('SELECT * FROM users WHERE name = :name'), {'name': 'John'})
    for row in result:
        print(row)