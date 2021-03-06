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

def select_one(id):
    animal = None
    sql = "SELECT * FROM animals WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        treatment = treatment_repository.select_one(result['treatment_id'])
        owner = owner_repository.select_one(result['owner_id'])
        vet = vet_repository.select_one(result['vet_id'])
        animal = Animal(result['name'], result['species'], result['dob'], result['symptoms'], owner, treatment, vet, result['id'])
    return animal

def delete_all():
    sql = "DELETE FROM animals"
    run_sql(sql)

def delete_one(id):
    sql = "DELETE FROM animals WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(animal):
    sql = "UPDATE animals SET (name, species, dob, symptoms, treatment_id, owner_id, vet_id) = (%s, %s, %s, %s, %s, %s, %s) WHERE id = %s"
    values = [animal.name, animal.species, animal.dob, animal.symptoms, animal.treatment.id, animal.owner.id, animal.vet.id, animal.id]
    run_sql(sql, values)