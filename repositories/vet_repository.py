from db.run_sql import run_sql
from models.vet import Vet

def save(vet):
    sql = "INSERT INTO vets (name, address, phone, email, speciality) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [vet.name, vet.address, vet.phone, vet.email, vet.speciality]
    result = run_sql(sql, values)
    id = result[0]['id']
    vet.id = id
    return vet

def select_all():
    vets = []
    sql = "SELECT * FROM vets"
    result = run_sql(sql)
    for row in result:
        vet = Vet(row['name'], row['address'], row['phone'], row['email'], row['speciality'], row['id'])
        vets.append(vet)
    return vets