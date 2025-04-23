#Sohel Tamboli

Test1 = int(input("Enter the Marks of Test1 Exam: "))
Test2 = int(input("Enter the Marks of Test2 Exam: "))

if Test1 < 18 or Test2 < 18:
    print("Not Eligible for End Semester Exam")
elif (Test1 + Test2) >= 36:
    print("Eligible for End Semester Exam")
else:
    print("Not Eligible for End Semester Exam")
