-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS client;
DROP TABLE IF EXISTS placed_order;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS coupon;
DROP TABLE IF EXISTS my_list;
DROP TABLE IF EXISTS cart_list;
DROP TABLE IF EXISTS coupon_list;
DROP TABLE IF EXISTS refund;
DROP TABLE IF EXISTS payment;
DROP TABLE IF EXISTS payment_order;
DROP TABLE IF EXISTS delivery_history;
DROP TABLE IF EXISTS client_order;
DROP TABLE IF EXISTS payment_detail;


CREATE TABLE client (
  id                  INTEGER PRIMARY KEY AUTOINCREMENT,
  email               VARCHAR(50) UNIQUE NOT NULL,
  name                VARCHAR(50) NOT NULL,
  password            VARCHAR(100) NOT NULL,
  phone               UNSIGNED INTEGER UNIQUE NOT NULL,
  address             VARCHAR(100) NOT NULL,
  mileage             UNSIGNED INTEGER DEFAULT 0
);

CREATE TABLE placed_order (
  order_id            INTEGER PRIMARY KEY AUTOINCREMENT,
  track_number        UNSIGNED INTEGER UNIQUE NOT NULL,
  delivery_company    VARCHAR(50) NOT NULL,
  last_status         INTEGER NOT NULL,
  order_date          TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE product (
  product_id          INTEGER PRIMARY KEY AUTOINCREMENT,
  name                VARCHAR(50) UNIQUE NOT NULL,
  category            VARCHAR(10) NOT NULL,
  price               FLOAT NOT NULL,
  stock               INTEGER NOT NULL ,
  dc_rate             INTEGER DEFAULT '0' NOT NULL,
  sales_num           INTEGER DEFAULT '0' NOT NULL,
  num_of_ratings      INTEGER DEFAULT '0' NOT NULL,
  product_rating      FLOAT NOT NULL,
  registration_date   TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  description         TEXT
);

CREATE TABLE coupon (
  coupon_id           INTEGER PRIMARY KEY AUTOINCREMENT,
  name                VARCHAR(50) NOT NULL,
  discount            INTEGER NOT NULL
);

CREATE TABLE payment (
  payment_id          INTEGER PRIMARY KEY AUTOINCREMENT,
  price               FLOAT NOT NULL,
  name                STRING NOT NULL,
  phone               INTEGER NOT NULL,
  address             STRING NOT NULL,
  discount_price      FLOAT NOT NULL
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
  used                INTEGER DEFAULT '0' NOT NULL,
  PRIMARY KEY(user_id, coupon_id)
);

CREATE TABLE client_order (
  client_id           INTEGER REFERENCES client(id),
  order_id            INTEGER REFERENCES placed_order(order_id),
  PRIMARY KEY(client_id, order_id)
);

CREATE TABLE payment_order (
  order_id            INTEGER REFERENCES placed_order(order_id),
  payment_id          INTEGER REFERENCES payment(payment_id),
  PRIMARY KEY(order_id, payment_id)
);

CREATE TABLE delivery_history (
  track_number        INTEGER REFERENCES placed_order(track_number),
  location            VARCHAR(20) NOT NULL,
  hub_date            TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY(track_number, location)
);

CREATE TABLE payment_detail (
  payment_id          INTEGER REFERENCES payment(payment_id),
  product_id          INTEGER REFERENCES product(product_Id),
  price               FLOAT NOT NULL,
  quantity            INTEGER NOT NULL,
  total_sum           FLOAT NOT NULL,
  PRIMARY KEY(payment_id, product_id)
);


-- Insert entities into the tables
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Maegan.Keith@gmail.com",     "Maegan Keith",     "12345", 01011111111, "Busan",  0);
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Reynold.Delroy@gmail.com",   "Reynold Delroy",   "54321", 01022222222, "Gwangju",    325);
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Agnes.Maurice@gmail.com",    "Agnes Maurice",    "11111", 01033333333, "Seoul",    547);
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Josh.Asher@gmail.com",       "Josh Asher",       "22222", 01044444444, "Gwangju",  0);
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Kallie.Ainsley@gmail.com",   "Kallie Ainsley",   "33333", 01055555555, "Seoul",    324);
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Alphonso.Konnor@gmail.com",  "Alphonso Konnor",  "44444", 01066666666, "Busan",    2345);
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Cheri.Arianna@gmail.com",    "Cheri Arianna",    "55555", 01077777777, "Seoul",    0);
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Saxon.Barret@gmail.com",     "Saxon Barret",     "66666", 01088888888, "Gwangju",  4574);
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Flossie.Jeannine@gmail.com", "Flossie Jeannine", "77777", 01000000000, "Seoul",    0);
INSERT INTO client (email, name, password, phone, address, mileage) VALUES ("Austin.Dustin@gmail.com",    "Austin Dustin",    "99999", 01099999999, "Busan",    734);

INSERT INTO coupon (coupon_id, name, discount) VALUES (1, "THANKS",  10);
INSERT INTO coupon (coupon_id, name, discount) VALUES (2, "OPEN",    20);
INSERT INTO coupon (coupon_id, name, discount) VALUES (3, "JUNEEVENT", 6);

INSERT INTO product (name, category, price, stock, dc_rate, sales_num, num_of_ratings, product_rating)
VALUES ("flower dress", "clothes", 44.95, 15, 15, 8, 1, 4.5);
INSERT INTO product (name, category, price, stock, dc_rate, sales_num, num_of_ratings, product_rating)
VALUES ("flower blouse", "clothes", 30.5, 5, 10, 2, 3, 4.2);
INSERT INTO product (name, category, price, stock, dc_rate, sales_num, num_of_ratings, product_rating)
VALUES ("blue stripe shirt", "clothes", 5.95, 20, 10, 13, 1, 5.0);
INSERT INTO product (name, category, price, stock, dc_rate, sales_num, num_of_ratings, product_rating)
VALUES ("brown coat", "clothes", 5.66, 17, 5, 5, 1, 4.5);
INSERT INTO product (name, category, price, stock, dc_rate, sales_num, num_of_ratings, product_rating)
VALUES ("avocado", "food", 10.1, 15, 30, 24, 5, 3.0);
INSERT INTO product (name, category, price, stock, dc_rate, sales_num, num_of_ratings, product_rating, description)
VALUES ("apple", "food", 4.95, 13, 13, 33, 5, 5.0, "Cheap and delicious apples from Dae-gu !!!");
INSERT INTO product (name, category, price, stock, dc_rate, sales_num, num_of_ratings, product_rating, description)
VALUES ("apple juice", "food", 4.75, 2, 5, 100, 5, 5.0, "Beverage to take care of your refreshing morning! Try apple juice.");
INSERT INTO product (name, category, price, stock, dc_rate, sales_num, num_of_ratings, product_rating, description)
VALUES ("apple pie", "food", 6.7, 10, 10, 10, 10, 3.9, "This apple pie is very delicious. If you taste this once, you will not forget this taste. Please enjoy our masterpieces made of fresh ingredients.");
INSERT INTO product (name, category, price, stock, dc_rate, sales_num, num_of_ratings, product_rating)
VALUES ("banana", "food", 11.1, 24, 0, 11, 12, 3.8);
INSERT INTO product (name, category, price, stock, dc_rate, sales_num, num_of_ratings, product_rating)
VALUES ("paradox lost", "book", 6.95, 5, 35, 26, 7, 4.0);
INSERT INTO product (name, category, price, stock, dc_rate, sales_num, num_of_ratings, product_rating)
VALUES ("visual studio guide", "book", 49.95, 2, 7, 0, 1, 3.0);
INSERT INTO product (name, category, price, stock, dc_rate, sales_num, num_of_ratings, product_rating)
VALUES ("microsoft: the programming bible", "book", 36.95, 5, 7, 19, 1, 2.0);

INSERT INTO cart_list (user_id, product_id, quantity) VALUES (1, 1, 1);
INSERT INTO cart_list (user_id, product_id, quantity) VALUES (1, 2, 1);
INSERT INTO cart_list (user_id, product_id, quantity) VALUES (1, 3, 1);
INSERT INTO cart_list (user_id, product_id, quantity) VALUES (1, 4, 1);
INSERT INTO cart_list (user_id, product_id, quantity) VALUES (1, 5, 1);
INSERT INTO cart_list (user_id, product_id, quantity) VALUES (1, 6, 1);

INSERT INTO my_list (user_id, product_id) VALUES (1, 4);
INSERT INTO my_list (user_id, product_id) VALUES (1, 5);
INSERT INTO my_list (user_id, product_id) VALUES (1, 6);
INSERT INTO my_list (user_id, product_id) VALUES (1, 7);
INSERT INTO my_list (user_id, product_id) VALUES (1, 8);
INSERT INTO my_list (user_id, product_id) VALUES (1, 9);

INSERT INTO placed_order (track_number, delivery_company, last_status, order_date) VALUES (1,   "LOGEN", 1, datetime('now','-3 day','localtime'));
INSERT INTO placed_order (track_number, delivery_company, last_status, order_date) VALUES (2, "HYUNDAI", 3, datetime('now','-6 day','localtime'));
INSERT INTO placed_order (track_number, delivery_company, last_status, order_date) VALUES (3,      "CJ", 2, datetime('now','-4 day','localtime'));

INSERT INTO payment (price, name, phone, address, discount_price) VALUES (181.38, "Maegan Keith", 01011111111, "Busan", 163.24);
INSERT INTO payment (price, name, phone, address, discount_price) VALUES (79.2, "Maegan Keith", 01011111111, "Busan", 71.28);
INSERT INTO payment (price, name, phone, address, discount_price) VALUES (179.8, "Maegan Keith", 01011111111, "Busan", 179.8);

INSERT INTO client_order (client_id, order_id) VALUES (1, 1);
INSERT INTO client_order (client_id, order_id) VALUES (1, 2);
INSERT INTO client_order (client_id, order_id) VALUES (1, 3);

INSERT INTO payment_order (order_id, payment_id) VALUES (1, 1);
INSERT INTO payment_order (order_id, payment_id) VALUES (2, 2);
INSERT INTO payment_order (order_id, payment_id) VALUES (3, 3);

INSERT INTO payment_detail (payment_id, product_id, price, quantity, total_sum) VALUES (1, 1, 44.95, 2, 89.9);
INSERT INTO payment_detail (payment_id, product_id, price, quantity, total_sum) VALUES (1, 2, 30.5, 1, 30.5);
INSERT INTO payment_detail (payment_id, product_id, price, quantity, total_sum) VALUES (1, 3, 5.95, 4, 23.8);
INSERT INTO payment_detail (payment_id, product_id, price, quantity, total_sum) VALUES (1, 4, 5.66, 3, 16.98);
INSERT INTO payment_detail (payment_id, product_id, price, quantity, total_sum) VALUES (1, 5, 10.1, 2, 20.2);

INSERT INTO payment_detail (payment_id, product_id, price, quantity, total_sum) VALUES (2, 6, 4.95, 3, 14.85);
INSERT INTO payment_detail (payment_id, product_id, price, quantity, total_sum) VALUES (2, 7, 4.75, 4, 19.0);
INSERT INTO payment_detail (payment_id, product_id, price, quantity, total_sum) VALUES (2, 8, 6.7, 2, 13.4);
INSERT INTO payment_detail (payment_id, product_id, price, quantity, total_sum) VALUES (2, 9, 11.1, 1, 11.1);
INSERT INTO payment_detail (payment_id, product_id, price, quantity, total_sum) VALUES (2, 10, 6.95, 3, 20.85);

INSERT INTO payment_detail (payment_id, product_id, price, quantity, total_sum) VALUES (3, 11, 49.95, 2, 99.9);
INSERT INTO payment_detail (payment_id, product_id, price, quantity, total_sum) VALUES (3, 12, 39.95, 2, 79.9);

INSERT INTO delivery_history (track_number, location, hub_date) VALUES (1, "Seoul", datetime('now','-2 day','localtime'));
INSERT INTO delivery_history (track_number, location, hub_date) VALUES (1, "Daegu", datetime('now','-1 day','localtime'));
INSERT INTO delivery_history (track_number, location, hub_date) VALUES (1, "Busan", datetime('now','localtime'));

INSERT INTO delivery_history (track_number, location, hub_date) VALUES (2, "Seoul", datetime('now','-5 day','localtime'));
INSERT INTO delivery_history (track_number, location, hub_date) VALUES (2, "Daegu", datetime('now','-4 day','localtime'));
INSERT INTO delivery_history (track_number, location, hub_date) VALUES (2, "Busan", datetime('now','-3 day','localtime'));

INSERT INTO delivery_history (track_number, location, hub_date) VALUES (3, "Seoul", datetime('now','-3 day','localtime'));
INSERT INTO delivery_history (track_number, location, hub_date) VALUES (3, "Daegu", datetime('now','-2 day','localtime'));
INSERT INTO delivery_history (track_number, location, hub_date) VALUES (3, "Busan", datetime('now','-1 day','localtime'));
