user_number = int(input('donne moi un nombre : '))


factorial_of_number = 1
for number in range(user_number):
    factorial_of_number *= number + 1
    print(number)


print(factorial_of_number)
