Given an integer N, check whether N the given number can be made a perfect square after adding to it.

Input Format:

Single integer input.

Output Format:

Yes or No.

Example Input:

24

Output:

Yes

Example Input:

26

Output:

No

import math       
n=int(input())
a=n+1
s=int(math.sqrt(a))
if(s*s==a):
    print("Yes")
else:
    print("No")
