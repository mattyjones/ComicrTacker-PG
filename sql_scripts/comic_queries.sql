s will return all the newstand issues of a particular series
--format ""SERIES TITLE    ISSUE NUMBER    ISBN NUMBER    QUANITY""
SELECT defaultseries.defaultseries, comicissue.comicissue_num, comicissue.isbn, comicissue.quanity
FROM defaultseries, comicissue
WHERE isbn like '__' 
	and fkey_defaultseries_id ='1'
	and defaultseries.defaultseries_id = comicissue.fkey_defaultseries_id

--this will list all the comics in the database
--format ""SERIES TITLE    ISSUE NUMBER    PUBLICATION DATE    QUANITY""
SELECT defaultseries.defaultseries, comicissue.comicissue_num, comicissue.pubdate, comicissue.quanity
FROM defaultseries, comicissue
WHERE defaultseries.defaultseries_id = comicissue.fkey_defaultseries_id

--this will list all the comics of a particular title
--format ""SERIES TITLE    ISSUE NUMBER    PUBLICATION DATE    QUANITY""
SELECT defaultseries.defaultseries, comicissue.comicissue_num, comicissue.pubdate, comicissue.quanity
FROM defaultseries, comicissue
WHERE defaultseries = 'Batman(1940)'
	and defaultseries.defaultseries_id = comicissue.fkey_defaultseries_id

--this will list all comics with a quanity greater then 1
--format ""SERIES TITLE    ISSUE NUMBER    PUBLICATION DATE    QUANITY""
SELECT defaultseries.defaultseries, comicissue.comicissue_num, comicissue.pubdate, comicissue.quanity
FROM defaultseries, comicissue
WHERE defaultseries.defaultseries_id = comicissue.fkey_defaultseries_id and quanity > '1'

--this will list all variants
--format ""SERIES TITLE    ISSUE NUMBER    PUBLICATION DATE    QUANITY""
SELECT defaultseries.defaultseries, comicissue.comicissue_num, comicissue.pubdate, comicissue.quanity
FROM defaultseries, comicissue
WHERE defaultseries.defaultseries_id = comicissue.fkey_defaultseries_id 
	and ( isbn like '___2_'
			or isbn like '___3_'
			or isbn like '___4_'
		)

--this will list all comics with an edition greater then 1
SELECT defaultseries.defaultseries, comicissue.comicissue_num, comicissue.pubdate, comicissue.quanity
FROM defaultseries, comicissue
WHERE defaultseries.defaultseries_id = comicissue.fkey_defaultseries_id 
	and ( isbn like '____2' 
			or isbn like '____3'
		)
