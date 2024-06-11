# Student.py de student classı oluşturduk

from Student import Student

studen_1 = Student("Jim", "Bussiness", 3.1, False)
studen_2 = Student("Annie", "Engineering", 2.1, True)



print(studen_1.name)
print(studen_1.major)
print(studen_1.gpa)
print(studen_1.is_on_probation)

print("------------")

print(studen_2.name)
print(studen_2.major)
print(studen_2.gpa)
print(studen_2.is_on_probation)