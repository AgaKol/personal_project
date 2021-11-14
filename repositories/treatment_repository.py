from db.run_sql import run_sql
from models.treatment import Treatment

def save(treatment):
    sql = "INSERT INTO treatments (advice, meds, price) VALUES (%s, %s, %s) RETURNING *"
    values = [treatment.advice, treatment.meds, treatment.price]
    result = run_sql(sql, values)
    id = result[0]['id']
    treatment.id = id
    return treatment