#Giraffe Language
#vowels -> Giraffe
#-----------------------

#dog -> dgg
#cat -> cgt


def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "aeıioöuü":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation +"g"

        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))