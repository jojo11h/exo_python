user_promt = list('essais')

print(user_promt)
for element in range(len(user_promt)):
    if element % 2 != 0:
        user_promt[element].upper()
        print(user_promt[element].upper(), end='')
    else:
        print(user_promt[element], end='')
