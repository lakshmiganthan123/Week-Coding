Consider a program to insert an element / item in the sorted array. Complete the logic by filling up required code in editable section. Consider an array of size 10. The eleventh item is the data is to be inserted.

 

Sample Test Cases

 

Test Case 1

 

Input

 

1

3

4

5

6

7

8

9

10

11

2

 

Output

 

ITEM to be inserted:2

After insertion array is:

1

2

3

4

5

6

7

8

9

10

11

 


Test Case 2

 

Input

 

11

22

33

55

66

77

88

99

110

120

44

 

Output

 

ITEM to be inserted:44

After insertion array is:

11

22

33

44

55

66

77

88

99

110

120
l=[]
for i in range (1,11):
    n=int(input())
    l.append(n)
m=int(input())
l.append(m)
print("ITEM to be inserted:",m,sep="")
print("After insertion array is:",end="\n")
l.sort()
for i in l:
    print(i,end="\n")
