def seperate_number(numbers):
    return [score for _, score in numbers if isinstance(score, float)]

def lowest_score(low):
    return min(low, default = 0)

def second_lowest_score(students):
    sort_number = seperate_number(students)
    if sort_number != []:
        lowest = lowest_score(sort_number)
        second_lowest = [x for x in sort_number if x != lowest]
        second_name = [name for name, score in students if score == lowest_score(second_lowest)]
        second_name.sort()
        print("Second lowest score is: ", end = "")
        print(lowest_score(second_lowest))
        print("Student have second lowest score is: ", end = "")
        print(', '.join(second_name))
    else:
        print("Score have problem!")
        
while True:
    try:
        students = []
        n = int(input("Enter number student in a class: "))
        for i in range(0, n, 1):
            name_student = str(input(f"Enter name student number {i + 1}: " ))
            score_student = float(input(f"Enter score student number {i+1}: "))
            student = [name_student, score_student]
            students.append(student)
        second_lowest_score(students)
    except ValueError:
        print("Just enter an interger! Try again.")
