# Sohel Tamboli

# Using break
for num in range(1, 11):
    if num == 5:
        print("Breaking the loop at:", num)
        break
    print("Current number (break loop):", num)

print("\n")

# Using continue
for num in range(1, 11):
    if num == 3:
        continue
    print("Skipping the number 3, current number:", num)

print("\n")

# Using pass
for num in range(1, 11):
    if num == 7:
        pass
    print("Pass executed at:", num)
