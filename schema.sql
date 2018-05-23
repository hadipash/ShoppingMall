-- Initialize the database.
-- Drop any existing data and create empty tables.

DROP TABLE IF EXISTS client;
DROP TABLE IF EXISTS my_list;
DROP TABLE IF EXISTS delivery;
DROP TABLE IF EXISTS product;
DROP TABLE IF EXISTS coupon;
DROP TABLE IF EXISTS productNum;

CREATE TABLE client (
  id                  UNSIGNED INTEGER PRIMARY KEY AUTOINCREMENT,
  email               VARCHAR(50) UNIQUE NOT NULL,
  name                VARCHAR(50) NOT NULL,
  password            VARCHAR(100) NOT NULL,
  phone               UNSIGNED INTEGER UNIQUE NOT NULL,
  address             VARCHAR(100),
  mileage             UNSIGNED INTEGER
);

CREATE TABLE my_list(
  user_id             UNSIGNED INTEGER REFERENCE client(id),
  product_id          UNSIGNED INTEGER REFERENCE product(product_id)
  PRIMARY KEY(user_id, product_id)
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


create table coupon (
  coupon_id           UNSIGNED integer primary key autoincrement,
  name                VARCHAR(50) not null,
  rate_of_discount    double not null,

);

create table coupon_product_list (
  coupon_id           UNSIGNED INTEGER REFERENCE coupon(coupon_id),
  product_id          UNSIGNED INTEGER REFERENCE product(product_id)
  PRIMARY KEY(user_id, product_id)
);

INSERT INTO delivery (order_id, delivery_company, location, status) VALUES (1,   "LOGEN",   "Busan", 1)
INSERT INTO delivery (order_id, delivery_company, location, status) VALUES (2, "HYUNDAI",   "Seoul", 0)
INSERT INTO delivery (order_id, delivery_company, location, status) VALUES (3,   "LOGEN", "Gwangju", 1)
INSERT INTO delivery (order_id, delivery_company, location, status) VALUES (4,  "HANJIN",   "Seoul", 0)
INSERT INTO Delivery (order_id, delivery_company, location, status) VALUES (5,  "HANJIN",   "BUSAN", 1)

INSERT INTO coupon (coupon_id, name, rate_of_discount) VALUES (1,   "10%할인",   "10.0")
INSERT INTO coupon (coupon_id, name, rate_of_discount) VALUES (2,   "20%할인",   "20.0")
INSERT INTO coupon (coupon_id, name, rate_of_discount) VALUES (3,   "5%할인",   "5.0")

