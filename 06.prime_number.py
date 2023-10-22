def isprime(num):

    for n in range(2, int(num)):
        if num % n == 0:
            return False
        else:
            return True


print(isprime(int(input('Donne un chiffre : '))))
