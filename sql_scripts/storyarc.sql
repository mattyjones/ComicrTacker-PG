BEGIN;

INSERT INTO DefaultStoryArc(defaultstoryarc)
Values ('Death Of The Family'),
		('Throne Of Atlantis'),
		('Night Of The Owls');

COMMIT;

BEGIN;

INSERT INTO StoryArc(fkey_storyarc_id, readingorder, fkey_defaultseries_id, storyarc_issue_num)
VALUES ('1', '1', '1','700'),
	('1','2', '1','701'),
	('1','3', '5','25'),
	('1','4', '5','26');

COMMIT;
