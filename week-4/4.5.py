Given a number N, find the next perfect square greater than N.

Input Format:

Integer input from stdin.

Output Format:

Perfect square greater than N.

Example Input:

10

Output:

16

import math
n=int(input())
while True:
    n=n+1
    s=int(math.sqrt(n))
    if (s*s==n):
        print(n)
        break
