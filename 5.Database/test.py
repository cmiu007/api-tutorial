import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor() # run the query and store the result

create_table = "CREATE TABLE users(id int, username text, password text)"

cursor.execute(create_table)

user = (1, 'jose', 'asdf')
insert_query = "INSERT INTO users VALUES (?,?,?)"
cursor.execute(insert_query, user)

users = [
    (2, 'martin', 'asdf'),
    (3, 'anna', 'asdf'),
    (4, 'cmiu', 'asdf')
]

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"

for row in cursor.execute(select_query):
    print (row)

connection.commit()

connection.close()