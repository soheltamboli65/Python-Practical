#Sohel Tamboli

dict = {}

dict['name'] = 'Sohel'
dict['age'] = 40
dict['city'] = 'Pune'

print("Dictionary:", dict)

name = dict.get('name')
age = dict.get('age')
city = dict.get('city')

print("Name:", name)
print("Age:", age)
print("City:", city)

keys = dict.keys()
print("Keys:", keys)

values = dict.values()
print("Values:", values)

value2 = dict.get('country', 'Not Found')
print("Country (not in dictionary):", value2)
