def factorial(number):
    if number == 0:
        return 1
    if number != 0:
        return number * factorial(number - 1)


number = int(input("Enter a number: "))
print(factorial(number))