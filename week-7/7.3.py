Write a program to eliminate the common elements in the given 2 arrays and print only the non-repeating

elements and the total number of such non-repeating elements.

Input Format:

The first line contains space-separated values, denoting the size of the two arrays in integer format respectively.

The next two lines contain the space-separated integer arrays to be compared.

Sample Input:

5 4

1 2 8 6 5

2 6 8 10

Sample Output:

1 5 10

3

Sample  Input: 

5 5

1 2 3 4 5

1 2 3 4 5

Sample Output:

NO SUCH ELEMENTS
a=input().split()
b=input().split()
c=input().split()
d=""
for i in b:
    if i not in c:
        d=d+i+" "
for i in c:
    if i not in b:
        d=d+i+" "
if len(d)>0:
    print(d)
    x=d.split()
    print(len(x))
else:
    print("NO SUCH ELEMENTS")
