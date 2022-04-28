from VetAnimal import Dog, Cat
from VetOwners import VetOwner

# importing and assigning of data

txt_file = open("CustomerData.txt", "r")
readfile = txt_file.readlines()
txt_file.close()

Pets = []
Owners = []

for i in range(len(readfile)):
    imported_str = readfile[i].strip()
    imported_dict = eval(imported_str)
    # print(imported_dict)
    if 'Owner_Name' in imported_dict:
        print('This a human')
        Owner_i = VetOwner(imported_dict['Owner_Name'])
        Owners.append(Owner_i)
    elif 'PetName' in imported_dict:
        print('This a pet')
        Pet_i = eval(imported_dict['value'])(imported_dict['PetName'], imported_dict['age'], imported_dict['owner_id'])
        if 'breed' in imported_dict:
            Pet_i.breed = imported_dict['breed']
        if 'colour' in imported_dict:
            Pet_i.colour = imported_dict['colour']
        Pets.append(Pet_i)
    else:
        print('ERROR: Not an Owner or Animal')

# Updates
Pets[1].vist('being slow even for a dog')
Pets[3].vist('Dog bite')

PetOwners = Owners
AnimalList = Pets
