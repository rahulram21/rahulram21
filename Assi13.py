#Write a Python program that takes a list of numbers and calculates the sum of all even numbers in the list

evenList = [1,2,3,4,5,6,7,8,12,17,9]
sum = 0
for i in evenList:
    if(i % 2 == 0):
        sum += i

print(sum)