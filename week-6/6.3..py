Write a Python program to Zip two given lists of lists.

Input:

m : row size

n: column size

list1 and list 2 :  Two lists

Output

Zipped List : List which combined both list1 and list2

Sample test case

Sample input

2

2
1 

3

5

7
2

4

6

8
Sample Output

[[1, 3, 2, 4], [5, 7, 6, 8]]
a=int(input())
b=int(input())
al=[]
bl=[]
a2=[]
b2=[]
c2=[]
for i in range (a*b):
    al.append(int(input()))
for i in range (b*a):
    bl.append(int(input()))
a2.extend(al[:b])
a2.extend(bl[:b])
b2.extend(al[b:])
b2.extend(bl[b:])
c2.append(a2)
c2.append(b2)
print(c2)
