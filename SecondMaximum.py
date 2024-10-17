def check_score(arr):
    for i in arr:
        if not (-100 <= i <= 100):
            return False
    return True 

def highest_score(arr):
    return max(arr, default = 0)

def runner_up_score(arr):   
    if check_score(arr) == True:
        max_score = highest_score(arr)
        runner_up = [i for i in arr if i != max_score]
        if runner_up != []:
            print(highest_score(runner_up))
        else:
            print("This is emty!")
    else:
        print("Invalid score!")
        
while True:
    try:      
        n = int(input("Enter quanity score: "))
        if 2 < n <= 10:
            arr = list(map(int, input("Enter score: ").split()))
            if len(arr) == n:
                runner_up_score(arr)
            elif len(arr) > n:
                print("Too much score! Try again.")
            else:
                print("Too little score! Try again.")
        elif n <= 2:
            print("Too little quanity! Try again.")
        else:
            print("Too much quanity! Try again.")
    except ValueError:
        print("Just enter a number! Try again.")