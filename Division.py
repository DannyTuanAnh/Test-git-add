def integerDivision(a,b):
    return a//b

def floatDivision(a,b):
    return a/b

while True:
    try:
        firstNumber = int(input())
        secondNumber = int(input())
        if firstNumber < 0 and secondNumber < 0:
            print("This is not integer!")
        elif firstNumber <0:
            print("The first number is not integer!")
        elif secondNumber < 0:
            print("The second number is not integer!")
        elif secondNumber == 0:
            print("Error!!!")
        else:
            print(integerDivision(firstNumber, secondNumber))
            print(floatDivision(firstNumber, secondNumber))
    except ValueError:
        break
