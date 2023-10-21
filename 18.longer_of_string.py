list_of_word = input('donne moi une liste de mot : ')

if len(list_of_word) < 1:

    list_of_word = "Créer un programme qui permet d afficher la chaîne de caractères d une liste la plus longue."

list_of_word = list_of_word.lower().split()

bigger = list()

for element in list_of_word:
    if len(element) > len(bigger):
        print(element, '=>', len(element))
        bigger = element

print(f'le mot le plus long est : {bigger}')
