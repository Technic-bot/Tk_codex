-- to run from root
-- sqlite3 backend/db/twk.db < scripts/create_tables.sql 
drop table comic;
drop table chars;
drop table script;

CREATE TABLE IF NOT EXISTS "comic"(
  "page" INTEGER PRIMARY KEY,
  "title" TEXT,
  "date" TEXT,
  "url" TEXT,
  "transcript" TEXT
);

CREATE TABLE IF NOT EXISTS "chars"(
  "page" INTEGER ,
  "character" TEXT
);

CREATE TABLE IF NOT EXISTS "script"(
  "page" INTEGER ,
  "dialogue" TEXT,
  "speaker" TEXT
);

CREATE TABLE IF NOT EXISTS "alias"(
  "name" TEXT,
  "alias" TEXT
)

.mode csv
.import data/raw_csv/twk_chars.csv chars
.import data/raw_csv/twk_data.csv comic
.import data/raw_csv/twk_script.csv script


