from abc import ABC, abstractmethod

class VetAnimal(ABC):
    # Attributes
    Class_ID_Counter = 0
    IsAlive = True
    PetName = []
    owner_id = []

    # Constructors
    def __init__(self, pet_name):
        self.value = "Animal"

    # Methods
    @abstractmethod
    def type(self):
        pass

    def changePetName(self, petName):
        self.PetName = petName
        return

    def die(self):
        self.IsAlive = False
        return

    def eats(self):
        pass

    def vist(self, why):
        self.WhyLastVisit = str(why)
        return


# Mammal #################


class Mammal(VetAnimal):
    # Attributes

    # Constructors
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.value = "Mammal"

    # Methods
    @abstractmethod
    def type(self):
        pass

    def eats(self):
        pass


# Bird ####################


class Bird(VetAnimal):
    # Attributes
    wingspan = None

    # Constructors
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.value = "Bird"

    # Methods
    @abstractmethod
    def type(self):
        pass

    def eats(self):
        pass


# Mammals ##########################

# antelope


class Antelope(Mammal):
    # Attributes
    diet = ['grass']

    # Constructors
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.value = "antelope"

    def __repr__(self):
        rep = 'antelope'
        return rep

    # Methods
    def type(self):
        return self.value

    def eats(self):
        return self.diet


# Fox


class Fox(Mammal):
    # Attributes
    diet = ['chicken', 'sheep']

    # Constructors
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.value = "fox"

    def __repr__(self):
        rep = 'fox'
        return rep

    # Methods
    def type(self):
        return self.value

    def eats(self):
        return self.diet


# Dog #####################################
class Dog(Mammal):
    # Attributes
    # diet = ['meat', 'dog food'] # Future Implementation

    # Constructors
    def __init__(self, pet_name, age, owner_id, breed):
        super().__init__(pet_name)
        self.value = "dog"
        self.PetName = pet_name
        self.age = age
        self.breed = breed
        self.owner_id = owner_id
        self.pet_id = VetAnimal.Class_ID_Counter
        self.WhyLastVisit = 'First check up'
        VetAnimal.Class_ID_Counter += 1


    def __repr__(self):
        rep = 'dog'
        return rep

    # Methods
    def type(self):
        return self.value


class Cat(Mammal):
    # Attributes
    # diet = ['meat', 'dog food'] # Future Implementation

    # Constructors
    def __init__(self, pet_name, age, owner_id, colour):
        super().__init__(pet_name)
        self.value = "cat"
        self.PetName = pet_name
        self.age = age
        self.colour = colour
        self.owner_id = owner_id
        self.pet_id = VetAnimal.Class_ID_Counter
        self.WhyLastVisit = 'First check up'
        VetAnimal.Class_ID_Counter += 1

    def __repr__(self):
        rep = 'cat'
        return rep

    # Methods
    def type(self):
        return self.value


# giraffe


class Giraffe(Mammal):
    # Attributes
    diet = ['leaves']

    # Constructors
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.value = "giraffe"

    def __repr__(self):
        rep = 'giraffe'
        return rep

    # Methods
    def type(self):
        return self.value

    def eats(self):
        return self.diet


# bear ###################################################


class Bear(Mammal):
    # Attributes
    diet = ['big_fish', 'bug', 'chicken', 'cow', 'leaves', 'sheep']

    # Constructors
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.value = "bear"

    def __repr__(self):
        rep = 'bear'
        return rep

    # Methods
    def type(self):
        return self.value

    def eats(self):
        return self.diet


# Cow


class Cow(Mammal):
    # Attributes
    diet = ['grass']

    # Constructors
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.value = "cow"

    def __repr__(self):
        rep = 'cow'
        return rep

    # Methods
    def type(self):
        return self.value

    def eats(self):
        return self.diet


# Lion


class Lion(Mammal):
    # Attributes
    diet = ['antelope', 'cow']

    # Constructors
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.value = "lion"

    def __repr__(self):
        rep = 'lion'
        return rep

    # Methods
    def type(self):
        return self.value

    def eats(self):
        return self.diet

# Panda


class Panda(Mammal):
    # Attributes
    diet = ['leaves']

    # Constructors
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.value = "panda"

    def __repr__(self):
        rep = 'panda'
        return rep

    # Methods
    def type(self):
        return self.value


# Sheep

class Sheep(Mammal):
    # Attributes
    diet = ['grass']

    # Constructors
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.value = "sheep"

    def __repr__(self):
        rep = 'sheep'
        return rep

    # Methods
    def type(self):
        return self.value


# Birds ##########################

# chicken


class Chicken(Bird):
    # Attributes
    diet = ['bug']

    # Constructors
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.value = "chicken"

    def __repr__(self):
        rep = 'chicken'
        return rep

    # Methods
    def type(self):
        return self.value


# Others ##########################

# Bug

class Bug(VetAnimal):
    # Attributes
    diet = ['leaves']

    # Constructors
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.value = "Bug"

    def __repr__(self):
        rep = 'bug'
        return rep

    # Methods
    def reproduce(self):
        return "Lay Egg"

    def type(self):
        return self.value


# big-fish
class Big_Fish(VetAnimal):
    # Attributes
    diet = ['little_fish']

    # Constructors
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.value = "big_fish"

    def __repr__(self):
        rep = 'big_fish'
        return rep

    # Methods
    def type(self):
        return self.value

    def reproduce(self):
        return "Lay Eggs"


# Little-fish
class Little_Fish(VetAnimal):
    # Attributes
    diet = ['']

    # Constructors
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.value = "little_fish"

    def __repr__(self):
        rep = 'little_fish'
        return rep

    # Methods
    def type(self):
        return self.value

    def reproduce(self):
        return "Lay Eggs"


# grass
class Grass(VetAnimal):
    # Attributes
    diet = []

    # Constructors
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.value = "grass"

    def __repr__(self):
        rep = 'grass'
        return rep

    # Methods
    def reproduce(self):
        return "pollinate"

    def type(self):
        return self.value


# leaves
class Leaves(VetAnimal):
    # Attributes
    diet = []

    # Constructors
    def __init__(self, pet_name):
        super().__init__(pet_name)
        self.value = "leaves"

    def __repr__(self):
        rep = 'leaves'
        return rep

    # Methods
    def reproduce(self):
        return "pollinate"

    def type(self):
        return self.value
