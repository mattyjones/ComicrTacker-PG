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

STORY_ARC = 'Death Of The Family'
COMIC_FILE = 'comic_inserts/batman_test.txt'

LIST_OF_TITLES = {
                "Batman(1940)": 
                        {"comicissue_num":0, 
                        "isbn": "00011", 
                        "pubdate": "Feb76", 
                        "quantity": 1},
                "Batman(2011)":
                        {"comicissue_num":0, 
                        "isbn": "00011", 
                        "pubdate": "May12", 
                        "quantity": 1}
                }


db_con, db_cur = ct_funct.db_connection() #open a connection

storyarc_id = ct_funct.get_storyarc_id(STORY_ARC, db_cur)
#print storyarc_id


for title in LIST_OF_TITLES.iterkeys():       

        series_id = ct_funct.get_series_id(title, db_cur)

        comicinfo = LIST_OF_TITLES[title]

        ct_funct.insert_ComicIssue(series_id, comicinfo, db_cur)


#f = open(COMIC_FILE, 'rt')
#try:
#	reader = csv.DictReader(
#	for row in reader:
#		print row
#finally:
#	f.close()

#with open(COMIC_FILE) as file_object:
#	matt = list(csv.DictReader(file_object))
#print matt

reader = csv.DictReader(open(COMIC_FILE, 'r'), fieldnames = ['issue', 'isbn', 'key', 'date', 'quanity', 'edition'], dialect='excel-tab')
for row in reader:
	print row
 


db_con.commit()

ct_funct.close_db_connection(db_con, db_cur)


