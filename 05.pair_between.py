interval_start = int(input('nombre 1 : '))
interval_end = int(input('nombre 2 : '))

for element in range(interval_start,interval_end):
    if element % 2 == 0:
        print(f'{element} est un chiffre pair')
