import psycopg2

#---------------------------------------#
# LIST_OF_TITLES			#
#					#
# a dictionary list of comics to be 	#
# added 				#
#					#
#					#
#---------------------------------------#

STORY_ARC = 'Death Of The Family'

LIST_OF_TITLES = {
                "Batman(1940)": 
                        {"comicissue_num":0, 
                        "isbn": "00011", 
                        "pubdate": "Feb09", 
                        "quantity": 1},
                "Batman(2011)":
                        {"comicissue_num":0, 
                        "isbn": "00011", 
                        "pubdate": "May12", 
                        "quantity": 1}
                }

#---------------------------------------#
# db_connection                         #
#                                       #
# takes: nothing	                #
# returns: variables for the cursor and #
#          the connection               #
#                                       #
#---------------------------------------#

def db_connection():
	db_con = psycopg2.connect("dbname=comics user='matt'")
	db_cur = db_con.cursor()
	return db_con, db_cur

#---------------------------------------#
# get_storyarc_id                       #
#                                       #
# takes: a single title                 #
# returns: the pk of the storyarc       #
#                                       #
#                                       #
#---------------------------------------#

def get_storyarc_id(STORY_ARC):
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

def get_series_id(series_title):
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

def insert_ComicIssue(series_id, comicinfo):
        # series_id is an int primary key into DefaultSeries
        # {"comicissue_num":0, 
        #  "isbn": "00011", 
        #  "pubdate": "Nov12", 
        #  "quantity": 1}

        # TODO investigate parameterized queries
        db_cur.execute("INSERT INTO ComicIssue(fkey_defaultseries_id, comicissue_num, isbn, pubdate, quanity) VALUES ('%s','%s','%s','%s','%s')" % (series_id, comicinfo["comicissue_num"], comicinfo["isbn"], comicinfo["pubdate"], comicinfo["quantity"]))
        # TODO check return code of execute to make sure it worked and handle appropriately


db_con, db_cur = db_connection() #open a connection

storyarc_id = get_storyarc_id(STORY_ARC)
#print storyarc_id


for title in LIST_OF_TITLES.iterkeys():       

        series_id = get_series_id(title)

        comicinfo = LIST_OF_TITLES[title]

        insert_ComicIssue(series_id, comicinfo)


db_con.commit()

db_cur.close()
db_con.close()

