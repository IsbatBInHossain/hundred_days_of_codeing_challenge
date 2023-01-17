from os import system
from art import logo


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


calc_dictionary = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculator():
    print(logo)
    num1 = float(input("Input the first number: "))

    for i in calc_dictionary:
        print(i)

    should_continue = True

    while should_continue:
        operation = input("Pick an operation. ")
        num2 = float(input("Input the next number: "))
        answer = calc_dictionary[operation](num1, num2)

        print(f"{num1} {operation} {num2} = {answer}")

        if input( "Type 'y' to continue with current number or type 'n' to start a new calculation. ") == 'y':
            num1 = answer
        else:
            should_continue == False
            system('cls')
            calculator()


calculator()
