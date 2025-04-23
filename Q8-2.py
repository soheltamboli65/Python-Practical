#Sohel Tamboli


class Student:
    def __init__(self, name, marks=0):
        self._name = name
        self._marks = marks

    # Modify display to return a string instead of printing
    def display_info(self):
        return f"Name: {self._name}, Marks: {self._marks}"

# Creating an object of the Student class
s1 = Student("Sohel", 80)
s2 = Student("Ayesha")

# Using print to display the returned value from display_info()
print(s1.display_info())
print(s2.display_info())
