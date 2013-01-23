import psycopg2

conn = psycopg2.connect("dbname=test user=matt")

cur = conn.cursor()

cur.execute("INSERT INTO defaultseries(defaultseries) values ('Nightwing(1995)')
