import psycopg2
import os

conn = psycopg2.connect(os.environ['DATABASE_URL'])

cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS GUEST(id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, message TEXT NOT NULL)")
conn.commit()

cur.execute('INSERT INTO GUEST (name, message) VALUES (%s, %s)', ("arun", "test"))
conn.commit()

conn.close()