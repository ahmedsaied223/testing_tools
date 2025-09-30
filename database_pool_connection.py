import psycopg2
from psycopg2 import pool

connection_pool = psycopg2.pool.SimpleConnectionPool(1, 10, user='postgres', password='', host='localhost', port=5432, database='postgres')

 # get connction from the pool

connection = connection_pool.getconn()

# use the connections
cursor = connection.cursor()

employ_id  = cursor.execute('select * from users where id = 10')
print(employ_id)
cursor.execute('select * from users')
for row in cursor:
    print(row)poo

result = cursor.fetchall()
for row in result:
    print(row)

cursor.close()


