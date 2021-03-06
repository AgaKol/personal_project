import pdb
from models.owner import Owner
from models.vet import Vet
from models.treatment import Treatment
from models.animal import Animal

import repositories.owner_repository as owner_repository
import repositories.vet_repository as vet_repository
import repositories.animal_repository as animal_repository
import repositories.treatment_repository as treatment_repository

# owner1 = Owner("James Jones", "1 Rand Street PK3 4MN Dundee", "074939484", "j.jones@mail.com")
# owner_repository.save(owner1)
# result = owner_repository.select_all()
# for row in result:
#      print(row.__dict__)
# result = owner_repository.select_one(1)
# print(result.__dict__)
# owner_repository.delete_one(1)

vet1 = Vet("Jenny Williams", "2 Rand Street PK3 4MN Dundee", "073485659", "j.jones@mail.com", "dogs")
vet2 = Vet("Marie Williams", "2 Rand Street PK3 4MN Dundee", "073485659", "j.jones@mail.com", "cats")
vet_repository.save(vet1)
vet_repository.save(vet2)
# result = vet_repository.select_all()
# for row in result:
#     print(row.__dict__)
# result = vet_repository.select_one(1)
# print(result.__dict__)

