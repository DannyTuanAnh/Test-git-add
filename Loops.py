def square(i):
    return i*i
while True:
    try:
        n = int(input("Enter n: "))
        if 1 <= n <= 20:
            for number in range (0,n,1):
                print("Square each of number in n: ",square(number))
        else:
            print("Please enter 1 <= n <= 20 ")
    except ValueError:
        print("Invalid!!! Please try again.")   
        continue 

    