# Sohel Tamboli

# 1. Creating lists
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
print("List 1:", list1)
print("List 2:", list2)

# 2. Concatenation
concatenated_list = list1 + list2
print("After Concatenation:", concatenated_list)

# 3. Repetition
repeated_list = list1 * 2
print("Repeated List:", repeated_list)

# 4. Membership operations
check_element = 3
if check_element in list1:
    print(check_element, "is in list")
else:
    print(check_element, "is not in list")

# 5. Manipulating list elements
list1.append(9)                  # Add element to list1
print("After Append to List 1:", list1)

list2[1] = 10                    # Update element at index 1 in list2
print("After Update List 2:", list2)

list1.remove(9)                  # Remove the first occurrence of 9 in list1
print("After Deletion from List 1:", list1)
