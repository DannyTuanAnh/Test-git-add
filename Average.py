def average(scores):
    average = sum(scores)/len(scores)
    return f"{average:.2f}"
    
students = {}
n = int(input())
for x in range (n):
    name, *score = input().split()
    scores = list(map(float, score))
    students[name] = average(scores)
query_name = input().strip()
print(f"{students.get(query_name)}")
