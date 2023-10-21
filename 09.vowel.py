user_promt = input('rentrez une chaîne de charactère : ').lower()
vowel = "aeiou"


for element in user_promt:
    if vowel.find(element) != -1:
        print(element, end=' ')
