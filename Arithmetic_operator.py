def sumOfNumber(a, b):
    return a + b

def differenceOfNumber(a, b):
    return a - b

def productOfNumber(a, b):
    return a * b

while True:
    try:
        firstNumber = int(input("The first line contains the first integer: "))
        secondNumber = int(input("The second line contains the second integer: "))
        if (firstNumber < 1 or firstNumber > 10**10) and (secondNumber < 1 or secondNumber > 10**10):
            print("Invalid the first and the second integer!")
        elif firstNumber < 1 or firstNumber > 10**10:
            print("Invalid the first integer!")
        elif secondNumber < 1 or secondNumber > 10**10:
            print("Invalid the second integer!")
        else:
            print(sumOfNumber(firstNumber, secondNumber))
            print(differenceOfNumber(firstNumber, secondNumber))
            print(productOfNumber(firstNumber, secondNumber))
    except ValueError:
        break
        
                           