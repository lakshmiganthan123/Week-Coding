Output is a merged array without duplicates.

Input Format

N1 - no of elements in array 1

Array elements for array 1

N2 - no of elements in array 2

Array elements for array2

Output Format

Display the merged array

Sample Input 1

5

1 

2 

3 

6 

9

4

2 

4 

5 

10

Sample Output 1

1 2 3 4 5 6 9 10

n=int(input())
ll=[]
for i in range(n):
    ll.append(int(input()))
m=int(input())
l2=[]
for i in range (m):
    l2.append(int(input()))
l=set(ll+l2)
l=sorted(list(l))
for i in l:
    print(i,end=" ")
