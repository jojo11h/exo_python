
bool = False

while bool == False:
    user_word = input('trouve moi un palindrome : ')
    if user_word == user_word[::-1]:
        # user_word[::-1] inverse mon string ( c'est un peu comme la fonction .reverse())
        print("c'est bien un palindrome")
        bool = True
    else:
        print('raté !')
