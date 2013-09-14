# Comic Tracker
# Matt Jones caffeinatedengineering@gmail.com
# Main
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



import sys
import csv
import getopt
 
if "/home/matt/ComicTracker-PG/libs" not in sys.path:
	sys.path.append("/home/matt/ComicTracker-PG/libs")

if "/home/matt/ComicTracker-PG/comic_inserts" not in sys.path:
	sys.path.append("/home/matt/ComicTracker-PG/comic_inserts")


import ct_functions_testing as ct_funct

COMIC_FILE = ''
SERIES = 'Batman(1940)'
SERIES_ID = ''

db_con, db_cur = ct_funct.db_connection() #open a connection

COMIC_FILE = ct_funct.get_comic_file() #get the file to be read

reader = csv.DictReader(open(COMIC_FILE, 'rw'), fieldnames = ['series', 'issue', 'date', 'isbn', 'quanity'], dialect='excel-tab') #this reads a tab seperated file

comicinfo = [] # create a new list
for row in reader:
	comicinfo.append(row) #read all dict's into list one issue per line


SERIES_ID = ct_funct.get_series_id(SERIES, db_cur) #get the series id

s = {'series_id' : SERIES_ID } # create a dict entry for the series id 

for item in comicinfo:
	item.update (s) #append the series id to the list

for item in comicinfo:
	print item # print the list as a check
	db_cur.execute("INSERT INTO ComicIssue(fkey_defaultseries_id, comicissue_num, isbn, pubdate, quanity) VALUES ('%s','%s','%s','%s','%s')" % (item["series_id"], item["issue"], item["isbn"], item["date"], item["quanity"]))

db_con.commit() #commit all changes

ct_funct.close_db_connection(db_con, db_cur) #close the cursor and connection


