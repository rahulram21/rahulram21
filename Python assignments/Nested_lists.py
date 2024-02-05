mylist=[]
minn=0
for i in range(int(input())):
    name = input()
    score = float(input())
    mylist.append([name,score])
    
mylist.sort(key=lambda x:x[1])
print(mylist)
