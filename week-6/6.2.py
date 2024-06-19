Write a program to print all the locations at which a particular element (taken as input) is found in a list and also print the total number of times it occurs in the list. The location starts from 1.

 

For example, if there are 4 elements in the array:

 

5

6

5

7

 

If the element to search is 5 then the output will be:

 

5 is present at location 1

5 is present at location 3

5 is present 2 times in the array.

 

Sample Test Cases

 

Test Case 1

 

Input

 

4

5

6

5

7

5

 

Output

 

5 is present at location 1.

5 is present at location 3.

5 is present 2 times in the array.

 

Test Case 2

 

Input

 

5

67

80

45

97

100

50

 

Output

 

50 is not present in the array.
n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
a=int(input())
b=[]
c=0
for i in range(n):
    if(l[i]==a):
        c+=1
        b.append(i+1)
if(c==0):
    print(a,"is not present in the array.")
else:
    for i in b:
        print(a,"is present at location %d."%i)
    print(a,"is present %d times in the array."%len(b))
 

