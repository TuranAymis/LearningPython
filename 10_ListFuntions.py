lucky_numbers = [1,3.5,7,33]
friends = ["Görkem", "Onur", "Onur", "Fırat", "Aykut"]

print(friends)
print(lucky_numbers)

friends.extend(lucky_numbers)
print(friends)

friends.append("Şahin")
print(friends)

friends.insert(1,"Kaan")
print(friends)

friends.remove("Kaan")
print(friends)

friends.pop()
print(friends)

print(friends.index("Aykut"))

print(friends.count("Onur"))

lucky_numbers.sort()
print(lucky_numbers)

lucky_numbers.reverse()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)

friends.clear()
print(friends)