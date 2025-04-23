#Sohel Tamboli

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating an object of the Person class
person1 = Person("Sohel", 40)

# Displaying the details of the person object
person1.display_details()
