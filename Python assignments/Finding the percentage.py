n = int(input())
student_marks = {}

for _ in range (n):
    name, *line = input().split()
    scores = list(map(float,line))
    student_marks[name]=scores

query_name=input()

marks=student_marks[query_name]
sum=0
for i in marks:
    sum = sum +i
avg = sum/len(marks)
print("{:.2f}.format(avg)")