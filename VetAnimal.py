from abc import ABC, abstractmethod

class Animal(ABC):

    #Attributes
    age = None
    name = None
    health = None
    weight = None # Weight in grams
    IsAlive = True
    
    #Constructors
    def __init__(self,Age,Name,Weight,Health):
        self.value = "Animal"
        self.age = Age
        self.name = Name
        self.weight = Weight
        self.health = Health

    #Methods
    @abstractmethod
    def reproduce(self):
        pass

    def eat(self):
        pass

    def sleep(self):
        return ("I am sleeping")

    def type(self):
        pass

    def grow(self):
        return ("I am growing")

    def die(self):
        self.IsAlive = False
        self.health = 'Dead'
        return

    def healthCheck(self,HealthImput):
        self.health = HealthImput
        return
    
    def weightCheck(self):
        self.weight = input("Please Enter Weight in g: ")
        return

##################### Mammal #################

class Mammal(Animal):
    #Attributes


    #Constructors
    def __init__(self,Age,Name,Weight,Health):
        self.value = "Mammal"
        super().__init__(Age,Name,Weight,Health)


    #Methods
    @abstractmethod
    def eat(self):
        pass
    
    def reproduce(self):
        return "Live Birth"

    def type(self):
        pass

################### Bird ####################

class Bird(Animal):
    #Attributes
    wingspan = None

    #Constructors
    def __init__(self,Age,Name,Weight,Health):
        super().__init__(Age,Name,Weight,Health)
        self.value = "Bird"


    #Methods
    @abstractmethod
    def eat(self):
        pass
    
    def reproduce(self):
        return "Lay Egg"


    def type(self):
        pass

########################### Mammals ##########################
    
################## Cat
        
class Cat(Mammal):
     #Attributes
    colour = None

    #Constructors
    def __init__(self,Age,Name,Weight,Health):
        self.value = "Cat"
        super().__init__(Age,Name,Weight,Health)


    #Methods
    def type(self):
        return(self.value)

    def eat(self):
        return "I eat mice"

################## Dog
        
class Dog(Mammal):
     #Attributes
    breed = None

    #Constructors
    def __init__(self,Age,Name,Weight,Health):
        self.value = "Dog"
        super().__init__(Age,Name,Weight,Health)


    #Methods
    def type(self):
        return(self.value)

    def eat(self):
        return "I eat meat"

########################### Birds ##########################
    
## Pigeon

class Pigeon(Bird):
     #Attributes
    colour = None

    #Constructors
    def __init__(self,Age,Name,Weight,Health):
        self.value = "Pigeon"
        super().__init__(Age,Name,Weight,Health)

    #Methods
    def type(self):
        return(self.value)

    def eat(self):
        return "I eat anythng"

## Parrot

class Parrot(Bird):
     #Attributes
    colour = None

    #Constructors
    def __init__(self,Age,Name,Weight,Health):
        self.value = "Parrot"
        super().__init__(Age,Name,Weight,Health)

    #Methods
    def type(self):
        return(self.value)

    def eat(self):
        return "I eat fruit, seeds and nuts"

## Owl

class Owl(Bird):
     #Attributes
    colour = None

    #Constructors
    def __init__(self,Age,Name,Weight,Health):
        self.value = "Owl"
        super().__init__(Age,Name,Weight,Health)

    #Methods
    def type(self):
        return(self.value)

    def eat(self):
        return "I eat mice, small birds and frogs"
