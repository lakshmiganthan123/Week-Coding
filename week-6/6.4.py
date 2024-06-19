Complete the program to count frequency of each element of an array. Frequency of a particular element will be printed once.

 

Sample Test Cases

 

Test Case 1

 

Input

 

7

23

45

23

56

45

23

40

 

Output

 

23 occurs 3 times

45 occurs 2 times

56 occurs 1 times

40 occurs 1 times
n=int(input())
ll=[]
for i in range(n):
    ll.append(int(input()))
l2=[]
for x in ll: 
    if(x not in l2):
        l2.append(x)
for i in range(0,len(l2)):
    c=ll.count(l2[i])
    print(l2[i],"occurs",c,"times")
    
