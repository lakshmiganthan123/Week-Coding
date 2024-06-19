Write a python program to count all letters, digits, and special symbols respectively from a given string

ip=input()
l=0
d=0
sy=0
for char in ip:
    if char.isalpha():
        l+=1
    elif char.isdigit():
        d+=1
    else:
        sy+=1
print(l)
print(d)
print(sy)
