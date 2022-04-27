from abc import ABC, abstractmethod
import itertools


class VetAnimal(ABC):
    # Attributes

    IsAlive = True
    diet = None
    id_iter = itertools.count()
    WhyLastVisit = 'First check up'
    PetName = []

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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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
    diet = ['meat', 'dog food']

    # Constructors
    def __init__(self, pet_name, age, breed):
        self.value = "dog"
        self.PetName = pet_name
        self.age = age
        self.breed = breed
        self.id = next(self.id_iter)


    def __repr__(self):
        rep = 'dog'
        return rep

    # Methods
    def type(self):
        return self.value

    def eats(self):
        return self.diet

# giraffe


class Giraffe(Mammal):
    # Attributes
    diet = ['leaves']

    # Constructors
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
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
    def __init__(self):
        self.value = "panda"

    def __repr__(self):
        rep = 'panda'
        return rep

    # Methods
    def type(self):
        return self.value

    def eats(self, Food):
        if Food in self.diet:
            self.Test = True
            return
        else:
            self.Test = False


# Sheep

class Sheep(Mammal):
    # Attributes
    diet = ['grass']

    # Constructors
    def __init__(self):
        self.value = "sheep"

    def __repr__(self):
        rep = 'sheep'
        return rep

    # Methods
    def type(self):
        return self.value

    def eats(self, Food):
        if Food in self.diet:
            self.Test = True
            return
        else:
            self.Test = False


# Birds ##########################

# chicken


class Chicken(Bird):
    # Attributes
    diet = ['bug']

    # Constructors
    def __init__(self):
        self.value = "chicken"

    def __repr__(self):
        rep = 'chicken'
        return rep

    # Methods
    def type(self):
        return self.value

    def eats(self, Food):
        if Food in self.diet:
            self.Test = True
            return
        else:
            self.Test = False


# Others ##########################

# Bug

class Bug(VetAnimal):
    # Attributes
    diet = ['leaves']

    # Constructors
    def __init__(self):
        self.value = "Bug"

    def __repr__(self):
        rep = 'bug'
        return rep

    # Methods
    def reproduce(self):
        return "Lay Egg"

    def type(self):
        return self.value

    def eats(self, Food):
        if Food in self.diet:
            self.Test = True
            return
        else:
            self.Test = False


# big-fish
class Big_Fish(VetAnimal):
    # Attributes
    diet = ['little_fish']

    # Constructors
    def __init__(self):
        self.value = "big_fish"

    def __repr__(self):
        rep = 'big_fish'
        return rep

    # Methods
    def type(self):
        return self.value

    def reproduce(self):
        return "Lay Eggs"

    def eats(self, Food):
        if Food in self.diet:
            self.Test = True
            return
        else:
            self.Test = False


# Little-fish
class Little_Fish(VetAnimal):
    # Attributes
    diet = ['']

    # Constructors
    def __init__(self):
        self.value = "little_fish"

    def __repr__(self):
        rep = 'little_fish'
        return rep

    # Methods
    def type(self):
        return self.value

    def reproduce(self):
        return "Lay Eggs"

    def eats(self, Food):
        if Food in self.diet:
            self.Test = True
            return
        else:
            self.Test = False


# grass
class Grass(VetAnimal):
    # Attributes
    diet = []

    # Constructors
    def __init__(self):
        self.value = "grass"

    def __repr__(self):
        rep = 'grass'
        return rep

    # Methods
    def reproduce(self):
        return "pollinate"

    def type(self):
        return self.value

    def eats(self, Food):
        if Food in self.diet:
            self.Test = True
            return
        else:
            self.Test = False


# leaves
class Leaves(VetAnimal):
    # Attributes
    diet = []

    # Constructors
    def __init__(self):
        self.value = "leaves"

    def __repr__(self):
        rep = 'leaves'
        return rep

    # Methods
    def reproduce(self):
        return "pollinate"

    def type(self):
        return self.value

    def eats(self, Food):
        if Food in self.diet:
            self.Test = True
            return
        else:
            self.Test = False