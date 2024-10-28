def average(scores):
    average = sum(scores)/len(scores)
    return f"{average:.2f}"
     
students = {}
while True:
    n = int(input("Enter n: "))
    try:
        if 2 <= n <= 10:
            for x in range (n):
                name, *score = input(f"Student {x + 1}: ").split()
                scores = list(map(float, score))
                if all(0 <= score <= 100 for score in scores) : 
                    students[name] = average(scores)
                else:
                    print("Exceed value!!!")
                    break 
            else:
                query_name = input("Enter your name you need to find: ").strip()
                print(f"Point is: {students.get(query_name)}")
        else:
            print("Just in 2 <= n <= 10.")
            continue
    except ValueError:
        print("Invalid!")
        continue