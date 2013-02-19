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


#last thing I was doing was getting the functio to use a file as an arguement to work.  If you remove the function def the code works fine


import sys
import csv
 
if "/home/matt/ComicTracker-PG/libs" not in sys.path:
	sys.path.append("/home/matt/ComicTracker-PG/libs")

if "/home/matt/ComicTracker-PG/comic_inserts" not in sys.path:
	sys.path.append("/home/matt/ComicTracker-PG/comic_inserts")


import ct_functions as ct_funct
import getopt

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

def get_comci_file(arg, OMIC_FILE):
	opts, arg = getopt.getopt(sys.argv[1:],  'hi:', ["ifile="])
	for opt, arg in opts:
		if opt in ('-h'):
     			print 'comic_prod.py -i <inputfile>'
     			sys.exit()
  		elif opt in ("-i"):
     			COMIC_FILE = arg
			print COMIC_FILE
			return COMIC_FILE

db_con, db_cur = ct_funct.db_connection() #open a connection

reader = csv.DictReader(open(COMIC_FILE, 'rw'), fieldnames = ['series', 'issue', 'date', 'isbn', 'quanity'], dialect='excel-tab') #this reads a tab seperated file

comicinfo = [] # create a new list
for row in reader:
	comicinfo.append(row) #read all dict's into list one issue per line


s = {'series_id' : '1'} # get the correct series id 

for item in comicinfo:
	item.update (s) #append the series id to the list

for item in comicinfo:
	print item # print the list as a check
#	db_cur.execute("INSERT INTO ComicIssue(fkey_defaultseries_id, comicissue_num, isbn, pubdate, quanity) VALUES ('%s','%s','%s','%s','%s')" % (item["series_id"], item["issue"], item["isbn"], item["date"], item["quanity"]))

db_con.commit() #commit all changes

ct_funct.close_db_connection(db_con, db_cur) #close the cursor and connection


