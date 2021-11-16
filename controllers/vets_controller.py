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

@vet_blueprint.route('/vets/<id>', methods = ["GET"])
def show_vet(id):
    vet = vet_repository.select_one(id)
    animals = animal_repository.select_all()
    return render_template("vets/show.html", vet = vet, animals = animals)

@vet_blueprint.route("/vets/<id>/edit", methods = ["GET"])
def edit_vet(id):
    vet = vet_repository.select_one(id)
    return render_template("vets/edit.html", vet = vet)

@vet_blueprint.route("/vets/<id>", methods = ["POST"])
def update_vet(id):
    name = request.form["name"]
    address = request.form["address"]
    phone = request.form["phone"]
    email = request.form["email"]
    speciality = request.form["speciality"]
    vet = Vet(name,address,phone,email,speciality,id)
    vet_repository.update(vet)
    return redirect("/vets")

@vet_blueprint.route("/vets/<id>/delete", methods = ["POST"])
def delete_vet(id):
    vet_repository.delete_one(id)
    return redirect("/vets")