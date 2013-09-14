/*------------------------------------------------------- 
CaffeinatedEngineering
Matt Jones caffeinatedengineering@gmail.com

<Overview>
 This files holds the table structure and creation code for
 the comic book database

<Change Log>


 Copyright 2010 CaffeinatedEngineering
 
    This is free software: you can redistribute it and/or modify
	it under the terms of the Affero General Public License as published by
    Affero, either version 2 of the License, or
    (at your option) any later version.
--------------------------------------------------------*/

BEGIN;

CREATE TABLE DefaultSeries (

	defaultseries_id	serial	PRIMARY KEY,
	defaultseries		text	UNIQUE --referencial check for the series table and will store all the values
	);

CREATE TABLE DefaultStoryArc (

	defaultstoryarc_id	serial	PRIMARY KEY,
	defaultstoryarc		text	UNIQUE --referencial check for the storyarc table and will store all the values
	);

CREATE TABLE ComicIssue (

	comicissue_id		serial		PRIMARY KEY,  --unique id and will be used as a foreign key when needed
	fkey_defaultseries_id 	int		REFERENCES DefaultSeries(defaultseries_id),
	comicissue_num		int		NOT NULL,  --the title of the issue (ex. #15, #701)
	isbn			varchar(6),	-- the isbn to check for varients and non-first editions
	pubdate			text		NOT NULL,  --the cover date (ex. Jun 86, Apr 11)
	quanity			int		NOT NULL,  --how many copies are in the users collection
	boxnumber		int,		--the location of the comic
	digital_copy		boolean,	--this will show if I have digital copy of the comic 1==true 0==false
	notes			text		--various notes about the comic
	);

CREATE TABLE StoryTitle (
	
	storytitle_id		serial		PRIMARY KEY,  --unique id and will be used as a foreign key when needed
	storytitle		text		NOT NULL,  --the storytitle (ex. Fear and Denial Part 1: The Truth, Fear And Denial Part 2: The Test)
	fkey_comicissue_id	int		REFERENCES ComicIssue(comicissue_id)  --references the comicissue_id to show it is contained within
	);

CREATE TABLE StoryArc (

	storyarc_id		serial	 	PRIMARY KEY,  --unique id and will be used as a foreign key when needed
	fkey_storyarc_id1	int		REFERENCES DefaultStoryArc(defaultstoryarc_id),  --references defaultstoryarc
	fkey_storyarc_id2	int		REFERENCES DefaultStoryArc(defaultstoryarc_id),
	readingorder		int,		--the reading order of the comic issue in the story arc
	notes  			text,		--various notes about the story arc
	fkey_defaultseries_id 	int		REFERENCES DefaultSeries(defaultseries_id), --this will be the series
	storyarc_issue_num	int		--the will be the issue number
	);

CREATE TABLE WantList (
	
	wantlist_id		serial		PRIMARY KEY, --unique key to be refrenced if necessary
	fkey_defaultseries_id	int		REFERENCES DefaultSeries(defaultseries_id), --the series
	wantlist_issue_num	int,		--the issue number I want
	notes			text		--various notes about the issue		
	);

COMMIT;
