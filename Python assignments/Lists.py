
mylist=[]
N = int(input())

i=0
while i<N:
    commands = input().split(' ')
    if commands[0] == 'print':
        print(mylist)
    if commands[0] == 'sort':
        mylist.sort()
    if commands[0] == 'reverse':
        mylist.reverse()
    if commands[0] == 'pop':
        mylist.pop()
    if commands[0] == 'append':
        mylist.append(int(commands[1]))
    if commands[0] == 'remove':
        mylist.remove(int(commands[1]))
    if commands[0] == 'insert':
        mylist.insert(int(commands[1]), int(commands[2]))
    i+=1



# insert
# append
# remove
# pop
# reverse
# print
# sort

# 12
# insert 0 5
# insert 1 10
# insert 0 6
# print
# remove 6
# append 9
# append 1
# sort
# print
# pop
# reverse
# print