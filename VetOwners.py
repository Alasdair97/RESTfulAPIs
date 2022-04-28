from abc import ABC, abstractmethod


class VetOwner(ABC):
    # Attributes
    Class_ID_Counter = 0
    id = []
    Owner_Name = []

    # Constructors
    def __init__(self, owner_name):
        self.value = "owner"
        self.Owner_Name = owner_name
        self.id = VetOwner.Class_ID_Counter
        VetOwner.Class_ID_Counter += 1

    # Methods
 #   @abstractmethod
