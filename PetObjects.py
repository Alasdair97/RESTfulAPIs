from VetAnimal import Dog, Cat
from VetOwners import VetOwner

# importing and assigning of data

txt_file = open("CustomerData.txt", "r")
readfile = txt_file.readlines()
txt_file.close()

Pets = []

for i in range(len(readfile)):
    imported_str = readfile[i].strip()
    imported_dict = eval(imported_str)
    print(imported_dict)
    if 'Owner_name' in imported_dict:
        print('This a human')
    elif 'PetName' in imported_dict:
        print('This a pet')
        Pet_i = eval(imported_dict['value'])(imported_dict['PetName'], imported_dict['age'], imported_dict['owner_id'])
        if 'breed' in imported_dict:
            Pet_i.breed = imported_dict['breed']
        if 'colour' in imported_dict:
            Pet_i.colour = imported_dict['colour']
        Pets.append(Pet_i)
    else:
        print('WTF is this')

Alasdair = VetOwner('Alasdair')
Ahmed = VetOwner('Ahmed')
Gareth = VetOwner('Gareth')

# Updates
Pets[1].vist('being slow even for a dog')
Pets[3].vist('Dog bite')

PetOwners = [Alasdair, Ahmed, Gareth]
AnimalList = Pets
print("done")
