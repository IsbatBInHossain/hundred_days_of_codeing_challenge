from math import sqrt

def prime_checker(number):
    x = round(sqrt(number))
    count = 2
    is_prime = True
    while (is_prime and count<=x):
        if number%count == 0:
            is_prime = False
            print("It's not a prime number.")
        elif count == x:
            print("It's a prime number.")
        count+=1

n = int(input("Check this number: "))
prime_checker(number=n)
