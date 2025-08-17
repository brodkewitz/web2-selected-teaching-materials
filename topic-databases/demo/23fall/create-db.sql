-- Create the database using:
-- $ sqlite3 spotify-data.db < [this-script]
-- Purge the database to start fresh using:
-- $ sqlite3 spotify-data.db < 'DELETE FROM songs;'
-- Or just delete the database file =)

-- Import syntax (used below):
-- $ sqlite> .import data.csv songs --csv --skip 1;


DROP TABLE IF EXISTS songs;

-- Note you can skip the ID col bc sqlite automatically creates a `rowid` col
CREATE TABLE IF NOT EXISTS songs(
	`username` TEXT,
	`track_uri` TEXT,
	`track_name` TEXT,
	`artist_uris` TEXT,
	`artist_names` TEXT,
	`album_uri` TEXT,
	`album_name` TEXT,
	`album_artist_uris` TEXT,
	`album_artist_names` TEXT,
	`album_release_date` DATE,
	`album_image_url` TEXT,
	`disc_number` INTEGER,
	`track_number` INTEGER,
	`track_duration_ms` INTEGER,
	`track_preview_url` TEXT,
	`explicit` NUMERIC,
	`popularity` INTEGER,
	`isrc` TEXT,
	`added_by` TEXT,
	`added_at` TEXT,
	`artist_genres` TEXT,
	`danceability` REAL,
	`energy` REAL,
	`key` INTEGER,
	`loudness` REAL,
	`mode` INTEGER,
	`speechiness` REAL,
	`acousticness` REAL,
	`instrumentalness` REAL,
	`liveness` REAL,
	`valence` REAL,
	`tempo` REAL,
	`time_signature` INTEGER,
	`album_genres` TEXT,
	`label` TEXT,
	`copyrights` TEXT
);

-- .mode table
-- .headers on

.mode csv

.import --skip 1 csv-import-data/231130-brandon-liked.csv songs
.import --skip 1 csv-import-data/angel-classic_rap.csv songs
.import --skip 1 csv-import-data/emily-liked.csv songs
.import --skip 1 csv-import-data/emma-playlist.csv songs
.import --skip 1 csv-import-data/kael-liked.csv songs
.import --skip 1 csv-import-data/matt-liked.csv songs
.import --skip 1 csv-import-data/nikolas-liked.csv songs
