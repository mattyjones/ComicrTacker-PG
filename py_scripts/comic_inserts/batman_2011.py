import psycopg2

#connect to the db and open a cursor
db_con = psycopg2.connect("dbname=test user=matt")
db_cur = db_con.cursor()



db_cur.execute("""
        INSERT INTO ComicIssue(fkey_defaultseries, comicissue_num, isbn, pubdate, quanity, edition, notes)
        VALUES ('2', '1', '00111', 'Jan 13', '1', '1'),
		('2', '1', '00111', 'Jun 12', '1', '1'),
		('2', '2', '00211', 'Jul 12', '1', '1'),
		('2', '3', '00311', 'Aug 12', '1', '1'),
		('2', '4', '00411', 'Sep 12', '1', '1'),
		('2', '5', '00511', 'Oct 12', '1', '1'),
		('2', '6', '00611', 'Nov 12', '1', '1'),
		('2', '7', '00711', 'Dec 12', '1', '1'),
		('2', '8', '00811', 'Jan 13', '1', '1'),
		('2', '9', '00911', 'Feb 13', '1', '1'),
		

#for row in db_cur.fetchall():
#	print row

#commit all changes to the db and make them persistent
db_con.commit()

#close the cursor and connection
db_cur.close()
db_con.close()

