-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS client;
DROP TABLE IF EXISTS delivery;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS my_list;


CREATE TABLE client (
  id                  UNSIGNED INTEGER PRIMARY KEY AUTOINCREMENT,
  email               VARCHAR(50) UNIQUE NOT NULL,
  name                VARCHAR(50) NOT NULL,
  password            VARCHAR(100) NOT NULL,
  phone               UNSIGNED INTEGER UNIQUE NOT NULL,
  address             VARCHAR(100),
  mileage             UNSIGNED INTEGER
);

CREATE TABLE delivery (
  track_number        UNSIGNED INTEGER PRIMARY KEY AUTOINCREMENT,
  order_id            UNSIGNED INTEGER UNIQUE NOT NULL,
  delivery_company    VARCHAR(50) NOT NULL,
  location            VARCHAR(100) NOT NULL,
  status              INTEGER NOT NULL,
  date_arrived        TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product (
  product_id          UNSIGNED INTEGER PRIMARY KEY AUTOINCREMENT,
  name                VARCHAR(50) UNIQUE NOT NULL,
  category            VARCHAR(10) NOT NULL,
  price               FLOAT NOT NULL,
  stock               INTEGER NOT NULL ,
  dc_rate             INTEGER DEFAULT '0' NOT NULL,
  sales_num           INTEGER DEFAULT '0' NOT NULL
);


-- Relational tables
CREATE TABLE my_list(
  user_id             UNSIGNED INTEGER REFERENCES client(id),
  product_id          UNSIGNED INTEGER REFERENCES product(product_id),
  PRIMARY KEY(user_id, product_id)
);

CREATE TABLE cart_list(
  user_id             UNSIGNED INTEGER REFERENCES client(id),
  product_id          UNSIGNED INTEGER REFERENCES product(product_id),
  quantity            UNSIGNED INTEGER NOT NULL,
  PRIMARY KEY(user_id, product_id)
);

CREATE TABLE coupon_list(
  user_id             UNSIGNED INTEGER REFERENCES client(id),
  coupon_id           UNSIGNED INTEGER REFERENCES coupon(coupon_id),
  quantity            UNSIGNED INTEGER NOT NULL,
  PRIMARY KEY(user_id, coupon_id)
);


-- Insert entities into the tables
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Maegan.Keith@gmail.com",     "Maegan Keith",     "12345", 01011111111, "Gwangju",  0)
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Reynold.Delroy@gmail.com",   "Reynold Delroy",   "54321", 01022222222, "Busan",    325)
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Agnes.Maurice@gmail.com",    "Agnes Maurice",    "11111", 01033333333, "Seoul",    547)
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Josh.Asher@gmail.com",       "Josh Asher",       "22222", 01044444444, "Gwangju",  0)
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Kallie.Ainsley@gmail.com",   "Kallie Ainsley",   "33333", 01055555555, "Seoul",    324)
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Alphonso.Konnor@gmail.com",  "Alphonso Konnor",  "44444", 01066666666, "Busan",    2345)
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Cheri.Arianna@gmail.com",    "Cheri Arianna",    "55555", 01077777777, "Seoul",    0)
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Saxon.Barret@gmail.com",     "Saxon Barret",     "66666", 01088888888, "Gwangju",  4574)
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Flossie.Jeannine@gmail.com", "Flossie Jeannine", "77777", 01000000000, "Seoul",    0)
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Austin.Dustin@gmail.com",    "Austin Dustin",    "99999", 01099999999, "Busan",    734)

INSERT INTO delivery (order_id, delivery_company, location, status) VALUES (1,   "LOGEN",   "Busan", 1)
INSERT INTO delivery (order_id, delivery_company, location, status) VALUES (2, "HYUNDAI",   "Seoul", 0)
INSERT INTO delivery (order_id, delivery_company, location, status) VALUES (3,   "LOGEN", "Gwangju", 1)
INSERT INTO delivery (order_id, delivery_company, location, status) VALUES (4,  "HANJIN",   "Seoul", 0)
INSERT INTO delivery (order_id, delivery_company, location, status) VALUES (5,  "HANJIN",   "Busan", 1)
