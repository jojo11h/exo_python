import random as r

list_of_number = list()

for element in range(10):
    list_of_number.append(r.randint(0, 50))


modulo_of_3 = list()

for element in list_of_number:
    if element % 3:
        modulo_of_3.append(element)

print(set(list_of_number), end=' ')
print()
print(set((modulo_of_3)), end=' ')
