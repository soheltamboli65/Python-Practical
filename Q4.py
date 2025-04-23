# Sohel Tamboli

# 1. Creating an array
import array as arr
a = arr.array('i', [1, 2, 3, 4, 5])
print(*a)

# 2. Adding New Element to array
a.insert(1, 4)
print("New Array list:", *a)

# 3. Removing an Element
a.remove(2)
print("Array after removing element:", *a)

# 4. Removing an element using Pop function
a.pop()
print("Array after pop:", *a)

# 5. Slicing an array
print("Slice a[1:4]:", *a[1:4])     # Elements from index 1 to 3
print("Slice a[:3]:", *a[:3])       # First 3 elements
print("Slice a[2:]:", *a[2:])       # Elements from index 2 to end
print("Slice a[::2]:", *a[::2])     # Every 2nd element
print("Slice a[::-1]:", *a[::-1])   # Reversed array

# 6. Reverse Array using reverse()
a.reverse()
print("Reversed array using reverse():", *a)
