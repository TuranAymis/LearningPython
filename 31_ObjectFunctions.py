# Student.py de oluşturduğumuz classı kullanıyoruz
from Student import Student

student_1 = Student("Oscar", "Accounting", 3.6, False)
student_2 = Student("Philip", "Business", 2.4, True)


print(student_1.on_honor_roll())
print(student_2.on_honor_roll())