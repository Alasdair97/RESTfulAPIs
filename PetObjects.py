from VetAnimal import Dog, Cat
from VetOwners import VetOwner

# importing and assigning of data

txt_file = open("CustomerData.txt", "r")
readfile = txt_file.readlines()
Pet = []

for i in range(len(readfile)):
    imported_animal_str = readfile[i].strip()
    imported_animal_dict = eval(imported_animal_str)
    print(imported_animal_dict)
    Pet_i = eval(imported_animal_dict['value'])(imported_animal_dict['PetName'], imported_animal_dict['age'],
                                                imported_animal_dict['owner_id'])
    if 'breed' in imported_animal_dict:
        Pet_i.breed = imported_animal_dict['breed']
    if 'colour' in imported_animal_dict:
        Pet_i.breed = imported_animal_dict['colour']
    Pet.append(Pet_i)


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
Leia = Cat('Leia', 18, 0)  # , 'white')

Mac = Dog('Mac', 3, 1)  # , 'Boxer')
Mac.vist('being slow even for a dog')

CptJPants = Cat('Captain Jazzy Pants', 4, 2) # , 'Ginger')

# print(Oscar.PetName, 'was at the vest for', Oscar.WhyLastVisit)
# print(Mac.PetName, 'was at the vest for', Mac.WhyLastVisit)
# OscarVars = vars(Oscar)
# print(OscarVars)
Pet[1].vist('being slow even for a dog')

PetOwners = [Alasdair, Ahmed, Gareth]
AnimalList = Pet
print("done")
