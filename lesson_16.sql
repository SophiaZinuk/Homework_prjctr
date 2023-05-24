CREATE TABLE user_type(
	user_type_id int,
	user_type char,
	
	CONSTRAINT PK_user_type_user_type_id PRIMARY KEY (user_type_id)
);

CREATE TABLE users(
	user_id int, 
	user_name varchar(64) NOT NULL,
	user_surname varchar(64) NOT NULL,
	user_type_id int,
	phone_number varchar(12),
	
	CONSTRAINT PK_users_user_id PRIMARY KEY (user_id),
	CONSTRAINT FK_users_user_type FOREIGN KEY (user_type_id) REFERENCES user_type(user_type_id)
);

CREATE TABLE host_details(
	host_id int, 
	num_of_apartments smallint NOT NULL,
	user_id int,
	phone_number varchar(12),
	
	CONSTRAINT PK_host_details_host_id PRIMARY KEY (host_id),
	CONSTRAINT FK_host_details_users FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE guest_details(
	guest_id int,
	user_id int,
	phone_number varchar(12),
	entry_date date,
	departure_date date,
	
	CONSTRAINT PK_guest_details_guest_id PRIMARY KEY (guest_id),
	CONSTRAINT FK_guest_details_users FOREIGN KEY (user_id) REFERENCES users(user_id)
);

CREATE TABLE apartment_status(
	status_id int,
	status char, /* f - free, o - occupy */ 
	
	CONSTRAINT PK_apartment_status_status_id PRIMARY KEY (status_id),
);



CREATE TABLE apartment_types(
	apartment_type_id int,
	apartment_type varchar(16),
	
	CONSTRAINT PR_apartment_types_apartment_type_id PRIMARY KEY (apartment_type_id)
);

CREATE TABLE apartment(
	apartment_id int,
	host_id int,
	status_id int,
	guest_id int,
	apartment_type_id int, 
	apartment_city varchar(64),
	apartment_adress text,
	price_for_night decimal,
	
	CONSTRAINT PK_apartment_apartment_id PRIMARY KEY (apartment_id),
	CONSTRAINT FK_apartment_host_details FOREIGN KEY (host_id) REFERENCES host_details (host_id),
	CONSTRAINT FK_apartment_apartment_status FOREIGN KEY (status_id) REFERENCES apartment_status(status_id),
	CONSTRAINT FK_apartment_guest_details FOREIGN KEY (guest_id) REFERENCES guest_details(guest_id),
	CONSTRAINT FK_apartment_apartment_types FOREIGN KEY (apartment_type_id) REFERENCES apartment_types(apartment_type_id)
);

CREATE TABLE apartment_details (
	apartment_id int,
	residents_number smallint,
	num_of_rooms smallint,
	bath bool DEFAULT FALSE,
	refrigerator bool DEFAULT FALSE,
	conditionung bool DEFAULT FALSE,
	kitchen bool DEFAULT FALSE,
	washmachine bool DEFAULT FALSE,
	clean_service bool DEFAULT FALSE,
	pets bool DEFAULT FALSE,
	
	CONSTRAINT FK_apartment_details_apartment FOREIGN KEY (apartment_id) REFERENCES apartment (apartment_id)
);

INSERT INTO user_type
VALUES
(1, 'g'),
(2, 'h')

INSERT INTO users
VALUES
(1, 'Ann', 'Smith', 1, '123456789'),
(2, 'John', 'Williams', 1, '376566790'),
(3, 'Bob', 'Brown', 2, '123463167'),
(4, 'Liam', 'Davis', 2, '123456789'),
(5, 'Oliver', 'Miller', 2, '376566790'),
(6, 'Isabella', 'Wilson', 1, '123463167')

INSERT INTO host_details
VALUES
(1, 4, 3, '123463167'),
(2, 2, 4, '123456789'),
(3, 1, 5, '376566790')

INSERT INTO guest_details
VALUES 
(1, 1, '123456789', '2022-03-4', '2022-04-1'),
(2, 2, '376566790', '2022-03-4', '2022-04-1'),
(3, 6, '123463167', '2022-09-8', '2022-09-20' )


INSERT INTO apartment_types
VALUES
(1, 'Studio'),
(2, 'Alcove studio'),
(3, 'Convertible studio'),
(4, 'Micro apartment'),
(5, 'Loft'),
(6, 'Duplex'),
(7, 'Triplex'),
(8, 'Co-op'),
(9, 'Garder apartment'),
(10, 'High-rise'),
(11, 'Mid-rise'),
(12, 'Low-rise'),
(13, 'Walk-up'),
(14, 'Railroad apartmnent'),
(15, 'Other')

INSERT INTO apartment
VALUES
(1, 1, 2, 1, 1, 'London', 'address1', 299, 'Great Britain'),
(2, 1, 1, NULL, 13, 'New-York', 'address2', 500, 'US'),
(3, 1, 2, 2, 10, 'Oslo', 'address3', 799, 'Norway'),
(4, 1, 1, NULL, 6, 'Kyiv', 'address4', 2000, 'Ukraine'),
(5, 2, 1, NULL, 4, 'Istanbul', 'address5', 1560, 'Turkey'),
(6, 2, 2, 3, 9, 'Sarajevo','address6', 800, 'Bosnia and Herzegovina'),
(7, 3, 1, NULL, 2, 'Dresden', 'address7', 3400, 'Germany')

SELECT *
FROM apartment_details

INSERT INTO apartment_details
VALUES 
(1, 2, 3, TRUE, TRUE),
(2, 5, 5, TRUE, TRUE),
(3, 3, 5, TRUE, TRUE),
(4, 5, 5, TRUE, TRUE),
(5, 5, 2, TRUE, TRUE),
(6, 5, 5, TRUE, TRUE),
(7, 1, 5, TRUE, TRUE)

INSERT INTO users
VALUES 
(7, 'name1', 'surname1', 1, NULL),
(8, 'name2', 'surname2', 2, NULL),
(9, 'name3', 'surname3', 2, NULL)


INSERT INTO host_details
VALUES
(4, 2, 8, NULL),
(5, 3, 9, NULL)

INSERT INTO guest_details
VALUES
(4, 7, NULL, '2022-12-01', '2023-01-02')

INSERT INTO apartment
VALUES
(8, 4, 2, 4, 1, 'ABRA', 'address000', 40, 'OLOLO'),
(9, 4, 2, 4, 4, 'dfgA', 'addfgess000', 900, 'OrfhOLO'),
(10, 5, 2, 4, 7, 'AdfgA', 'adsdf000', 4000, 'OLbO')

/* Find a user who had biggest amount of reservation. Return user name and user_id */

SELECT user_id, user_name 
FROM users
JOIN guest_details USING (user_id)
JOIN (
	SELECT guest_id, COUNT(apartment_id) AS number_of_reservation
	FROM apartment
	JOIN guest_details USING (guest_id)
	JOIN users USING (user_id)
	WHERE guest_id IS NOT NULL
	GROUP BY guest_id
	ORDER BY number_of_reservation DESC
	LIMIT 1) AS table_ USING (guest_id)
	
/* Find a host who earned biggest amount of money */	

SELECT user_name, user_surname
FROM users
JOIN (
SELECT user_id, SUM(price_for_night) as sum_
FROM apartment
JOIN host_details USING (host_id)
JOIN users USING (user_id)
GROUP BY user_id
ORDER BY sum_ DESC
LIMIT 1) AS table_1 USING (user_id)

