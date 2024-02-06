# mylist=[['Rahul', 22.0], ['sumesh', 26.0], ['Amal', 28.0], ['Zhazha', 30.0]]
mylist=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    mylist.append([name,score])
    
mylist.sort(key=lambda x:x[1], reverse=True)
second_lowest = 0
if len(mylist) > 2:
    length = len(mylist)-1
else:
    length = len(mylist)
for i in range (1, length):
    if mylist[i][1] < mylist[i-1][1]:
        second_lowest = mylist[i][1]

mylist.sort(key=lambda x:x[0])

for name,score in mylist:
    if(score == second_lowest):
        print(name)


# print(second_lowest)
# print(mylist)