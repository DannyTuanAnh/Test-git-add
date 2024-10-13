def leap(i):
    match i:
        case i if i % 4 == 0 and i % 100 != 0 and i % 400 != 0:
            print("It's a leap year")
        case i if i % 4 == 0 and i % 100 == 0 and i % 400 != 0:
            print("It's not a leap year")
        case i if i % 4 == 0 and i % 100 == 0 and i % 400 == 0:
            print("It's a leap year")
        case i if i % 4 != 0:
            print("It's not a leap year")

while True:
    try:
        year = int(input("Enter year: "))
        if 1900 <= year <= 10**5:
            leap(year)
        else:
            print("Please enter 1900 <= year <= 10^5: ")
    except ValueError:
        print("Invalid!")
        continue 
 