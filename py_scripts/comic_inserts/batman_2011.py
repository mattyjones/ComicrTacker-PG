import sys

if "/home/matt/ComicTracker-PG/libs" not in sys.path:
	sys.path.append("/home/matt/ComicTracker-PG/libs")

import ct_functions.py as ct_funct

db_con, db_cur = db_connection()



db_cur.execute("""
INSERT INTO ComicIssue(fkey_defaultseries, comicissue_num, isbn, pubdate, quanity, edition)
        VALUES ('2', '0', '00011', 'Nov 12', '1', '1'), 
                ('2', '0', '00011', 'Nov 12', '1', '1'),
                ('2', '0', '00021', 'Nov 12', '1', '1'),
                ('2', '1', '00111', 'Nov 11', '1', '1'),
                ('2', '2', '00211', 'Dec 11', '1', '1'),
                ('2', '3', '00311', 'Jan 12', '1', '1'),
                ('2', '4', '00411', 'Feb 12', '1', '1'),
                ('2', '5', '00511', 'Mar 12', '1', '1'),
                ('2', '6', '00611', 'Apr 12', '1', '1'),
                ('2', '7', '00711', 'May 12', '1', '1'),
                ('2', '8', '00811', 'Jun 12', '1', '1'),
                ('2', '9', '00911', 'Jul 12', '1', '1'),
                ('2', '10', '01011', 'Aug 12', '1', '1'),
                ('2', '11', '01121', 'Sep 12', '1', '1'),
                ('2', '11', '01111', 'Sep 12', '1', '1'),
                ('2', '12', '01211', 'Oct 12', '1', '1'),
                ('2', '13', '01311', 'Dec 12', '2', '1'),
                ('2', '13', '01312', 'Jan 13', '1', '2'),
                ('2', '14', '01321', 'Dec 12', '1', '1'),
                ('2', '14', '01421', 'Jan 13', '1', '1'),
                ('2', '14', '01411', 'Jan 13', '2', '1'),
                ('2', '15', '01511', 'Feb 13', '3', '1'),
                ('2', '15', '01521', 'Feb 13', '1', '1');
                """)


        INSERT INTO ComicIssue(fkey_defaultseries, comicissue_num, isbn, pubdate, quanity, edition, notes)
        VALUES ('2', '0', '00111', 'Jan 13', '1', '1'),
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

