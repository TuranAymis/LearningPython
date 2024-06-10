employee_file = open("26_ReadingFiles_text.txt", "r") # r -> read | w -> write | a -> append | r+ -> read and write

print(employee_file.readable()) # Dosya okunabiliyor mu True False cevap verir
print("----------")

print(employee_file.readline()) # Dosyadan ilk satırı okur
print(employee_file.readline()) # Dosyadan sıradaki satırı okur
print("----------")

print(employee_file.readlines()) # Dosyadaki satırları sırayla okur | dosyayı kapatmadığımızdan sıradakileri getiriyor
print("----------")
employee_file.close()

employee_file = open("26_ReadingFiles_text.txt", "r")

for employee in employee_file.readlines():
    print(employee)

employee_file.close()