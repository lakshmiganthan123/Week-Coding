Given a tuple and a positive integer k, the task is to find the count of distinct pairs in the tuple whose sum is equal to K.

Examples:

Input: t = (5, 6, 5, 7, 7, 8 ), K = 13 
Output: 2 
Explanation: 
Pairs with sum K( = 13) are  {(5, 8), (6, 7), (6, 7)}. 
Therefore, distinct pairs with sum K( = 13) are { (5, 8), (6, 7) }. 
Therefore, the required output is 2.

a=input()
b=int(input())
a=a.split(",")
x=[]
for i in a:
    i=int(i)
    for j in a:
        j=int(j)
        if i+j==b:
            x.append(i)
y=(len(set(x)))
print(int(y/2))
