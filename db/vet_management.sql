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

CREATE TABLE treatments (
    id SERIAL PRIMARY KEY,
    advice TEXT,
    meds VARCHAR(255),
    price INT
);

CREATE TABLE animals (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    species VARCHAR(255),
    dob VARCHAR(255),
    symptoms TEXT,
    treatment_id INT REFERENCES treatments(id),
    owner_id INT REFERENCES owners(id),
    vet_id INT REFERENCES vets(id)
)