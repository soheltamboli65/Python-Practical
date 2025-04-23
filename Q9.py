# Sohel Tamboli

# Creating a list

list = [3,4,5,1,2,9,8]
print("Original List:", list)

# 1. append() – adds a single element at the end

list.append(6)
print(list)

# 2. extend() – adds multiple elements at the end

list.extend([7, 10])
print(list)

# 3. pop() – removes and returns the last item

list.pop()
print("After pop():", list)

# 4. remove() – removes the first occurrence of a value

list.remove(1)
print("After remove(2):", list)

# 5. sort() – sorts the list in ascending order

list.sort()
print(list)
