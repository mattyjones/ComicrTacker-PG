
#db_cur.execute("Select DefaultSeries.defaultseries_id FROM DefaultSeries Where DefaultSeries.defaultseries = %s;" % (TITLE))
import psycopg2

TITLE = 'Batman(1940)'

#connect to the db and open a cursor
db_con = psycopg2.connect("dbname=test user=matt")
db_cur = db_con.cursor()

#print all the rows found in the query
def printall():
	for row in db_cur.fetchall():
		print row

def testing():
	test = db_cur.execute("Select DefaultSeries.defaultseries_id FROM DefaultSeries Where DefaultSeries.defaultseries = '%s';" % (TITLE)) 
	return test

matt = testing()

print matt


printall() # print all the rows from a query

#commit all changes to the db and make them persistent
db_con.commit()

#close the cursor and connection
db_cur.close()
db_con.close()

