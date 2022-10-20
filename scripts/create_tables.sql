drop table comic;
drop table chars;

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


.mode csv
.import data/raw_csv/twk_chars.csv chars
.import data/raw_csv/twk_data.csv comic



