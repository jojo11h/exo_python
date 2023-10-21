list_of_number = list(range(20))

some_of_list = 0
for element in list_of_number:
    some_of_list += element

print(f'La moyenne de cette list est : {some_of_list / len(list_of_number)}')
