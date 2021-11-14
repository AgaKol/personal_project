from db.run_sql import run_sql
from models.animal import Animal
from models.owner import Owner
from models.vet import Vet
from models.treatment import Treatment
import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.treatment_repository as treatment_repository

def save(animal):
    sql = "INSERT INTO animals (name, species, dob, symptoms, treatment_id, owner_id, vet_id) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING *"
    values = [animal.name, animal.species, animal.dob, animal.symptoms, animal.treatment.id, animal.owner.id, animal.vet.id]
    result = run_sql(sql, values)
    id = result[0]['id']
    animal.id = id
    return animal

def select_all():
    animals = []
    sql = "SELECT * FROM animals"
    result = run_sql(sql)
    for row in result:
        treatment = treatment_repository.select_one(row['treatment_id'])
        owner = owner_repository.select_one(row['owner_id'])
        vet = vet_repository.select_one(row['vet_id'])
        animal = Animal(row['name'], row['species'], row['dob'], row['symptoms'], owner, treatment, vet, row['id'])
        animals.append(animal)
    return animals