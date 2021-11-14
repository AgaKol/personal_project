DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    address VARCHAR(255),
    phone_number VARCHAR(255),
    email VARCHAR(255),
    registered BOOLEAN
);

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    address VARCHAR(255),
    phone_number VARCHAR(255),
    email VARCHAR(255),
    speciality VARCHAR(255)
);