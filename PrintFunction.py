def change_string(i):
    a = str(i)
    print(a, end = "")
    
while True:
    try:
        number = int(input("Enter n: "))
        if 1 <= number <= 150:
            for i in range(1, number + 1, 1):
                change_string(i)
                if i == number:
                    print()
        else:
            print("Please enter 1 <= n <= 150!")
    except ValueError:
        print("Invalid!")
        continue 


    

    