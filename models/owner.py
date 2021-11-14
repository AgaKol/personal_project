from models.person import Person


class Owner:
    def __init__(self, name, address, phone, email, registered = True, id = None):
        Person.__init__(self, name, address, phone, email)
        self.registered = registered
        self.id = id