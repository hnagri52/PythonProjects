class Student:
    classes_skipped = 0
    pass


hussein = Student()
sabi = Student()


hussein.name = "Hussein"
hussein.age = 19
hussein.height = 6

sabi.name = "sabi"
sabi.age = 18
sabi.height = 5


sabi.classes_skipped = 2

print(Student.classes_skipped, sabi.classes_skipped)
print(hussein.__dict__, "\n", sabi.__dict__, "\n\nNow showing how classes work")


print("Before ", Student.__dict__)
#now that I change it, everything will inherit
Student.classes_skipped = 3
print("After: ", Student.__dict__)
print(hussein.classes_skipped)