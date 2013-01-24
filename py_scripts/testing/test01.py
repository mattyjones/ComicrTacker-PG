
#db_cur.execute("Select DefaultSeries.defaultseries_id FROM DefaultSeries Where DefaultSeries.defaultseries = %s;" % (TITLE))
import psycopg2


TITLE = ['Batman(1940)',
	'Batman(2011)',
	'Batgirl(2011)']



#connect to the db and open a cursor
db_con = psycopg2.connect("dbname=comics user='matt'")
db_cur = db_con.cursor()


#print all the rows found in the query
#def printall():
#	for row in db_cur.fetchall():
#		print row

#def testing():



#---------------------------------------#
# get_series_id				#
#					#
# takes: a list				#
# returns: the pk of each list item	#
#					#
#					#
#---------------------------------------#

def get_series_id(TITLE):
	#i = iter(TITLE)
	#for word in TITLE:
	name = i.next()
#	item = name
#	db_cur.execute("Select DefaultSeries.defaultseries_id FROM DefaultSeries Where DefaultSeries.defaultseries = '%s';" % (name))
	db_cur.execute("Select * FROM DefaultSeries Where DefaultSeries.defaultseries = '%s';" % (name))
	item = db_cur.fetchone()
	#print name, item
	#return name, item
	return item
		
#get_series_id(TITLE)

#item = ''
#name = ''
#item = ' '

i = iter(TITLE)
for word in TITLE:
	item = get_series_id(TITLE)
	#print name, item
	print item[0]
	print item[1]
	
	if item[1] == TITLE[1]:
		#db_cur.execute("INSERT INTO ComicIssue(fkey_defaultseries_id, comicissue_num, isbn, pubdate, quanity, edition) VALUES ('%s', '0', '00011', 'Nov12', '1', '1');" % (item)) 
	elif item[1] == TITLE[2]:
		#db_cur.execute("INSERT INTO ComicIssue(fkey_defaultseries_id, comicissue_num, isbn, pubdate, quanity, edition) VALUES ('%s', '1', '00011', 'Aug12', '1', '3');" % (item)) 
	elif item[1] == TITLE[3]:
		#db_cur.execute("INSERT INTO ComicIssue(fkey_defaultseries_id, comicissue_num, isbn, pubdate, quanity, edition) VALUES ('%s', '0', '00011', 'Jun12', '1', '1');" % (item)) 


#	print item, name


#	return test

#matt = testing()

#print matt


#printall() # print all the rows from a query

#commit all changes to the db and make them persistent
db_con.commit()

#close the cursor and connection
db_cur.close()
db_con.close()

