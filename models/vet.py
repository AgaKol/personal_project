from models.person import Person


class Vet:
    def __init__(self, name, address, phone, email, speciality, id = None):
        Person.__init__(self, name, address, phone, email)
        self.speciality = speciality
        self.id = id