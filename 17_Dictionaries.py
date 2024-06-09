monthConvertions = {
    "jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}

monthConvertions2 = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

print(monthConvertions["Nov"])

print(monthConvertions.get("Dec"))

print(monthConvertions.get("May", "Not a valid key"))

print(monthConvertions.get("Luv", "Not a valid key"))


print(monthConvertions2[1])

print(monthConvertions2.get(2))

print(monthConvertions2.get(3, "Not a valid key"))

print(monthConvertions2.get(0, "Not a valid key"))