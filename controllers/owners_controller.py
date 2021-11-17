import re
from flask import Flask, render_template, request, redirect, Blueprint
from repositories import owner_repository, animal_repository, vet_repository, treatment_repository
from models.owner import Owner
from models.animal import Animal

owners_blueprint = Blueprint("owners", __name__)

@owners_blueprint.route("/owners")
def owners():
    owners = owner_repository.select_all()
    print (owners)
    return render_template ("/owners/index.html", owners = owners)

@owners_blueprint.route('/owners/<id>', methods = ["GET"])
def show_owner(id):
    owner = owner_repository.select_one(id)
    animals = animal_repository.select_all()
    return render_template("owners/show.html", owner = owner, animals = animals)

@owners_blueprint.route("/owners/<id>/delete", methods = ["POST"])
def delete_owner(id):
    owner_repository.delete_one(id)
    return redirect("/owners")

@owners_blueprint.route("/owners/<id>/edit", methods = ["GET"])
def edit_owner(id):
    owner = owner_repository.select_one(id)
    return render_template("owners/edit.html", owner = owner)

@owners_blueprint.route("/owners/<id>", methods = ["POST"])
def update_owner(id):
    name = request.form["name"]
    address = request.form["address"]
    phone = request.form["phone"]
    email = request.form["email"]
    registered = request.form["registered"]
    owner = Owner(name,address,phone,email,registered,id)
    owner_repository.update(owner)
    return redirect("/owners")

@owners_blueprint.route("/owners/<id>/add_pet", methods = ["GET"])
def adding_pet(id):
    owner = owner_repository.select_one(id)
    treatments = treatment_repository.select_all()
    vets = vet_repository.select_all()
    if owner.registered == False:
        return render_template("owners/add_pet.html", owner = owner, treatments = treatments, vets = vets)
    else:
        return render_template("/pets/new.html", treatments = treatments, vets = vets)

@owners_blueprint.route("/owners/<id>/add_pet", methods = ["POST"])  
def add_pet(id):
    owner = owner_repository.select_one(id)
    name = request.form["pet_name"]
    species = request.form["species"]
    dob = request.form["dob"]
    symptoms = request.form["symptoms"]
    treatment_id = request.form["treatment_id"]
    treatment = treatment_repository.select_one(treatment_id)
    vet_id = request.form["vet_id"]
    vet = vet_repository.select_one(vet_id)
    animal = Animal(name, species, dob, symptoms, owner, treatment, vet)
    animal_repository.save(animal)
    return redirect("/owners/show.html")