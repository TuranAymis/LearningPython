is_male = True
is_tall = False

if is_male:
    print("You are a male")
else:
    print("You are not a male")

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You neither a male nor tall")

if is_male and is_tall:
    print("You are a tall male")
else:
    print("You are either not male or not tall or both")

if is_male and is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall):
    print("You are a shot male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall")