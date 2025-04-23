#Sohel Tamboli

# Base class

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"The {self.species} named {self.name} makes a sound.")

# Derived class

class Dog(Animal):
    def __init__(self, name, breed):
        
        # Calling the constructor of the base class
        super().__init__(name, "Dog")
        self.breed = breed

    def speak(self):
        print(f"The {self.breed} dog named {self.name} barks.")

# Creating an object of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")

# Displaying details and calling the method
dog1.speak()  
