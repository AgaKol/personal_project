from db.run_sql import run_sql
from models.owner import Owner

def save(owner):
    sql = "INSERT INTO owners(name, address, phone, email, registered) VALUES (%s, %s, %s, %s, %s) RETURNING *"
    values = [owner.name, owner.address, owner.phone, owner.email, owner.registered]
    result = run_sql(sql, values)
    id = result[0]['id']
    owner.id = id
    return owner

def select_all():
    owners = []
    sql = "SELECT * FROM owners"
    result = run_sql(sql)
    for row in result:
        owner = Owner(row['name'], row['address'], row['phone'], row['email'], row['registered'], row['id'])
        owners.append(owner)
    return owners

def select_one(id):
    owner = None
    sql = "SELECT * FROM owners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]
    if result is not None:
        owner = Owner(result['name'], result['address'], result['phone'], result['email'], result['registered'], result['id'])
    return owner

def delete_all():
    sql = "DELETE FROM owners"
    run_sql(sql)

def delete_one(id):
    sql = "DELETE FROM owners WHERE id = %s"
    values = [id]
    run_sql(sql, values)