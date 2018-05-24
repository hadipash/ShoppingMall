-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS client;
DROP TABLE IF EXISTS delivery;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS coupon;
DROP TABLE IF EXISTS my_list;
DROP TABLE IF EXISTS cart_list;
DROP TABLE IF EXISTS coupon_list;
DROP TABLE IF EXISTS coupon_applied_product_list;
DROP TABLE IF EXISTS refund;
DROP TABLE IF EXISTS payment;


CREATE TABLE client (
  id                  INTEGER PRIMARY KEY AUTOINCREMENT,
  email               VARCHAR(50) UNIQUE NOT NULL,
  name                VARCHAR(50) NOT NULL,
  password            VARCHAR(100) NOT NULL,
  phone               UNSIGNED INTEGER UNIQUE NOT NULL,
  address             VARCHAR(100),
  mileage             UNSIGNED INTEGER
);

CREATE TABLE delivery (
  track_number        INTEGER PRIMARY KEY AUTOINCREMENT,
  order_id            UNSIGNED INTEGER UNIQUE NOT NULL,
  delivery_company    VARCHAR(50) NOT NULL,
  location            VARCHAR(100) NOT NULL,
  status              INTEGER NOT NULL,
  date_arrived        TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product (
  product_id          INTEGER PRIMARY KEY AUTOINCREMENT,
  name                VARCHAR(50) UNIQUE NOT NULL,
  category            VARCHAR(10) NOT NULL,
  price               FLOAT NOT NULL,
  stock               INTEGER NOT NULL ,
  dc_rate             INTEGER DEFAULT '0' NOT NULL,
  sales_num           INTEGER DEFAULT '0' NOT NULL
);

CREATE TABLE coupon (
  coupon_id           INTEGER PRIMARY KEY AUTOINCREMENT,
  name                VARCHAR(50) NOT NULL,
  discount            DOUBLE NOT NULL
);

create table payment (
  paymentNum        INTEGER PRIMARY KEY AUTOINCREMENT,
  price             INTEGER NOT NULL,
  shippingFee       INTEGER,
  name              STRING NOT NULL,
  phone             INTEGER NOT NULL,
  address           STRING NOT NULL,
  discount          INTEGER
);


-- Relational tables
CREATE TABLE my_list(
  user_id             INTEGER REFERENCES client(id),
  product_id          INTEGER REFERENCES product(product_id),
  PRIMARY KEY(user_id, product_id)
);

CREATE TABLE cart_list(
  user_id             INTEGER REFERENCES client(id),
  product_id          INTEGER REFERENCES product(product_id),
  quantity            UNSIGNED INTEGER NOT NULL,
  PRIMARY KEY(user_id, product_id)
);

CREATE TABLE coupon_list(
  user_id             INTEGER REFERENCES client(id),
  coupon_id           INTEGER REFERENCES coupon(coupon_id),
  PRIMARY KEY(user_id, coupon_id)
);

create table refund (
  refundNum         INTEGER PRIMARY KEY AUTOINCREMENT,
  paymentNum        INTEGER REFERENCES payment(paymentNum),
  refundAdr         STRING NOT NULL
);

CREATE TABLE product_order (
  user_id             INTEGER REFERENCES client(id),
  track_number        INTEGER REFERENCES delivery(track_number),
  PRIMARY KEY(user_id, track_number)
);


-- Insert entities into the tables
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Maegan.Keith@gmail.com",     "Maegan Keith",     "12345", 01011111111, "Gwangju",  0);
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Reynold.Delroy@gmail.com",   "Reynold Delroy",   "54321", 01022222222, "Busan",    325);
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Agnes.Maurice@gmail.com",    "Agnes Maurice",    "11111", 01033333333, "Seoul",    547);
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Josh.Asher@gmail.com",       "Josh Asher",       "22222", 01044444444, "Gwangju",  0);
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Kallie.Ainsley@gmail.com",   "Kallie Ainsley",   "33333", 01055555555, "Seoul",    324);
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Alphonso.Konnor@gmail.com",  "Alphonso Konnor",  "44444", 01066666666, "Busan",    2345);
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Cheri.Arianna@gmail.com",    "Cheri Arianna",    "55555", 01077777777, "Seoul",    0);
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Saxon.Barret@gmail.com",     "Saxon Barret",     "66666", 01088888888, "Gwangju",  4574);
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Flossie.Jeannine@gmail.com", "Flossie Jeannine", "77777", 01000000000, "Seoul",    0);
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Austin.Dustin@gmail.com",    "Austin Dustin",    "99999", 01099999999, "Busan",    734);

INSERT INTO delivery (order_id, delivery_company, location, status) VALUES (1,   "LOGEN",   "Busan", 1);
INSERT INTO delivery (order_id, delivery_company, location, status) VALUES (2, "HYUNDAI",   "Seoul", 0);
INSERT INTO delivery (order_id, delivery_company, location, status) VALUES (3,   "LOGEN", "Gwangju", 1);
INSERT INTO delivery (order_id, delivery_company, location, status) VALUES (4,  "HANJIN",   "Seoul", 0);
INSERT INTO delivery (order_id, delivery_company, location, status) VALUES (5,  "HANJIN",   "Busan", 1);

INSERT INTO coupon (coupon_id, name, discount) VALUES (1,   "10%",   "10.0");
INSERT INTO coupon (coupon_id, name, discount) VALUES (2,   "20%",   "20.0");
INSERT INTO coupon (coupon_id, name, discount) VALUES (3,    "5%",    "5.0");

INSERT INTO product (name, category, price, stock, dc_rate, sales_num) VALUES ("flower dress", "clothes", 44.95, 15, 15, 8);
INSERT INTO product (name, category, price, stock, dc_rate, sales_num) VALUES ("blue stripe shirt", "clothes", 5.95, 20, 10, 13);
INSERT INTO product (name, category, price, stock, dc_rate, sales_num) VALUES ("brown coat", "clothes", 5.66, 17, 5, 5);
INSERT INTO product (name, category, price, stock, dc_rate, sales_num) VALUES ("avocado", "food", 10.1, 15, 30, 24);
INSERT INTO product (name, category, price, stock, dc_rate, sales_num) VALUES ("apple", "food", 4.95, 13, 13, 33);
INSERT INTO product (name, category, price, stock, dc_rate, sales_num) VALUES ("crap", "food", 11.1, 24, 0, 11);
INSERT INTO product (name, category, price, stock, dc_rate, sales_num) VALUES ("paradox lost", "book", 6.95, 5, 35, 26);
INSERT INTO product (name, category, price, stock, dc_rate, sales_num) VALUES ("visual studio guide", "book", 49.95, 2, 7, 0);
INSERT INTO product (name, category, price, stock, dc_rate, sales_num) VALUES ("microsoft: the programming bible", "book", 36.95, 5, 7, 19);
