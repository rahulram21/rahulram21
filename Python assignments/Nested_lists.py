#mylist=[['Rahul', 22.0], ['sumesh', 26.0], ['Amal', 28.0], ['Zhazha', 30.0]]
mylist=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    mylist.append([name,score])
    
mylist.sort(key=lambda x:x[1], reverse=True)
length = len(mylist)
lowest = mylist[length-1][1]


mylist=[[name,score] for name,score in mylist if score!=lowest]
second_lowest = mylist[len(mylist)-1][1]

mylist.sort(key=lambda x:x[0])

for name,score in mylist:
    if(score == second_lowest):
        print(name)
