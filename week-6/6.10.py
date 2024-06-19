Program to print all the distinct elements in an array. Distinct elements are nothing but the unique (non-duplicate) elements present in the given array.

Input Format:

First line take an Integer input from stdin which is array length n.

Second line take n Integers which is inputs of array.

Output Format:

Print the Distinct Elements in Array in single line which is space Separated

Example Input:

5

1 

2 

2 

3 

4

Output:

1 2 3 4

Example Input:

6

1 

1 

2 

2 

3 

3

Output:

1 2 3
n=int(input())
l=[]
for i in range (n):
    l.append(int(input()))
l.sort()
ll=[]
for i in l:
    if i not in ll:
        ll.append(i)
for i in  ll:
    print(i,end=" ")

