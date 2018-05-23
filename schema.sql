-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS client;
DROP TABLE IF EXISTS delivery;

CREATE TABLE client (
  id        UNSIGNED INTEGER PRIMARY KEY AUTOINCREMENT,
  email     VARCHAR(50) UNIQUE NOT NULL,
  name      VARCHAR(50) NOT NULL,
  password  VARCHAR(100) NOT NULL,
  phone     UNSIGNED INTEGER UNIQUE NOT NULL,
  address   VARCHAR(100),
  mileage   UNSIGNED INTEGER
);

CREATE TABLE delivery (
    track_number        UNSIGNED INTEGER PRIMARY KEY AUTOINCREMENT,
	order_id            UNSIGNED INTEGER UNIQUE NOT NULL,
	delivery_company    VARCHAR(50) NOT NULL,
	location            VARCHAR(100) NOT NULL,
	status              INTEGER NOT NULL,
	date_arrived        TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO delivery (order_id, delivery_company, location, status) VALUES (1,   "LOGEN",   "Busan", 1)
INSERT INTO delivery (order_id, delivery_company, location, status) VALUES (2, "HYUNDAI",   "Seoul", 0)
INSERT INTO delivery (order_id, delivery_company, location, status) VALUES (3,   "LOGEN", "Gwangju", 1)
INSERT INTO delivery (order_id, delivery_company, location, status) VALUES (4,  "HANJIN",   "Seoul", 0)
INSERT INTO Delivery (order_id, delivery_company, location, status) VALUES (5,  "HANJIN",   "BUSAN", 1)