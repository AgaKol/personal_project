import re
from flask import Flask, render_template, redirect, request, Blueprint
from repositories import animal_repository, owner_repository, vet_repository, treatment_repository

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route('/pets')
def animals():
    animals = animal_repository.select_all()
    print(animals)
    return render_template("/pets/index.html", animals = animals)