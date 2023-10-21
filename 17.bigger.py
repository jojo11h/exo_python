import random as r

list_of_number = list()

for element in range(10):
    list_of_number.append(r.randint(0, 50))

bigger = 0
for element in list_of_number:
    if bigger <= element:
        bigger = element

print(list_of_number)
print(bigger)


# method rapide utiliser la fonction max()

print(f'le nombre max est :{max(list_of_number)}')
