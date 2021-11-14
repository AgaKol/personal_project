class Animal:
    def __init__(self, name, species, dob, symptoms, owner, treatment = None, vet = None, id = None):
        self.name = name
        self.species = species
        self.dob = dob
        self.symptoms = symptoms
        self.owner = owner
        self.treatment = treatment
        self.vet = vet
        self.id = id