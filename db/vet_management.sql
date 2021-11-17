DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS treatments;
DROP TABLE IF EXISTS vets;
DROP TABLE IF EXISTS owners;

CREATE TABLE owners (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    phone VARCHAR(255),
    email VARCHAR(255),
    registered BOOLEAN
);

CREATE TABLE vets (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    address VARCHAR(255),
    phone VARCHAR(255),
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
    owner_id INT REFERENCES owners(id) ON DELETE CASCADE,
    vet_id INT REFERENCES vets(id)
);

INSERT INTO owners (name, address, phone, email, registered) VALUES ('Elliot Holloway', '84 Netherpark Crescent HR6 0NY Steens Brigde', '078 3530 4803', 'e.holloway@gmail.com', true);
INSERT INTO owners (name, address, phone, email, registered) VALUES ('Toby Davidson', '112 Asfordby Road B49 1UP Alcester', '077 4398 3368', 't.davidson@gmail.com', true);
INSERT INTO owners (name, address, phone, email, registered) VALUES ('Samuel Horton', '117 Bishopthorpe Road SY20 Pennal', '077 2280 6901', 's.horton@gmail.com', false);
INSERT INTO owners (name, address, phone, email, registered) VALUES ('Bradley Carey', '87 Hertingfordbury Road SK14 5DG Lennel', '077 2608 2663', 'b.carey@gmail.com', true);
INSERT INTO owners (name, address, phone, email, registered) VALUES ('Francis Connolly', '99 Jedburgh Road TD12 4EX Olney', '078 3590 2996', 'f.connoly@gmail.com', false);

INSERT INTO vets (name, address, phone, email, speciality) VALUES ('Dr Lara Mann', '106 Buckingham Road TA10 6AG Thorney', '079 4131 6155', 'lara.mann@ccvets.com', 'Feline medicine');
INSERT INTO vets (name, address, phone, email, speciality) VALUES ('Dr Charlie Marshall', '84 Ings Lane TQ11 9TQ Dean', '070 2982 1913', 'charlie.marshall@ccvets.com', 'Canine medicine');
INSERT INTO vets (name, address, phone, email, speciality) VALUES ('Dr Billy Gill', '44 Lamphey Road DL8 0GL Theakston', '070 2092 6590', 'billy.gill@ccvets.com', 'Oncology');
INSERT INTO vets (name, address, phone, email, speciality) VALUES ('Dr Reece Cunningham', '110 Bishop Road BB7 9DW Pendleton', '070 4851 2559', 'reece.cunningham@ccvets.com', 'Cardiology');
INSERT INTO vets (name, address, phone, email, speciality) VALUES ('Dr Charlotte Addams', '50 Walwyn Road 0X12 4PD', '078 2112 9524 East Lutton', 'charlotte.addams@ccvets.com', 'Surgery');

INSERT INTO treatments (advice, meds, price) VALUES ('new puppy health check', 'none', 100);
INSERT INTO treatments (advice, meds, price) VALUES ('cat neutering', 'general anesthesia', 170);
INSERT INTO treatments (advice, meds, price) VALUES ('blood panel, urinalysis, should be kept for monitoring overnight', 'Vetsulin', 300);
INSERT INTO treatments (advice, meds, price) VALUES ('mitral valve repair intervention, should be hospitalised for one week after surgery', 'general anesthesia, protamine, blood thinners', 1500);
INSERT INTO treatments (advice, meds, price) VALUES ('biopsy', 'general anesthesia', 250);

INSERT INTO animals (name, species, dob, symptoms, treatment_id, owner_id, vet_id) VALUES ('Bitey', 'Cat', '11/07/2010', 'healthy, no symptoms', 2, 1, 1);
INSERT INTO animals (name, species, dob, symptoms, treatment_id, owner_id, vet_id) VALUES ('Wiggle', 'Dog', '15/09/2021', 'healthy, no symptoms', 1, 2, 3);
INSERT INTO animals (name, species, dob, symptoms, treatment_id, owner_id, vet_id) VALUES ('Ginger', 'Cat', '23/08/2016', 'weight loss, increased thirst', 3, 5, 2);
INSERT INTO animals (name, species, dob, symptoms, treatment_id, owner_id, vet_id) VALUES ('Leo', 'Dog', '05/04/2013', 'skin lump', 5, 3, 5);
INSERT INTO animals (name, species, dob, symptoms, treatment_id, owner_id, vet_id) VALUES ('Cocoa', 'Dog', '14/02/2018', 'coughing, heart murmurs, low energy', 4, 4, 4)