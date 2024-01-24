#Write a Python program that takes a sentence as input and prints the first three words.

str = input("Enter your sentance here ")

m=str.split(" ")

i=0
while i<len(m):
    print(m[i])
    i+=1
    if(i==3):
        break