
# programme qui utilise la reccursion

def fibonacci(number):
    if number <= 1:
        return number
    else:
        return (fibonacci(number - 1) + fibonacci(number - 2))


user_input = int(input('saisir un nombre pour la suite de Fibonacci :'))
element = 0

while fibonacci(element) <= user_input + 1:
    print(fibonacci(element))
    element += 1
