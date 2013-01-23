BEGIN;

--INSERT INTO DefaultSeries(defaultseries)
--	VALUES('Batman (1940)'), ('Batman(2011)'), ('Robin(1993)');

--INSERT INTO DefaultStoryArc(defaultstoryarc)
--	VALUES ('Batman And Son'), ('Knightfall'), ('The Crusade'), ('Knightquest');

--INSERT INTO ComicIssue (fkey_defaultseries_id, comicissue_num, isbn, pubdate, quanity, edition)
--	VALUES ('7', '12', '0012', 'Nov 11', '1', '1' ),
--		   ('7', '13', '0013', 'Dec 11', '3', '1' ),
--		   ('7', '14', '0014', 'Apr 11', '1', '2' ),
--		   ('8', '15', '0015', 'Feb 11', '5', '1' ),
--		   ('9', '16', '0016', 'Mar 11', '1', '1' ),
--		   ('9', '17', '0017', 'Sep 11', '8', '3' );

INSERT INTO StoryTitle (fkey_comicissue_id, storytitle)
	VALUES ('19', 'The Many Deaths Of Batman'),
		   ('20', 'Another Slow Death Of Batman'),
		   ('19', 'The Rebirth Of Batman'),
		   ('23', 'The New Batman'),
		   ('24', 'The New Robin'); 

COMMIT;
