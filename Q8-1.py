#Sohel Tamboli


# Method Overloading and Overriding

# Parent class for overriding

class Animal:
    def speak(self):
        print("The animal makes a sound")

# Child class overriding the speak method

class Dog(Animal):
    def speak(self):  # Method Overriding
        print("The dog barks")

# Method Overloading (simulated with default argument)

class Calculator:
    def add(self, a=0, b=0, c=0):  # Method Overloading simulation with default values
        return a + b + c

# Creating objects
animal = Animal()
dog = Dog()

# Overridden method
animal.speak()
dog.speak()

# Method Overloading
calc = Calculator()
print("Sum of 0, 0, and 0:", calc.add())         # Should print 0 (using default values)
print("Sum of 5, 10, and 0:", calc.add(5, 10))   # Should print 15
print("Sum of 5, 10, and 15:", calc.add(5, 10, 15)) # Should print 30
