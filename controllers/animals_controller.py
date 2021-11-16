import re
from flask import Flask, render_template, redirect, request, Blueprint
from controllers.vets_controller import vets
from models.animal import Animal
from repositories import animal_repository, owner_repository, vet_repository, treatment_repository
from models.owner import Owner

animals_blueprint = Blueprint("animals", __name__)

@animals_blueprint.route('/pets')
def animals():
    animals = animal_repository.select_all()
    print(animals)
    return render_template("/pets/index.html", animals = animals)

@animals_blueprint.route('/pets/<id>', methods = ["GET"])
def show_animal(id):
    animal = animal_repository.select_one(id)
    return render_template("pets/show.html", animal = animal)

@animals_blueprint.route("/pets/<id>/delete", methods = ["POST"])
def delete_animal(id):
    animal_repository.delete_one(id)
    return redirect("/pets")

@animals_blueprint.route("/pets/<id>/edit", methods = ["GET"])
def edit_animal(id):
    animal = animal_repository.select_one(id)
    vets = vet_repository.select_all()
    owners = owner_repository.select_all()
    treatments = treatment_repository.select_all()
    return render_template("pets/edit.html", animal = animal, vets = vets, owners = owners, treatments = treatments)

@animals_blueprint.route("/pets/<id>", methods = ["POST"])
def update_animal(id):
    name = request.form["name"]
    species = request.form["species"]
    dob = request.form["dob"]
    symptoms = request.form["symptoms"]
    treatment_id = request.form["treatment_id"]
    treatment = treatment_repository.select_one(treatment_id)
    vet_id = request.form["vet_id"]
    vet = vet_repository.select_one(vet_id)
    owner_id = request.form["owner_id"]
    owner = owner_repository.select_one(owner_id)
    animal = Animal(name,species,dob,symptoms, owner, treatment, vet)
    return redirect("/pets")

@animals_blueprint.route("/pets/new", methods = ["GET"])
def new_animal():
    treatments = treatment_repository.select_all()
    vets = vet_repository.select_all()
    return render_template("/pets/new.html", treatments = treatments, vets = vets)

@animals_blueprint.route("/pets", methods = ["POST"])  
def create_animal():
    name = request.form["name"]
    species = request.form["species"]
    dob = request.form["dob"]
    symptoms = request.form["symptoms"]
    owner_name = request.form["owner_name"]
    owner_address = request.form["owner_address"]
    owner_phone = request.form["owner_phone"]
    owner_email = request.form["owner_email"]
    new_owner = Owner(owner_name,owner_address,owner_phone,owner_email)
    owner_repository.save(new_owner)
    treatment_id = request.form["treatment_id"]
    treatment = treatment_repository.select_one(treatment_id)
    vet_id = request.form["vet_id"]
    vet = vet_repository.select_one(vet_id)
    animal = Animal(name, species, dob, symptoms, new_owner, treatment, vet)
    animal_repository.save(animal)
    return redirect("/pets")