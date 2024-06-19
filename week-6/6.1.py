Write a Python program to check if a given list is strictly increasing or not. Moreover, If removing only one element from the list results in a strictly increasing list, we still consider the list true

Input:

n : Number of elements

List1: List of values

Output

Print "True" if list is strictly increasing or decreasing else print "False"

Sample Test Case

Input

7

1

2

3

0

4

5

6

Output 

True
n=int(input())
ll=[]
for i in range(n):
    ll.append(int(input()))
la=sorted(ll)
lb=sorted(ll,reverse=True)
if(ll==la or ll==lb):
    print("True")
else:
    f=0
    for i in range(len(ll)):
        b=ll.pop(i)
        l2a=sorted(ll)
        l2b=sorted(ll,reverse=True)
        if (ll==l2a or ll==l2b):
            f=1 
            break 
        else:
            ll.insert(i,b)
    if(f==0):
        print(False)
    else:
            print(True)
