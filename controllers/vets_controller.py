import re
from flask import Flask, render_template, redirect, request, Blueprint
from repositories import vet_repository, animal_repository, owner_repository, treatment_repository
from models.vet import Vet

vet_blueprint = Blueprint("vets", __name__)

@vet_blueprint.route('/vets')
def vets():
    vets = vet_repository.select_all()
    print (vets)
    return render_template("/vets/index.html", vets = vets)