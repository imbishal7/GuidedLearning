CREATE TYPE BANNED AS ENUM ('Yes', 'No');
CREATE TYPE ROLE AS ENUM ('client', 'driver', 'partner');

CREATE TABLE IF NOT EXISTS users(
	users_id INT,
	banned BANNED,
	role ROLE,
	PRIMARY KEY (users_id)
);

CREATE TYPE STATUS as ENUM ('completed', 'cancelled_by_driver', 'cancelled_by_client');

CREATE TABLE IF NOT EXISTS trips(
	id INT,
	client_id INT,
	driver_id INT,
	city_id INT,
	status STATUS,
	request_at DATE,
	PRIMARY KEY(id),
	FOREIGN KEY(client_id)
		REFERENCES users (users_id),
	FOREIGN KEY(driver_id)
		REFERENCES users(users_id)
);