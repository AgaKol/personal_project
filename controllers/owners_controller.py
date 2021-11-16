import re
from flask import Flask, render_template, request, redirect, Blueprint
from repositories import owner_repository, animal_repository, vet_repository, treatment_repository
from models.owner import Owner

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