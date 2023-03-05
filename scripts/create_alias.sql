-- to run from root
-- sqlite3 backend/db/twk.db < scripts/create_tables.sql 
CREATE TABLE IF NOT EXISTS "alias"(
  "name" TEXT,
  "alias" TEXT
)

.mode csv
.import data/aliases.csv alias


