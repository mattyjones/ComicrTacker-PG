# Comic Tracker
# Production Functions
# Matt Jones urlugal@gmail.com
# Created 01.24.13
# Last Update 01.24.13
#
# Notes:
#This will store all production functions used by the various scripts in Comic Tracker.
#The lastest versions can be found at https://git.caffeinatedengineering.com:ComicTracker-PG
#
# TODO:
# * add error checking
# * add support for rollling back large transactions
# * add ability to work with story titles
# * add ability to print out a status message
# * add ability to automaticly modify own StoryArc.own when a new issue is added to ComicIssue
#
#
#
#-----ERROR CODES-----
#  
#  
#  
#


import psycopg2
import sys
import getopt

#---------------------------------------#
# db_connection                         #
#                                       #
# takes: nothing	                #
# returns: variables for the cursor and #
#          the connection               #
#                                       #
#---------------------------------------#

def db_connection():
	db_con = psycopg2.connect("dbname=comics_test user='matt'")
	db_cur = db_con.cursor()
	return db_con, db_cur

#---------------------------------------#
# get_comic_file                        #
#                                       #
# takes: nothing	                #
# returns: the file name/location to be #
#		   entered		#
#                                       #
#---------------------------------------#

def get_comic_file():
	opts, arg = getopt.getopt(sys.argv[1:],  'hi:')
	for opt, arg in opts:
		if opt in ('-h'):
     			print 'comic_prod.py -i <inputfile>'
     			sys.exit()
  		elif opt in ("-i"):
     			COMIC_FILE = arg
			return COMIC_FILE


#---------------------------------------#
# get_storyarc_id                       #
#                                       #
# takes: a single title                 #
# returns: the pk of the storyarc       #
#                                       #
#                                       #
#---------------------------------------#

def get_storyarc_id(STORY_ARC, db_cur):
        db_cur.execute("Select defaultstoryarc_id FROM DefaultStoryArc Where DefaultStoryArc.defaultstoryarc = '%s';" % (STORY_ARC))
        storyarc_id = db_cur.fetchone()
        return storyarc_id[0]


#---------------------------------------#
# get_series_id                         #
#                                       #
# takes: a single title                 #
# returns: the pk of the title          #
#                                       #
#                                       #
#---------------------------------------#

def get_series_id(series_title, db_cur):
        db_cur.execute("Select defaultseries_id FROM DefaultSeries Where DefaultSeries.defaultseries = '%s';" % (series_title))
        sid = db_cur.fetchone()
        return sid[0]

#---------------------------------------#
# insert_comic_issue                    #
#                                       #
# takes: the series id and the dict     #
# returns: nothing		        #
#                                       #
#                                       #
#---------------------------------------#

def insert_ComicIssue(series_id, comicinfo, db_cur):
        # series_id is an int primary key into DefaultSeries
        # {"comicissue_num":0, 
        #  "isbn": "00011", 
        #  "pubdate": "Nov12", 
        #  "quantity": 1}

        # TODO investigate parameterized queries
	command = '''INSERT INTO ComicIssue(fkey_defaultseries_id, comicissue_num, isbn, pubdate, quanity) VALUES ('%s','%s','%s','%s','%s')" % (series_id, comicinfo["comicissue_num"], comicinfo["isbn"], comicinfo["pubdate"], comicinfo["quantity"]))'''
	db_cur.execute(command)

        # TODO investigate parameterized queries
#        db_cur.execute("INSERT INTO ComicIssue(fkey_defaultseries_id, comicissue_num, isbn, pubdate, quanity) VALUES ('%s','%s','%s','%s','%s')" % (series_id, comicinfo["comicissue_num"], comicinfo["isbn"], comicinfo["pubdate"], comicinfo["quantity"]))
        # TODO check return code of execute to make sure it worked and handle appropriately


#---------------------------------------#
# close_db_connection                   #
#                                       #
# takes: the connection and cursor token#
# returns: nothing		        #
#                                       #
#                                       #
#---------------------------------------#

def close_db_connection(db_con, db_cur):
	db_cur.close()
	db_con.close()


