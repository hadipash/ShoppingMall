-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS client;

CREATE TABLE client (
  id        UNSIGNED INTEGER PRIMARY KEY AUTOINCREMENT,
  email     VARCHAR(50) UNIQUE NOT NULL,
  name      VARCHAR(50) NOT NULL,
  password  VARCHAR(100) NOT NULL,
  phone     UNSIGNED INTEGER UNIQUE NOT NULL,
  address   VARCHAR(100),
  mileage   UNSIGNED INTEGER
);
