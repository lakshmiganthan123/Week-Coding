A Number is said to be Disarium number when the sum of its digit raised to the power of their respective positions becomes equal to the number itself. Write a program to print number is Disarium or not.

Input Format:

Single Integer Input from stdin.

Output Format:

Yes or No.

Example Input:

175

Output:

Yes

Explanation

1^1 + 7^2 +5^3 = 175

Example Input:

123

Output:

No
Number=int(input())
length=len(str(Number))
Temp=Number
sum=0
rem=0
while Temp>0:
    rem=Temp%10
    sum=sum+int(rem**length)
    Temp=Temp//10
    length=length-1
if sum ==Number:
    print("Yes")
else:
    print("No")
