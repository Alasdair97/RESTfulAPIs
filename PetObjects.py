from VetAnimal import Dog, Cat
from VetOwners import VetOwner

# importing and assigning of data

txt_file = open("CustomerData.txt", "r")
readfile = txt_file.readlines()

imported_animal_str = readfile[0].strip()
imported_animal_dict = eval(imported_animal_str)

print(imported_animal_dict)
Oscar = eval(imported_animal_dict['value'])(imported_animal_dict['PetName'], imported_animal_dict['age'], imported_animal_dict['owner_id'], imported_animal_dict['breed'])

# Type = imported_animal_dict['value']
# method_to_call = getattr(Dog, 'PetName')
# Test = imported_animal_dict['PetName']
# Test2 = imported_animal_dict['owner_id']
# TestAnimal = VetAnimal(Type)

txt_file.close()

Alasdair = VetOwner('Alasdair')
Ahmed = VetOwner('Ahmed')
Gareth = VetOwner('Gareth')

# Creation of pets
# Oscar = Dog('Oscar', 7, 0, 'weimaraner')
Leia = Cat('Leia', 18, 0, 'white')

Mac = Dog('Mac', 3, 1, 'Boxer')
Mac.vist('being slow even for a dog')

CptJPants = Cat('Captain Jazzy Pants', 4, 2, 'Ginger')

# print(Oscar.PetName, 'was at the vest for', Oscar.WhyLastVisit)
# print(Mac.PetName, 'was at the vest for', Mac.WhyLastVisit)
# OscarVars = vars(Oscar)
# print(OscarVars)

PetOwners = [Alasdair, Ahmed, Gareth]
AnimalList = [Oscar, Leia, Mac, CptJPants]
