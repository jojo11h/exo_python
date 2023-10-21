list_of_word = input('donne moi une liste de mot : ')

if len(list_of_word) < 1:

    list_of_word = "Programmez un script qui affiche le nombre total de caractères dans une liste de mots.Pour aller plus loin, vous pouvez, par exemple, transformer votre code en une fonction qui prend des listes en paramètre, vérifier que ce sont bien des listes contenant des mots et pas d autres types de variables."

if isinstance(list_of_word, str):

    print(list_of_word)
    list_of_word = list(list_of_word.lower().replace(' ', ''))
    print(f'Il y a {len(list_of_word)} charactères')
