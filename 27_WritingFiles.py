new_employee = input("Enter new employee: ")



employee_file = open("27_WritingFiles_text.txt", "a")
employee_file.write("\n"+new_employee)
employee_file.close()



employee_file = open("27_WritingFiles_text.txt", "r")
print(employee_file.read())
employee_file.close()

