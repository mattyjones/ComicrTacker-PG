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


# THIS IS A PRODUCTION SCRIPT DO NOT MODIFY!!

#need to move function to other lib file
#clean code of testing items
#figure out string processing to get the series and set the series id


import sys
import csv
import getopt
 
if "/home/matt/ComicTracker-PG/libs" not in sys.path:
	sys.path.append("/home/matt/ComicTracker-PG/libs")

if "/home/matt/ComicTracker-PG/comic_inserts" not in sys.path:
	sys.path.append("/home/matt/ComicTracker-PG/comic_inserts")


import ct_functions as ct_funct

#---------------------------------------#
# LIST_OF_TITLES			#
#					#
# a dictionary list of comics to be 	#
# added 				#
#					#
#					#
#---------------------------------------#

# COMIC_FILE = '../comic_inserts/batman_1940'
#COMIC_ISSUE = ''
COMIC_FILE = ''
SERIES = ''

db_con, db_cur = ct_funct.db_connection() #open a connection

COMIC_FILE = ct_funct.get_comic_file()

reader = csv.DictReader(open(COMIC_FILE, 'rw'), fieldnames = ['series', 'issue', 'date', 'isbn', 'quanity'], dialect='excel-tab') #this reads a tab seperated file

comicinfo = [] # create a new list
for row in reader:
	comicinfo.append(row) #read all dict's into list one issue per line


one = 'Birds Of Prey(2011)'
matt = ct_funct.get_series_id(one, db_cur)
print matt

s = {'series_id' : matt } # get the correct series id 

for item in comicinfo:
	item.update (s) #append the series id to the list

for item in comicinfo:
#	print 'hello'
	print item # print the list as a check
#	db_cur.execute("INSERT INTO ComicIssue(fkey_defaultseries_id, comicissue_num, isbn, pubdate, quanity) VALUES ('%s','%s','%s','%s','%s')" % (item["series_id"], item["issue"], item["isbn"], item["date"], item["quanity"]))

db_con.commit() #commit all changes

ct_funct.close_db_connection(db_con, db_cur) #close the cursor and connection


