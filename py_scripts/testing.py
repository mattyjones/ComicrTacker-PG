# Comic Tracker
# Main
# Matt Jones urlugal@gmail.com
# Created 01.24.13
# Last Update 01.24.13
#
# Notes:
# This is the main file and will be executed from the top down.  It will import functions from
# ctfunctions.py for all necessary functionality.  All data will be stored in external files to
# be imported when necessary.
# The lastest versions can be found at https://git.caffeinatedengineering.com:ComicTracker-PG
#
# TODO:
# * add error checking
# 
# 
# 
#-----ERROR CODES-----
#
#
#
#


#the last thing I was trying to do was to get the series out from the list and then run it and return the id to insert into the statement.
#I should look at prepared statements and also creating a class for comic issues.



import sys
import csv
 
if "/home/matt/ComicTracker-PG/libs" not in sys.path:
	sys.path.append("/home/matt/ComicTracker-PG/libs")

import ct_functions as ct_funct

#---------------------------------------#
# LIST_OF_TITLES			#
#					#
# a dictionary list of comics to be 	#
# added 				#
#					#
#					#
#---------------------------------------#

COMIC_FILE = 'comic_inserts/detective_comics_1937.txt'


db_con, db_cur = ct_funct.db_connection() #open a connection

reader = csv.DictReader(open(COMIC_FILE, 'rw'), fieldnames = ['series', 'issue', 'date', 'isbn', 'quanity'], dialect='excel-tab') #this reads a tab seperated file

comicinfo = [] # create a new list
for row in reader:
	comicinfo.append(row) #read all dict's into list one issue per line

##print comicinfo

s = {'series_id' : '7'} # get the correct series id 

for item in comicinfo:
	item.update (s) #append the series id to the list

for item in comicinfo:
	print item # print the list as a check
#	SQL = "INSERT INTO ComicIssue(fkey_defaultseries_id, comicissue_num, isbn, pubdate, quanity, edition) VALUES ('%s','%s','%s','%s','%s','%s');"
#	DATA = "(item[\"series_id\"], item[\"issue\"], item[\"isbn\"], item[\"date\"], item[\"quanity\"], item[\"edition\"])" 
#	db_cur.execute(SQL, DATA)
#	db_cur.execute("INSERT INTO ComicIssue(fkey_defaultseries_id, comicissue_num, isbn, pubdate, quanity) VALUES (%(series_id)s, %(issue)s, %(isbn)s, %(date)s, %(quanity)s);" { item["series_id"], item["issue"], item["isbn"], item["date"], item["quanity"]})
        # TODO check return code of execute to make sure it worked and handle appropriately



	#db_cur.execute(command)
#for item in comicinfo: #insert the records into the table
	db_cur.execute("INSERT INTO ComicIssue(fkey_defaultseries_id, comicissue_num, isbn, pubdate, quanity) VALUES ('%s','%s','%s','%s','%s')" % (item["series_id"], item["issue"], item["isbn"], item["date"], item["quanity"]))
        # TODO check return code of execute to make sure it worked and handle appropriately


db_con.commit() #commit all changes

ct_funct.close_db_connection(db_con, db_cur) #close the cursor and connection


