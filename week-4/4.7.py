Write a program to find the sum of the series 1 +11 + 111 + 1111 + . . . + n terms (n will be given as input from the user and sum will be the output)

Sample Test Cases

Test Case 1      

Input

4          

Output

1234 

Test Case 2

Input 

6

Output 

123456

n=int(input())
sum=0
j=1
for i in range (0,n):
    sum=sum+j
    j=(j*10)+1
print(sum)
