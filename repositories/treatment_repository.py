from db.run_sql import run_sql
from models.treatment import Treatment

def save(treatment):
    sql = "INSERT INTO treatments (advice, meds, price) VALUES (%s, %s, %s) RETURNING *"
    values = [treatment.advice, treatment.meds, treatment.price]
    result = run_sql(sql, values)
    id = result[0]['id']
    treatment.id = id
    return treatment

def select_all():
    treatments = []
    sql = "SELECT * FROM treatments"
    result = run_sql(sql)
    for row in result:
        treatment = Treatment(row['advice'], row['meds'], row['price'], row['id'])
        treatments.append(treatment)
    return treatments

def select_one(id):
    treatment = None
    sql = "SELECT * FROM treatments WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)
    if result is not None:
        treatment = Treatment(result['advice'], result['meds'], result['price'], result['id'])
    return treatment

def delete_all():
    sql = "DELETE FROM treatments"
    run_sql(sql)

def delete_one(id):
    sql = "DELETE FROM treatments WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(treatment):
    sql = "UPDATE treatments SET (advice, meds, price) = (%s, %s, %s) WHERE id = %s"
    values = [treatment.advice, treatment.meds, treatment.price, treatment.id]
    run_sql(sql, values)