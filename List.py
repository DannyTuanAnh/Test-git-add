def list(x,y,z):
    for i in range(0, x + 1, 1):
                if i == 0:
                    print("[", end = "")
                for j in range(0, y + 1, 1):
                    for k in range(0, z + 1, 1):
                        if i + j + k == n:
                            continue
                        elif i == x and j == y and k == z: 
                            print("[",i,", ",j,", ",k,"]",sep = "", end = "] \n")
                        else:
                            print("[",i,", ",j,", ",k,"]",sep = "", end = ", ")

while True:
    try:    
        x = int(input("Enter x: "))
        y = int(input("Enter y: "))
        z = int(input("Enter z: "))
        n = int(input("Enter n: "))
        if x == 0 and y == 0 and z == 0 and n == 0:
            print("[]")
        else:
            list(x,y,z)  
    except ValueError:
        print("Invalid!")
        continue 
        
                