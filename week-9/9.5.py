An e-commerce company plans to give their customers a special discount for Christmas.

They are planning to offer a flat discount. The discount value is calculated as the sum of all

the prime digits in the total bill amount.

Write an algorithm to find the discount value for the given total bill amount.

Constraints

1 <= orderValue< 10e100000

Input

The input consists of an integer orderValue, representing the total bill amount.

Output

Print an integer representing the discount value for the given total bill amount.

Example Input

578

Output

12

def christmasDiscount(n):
    n=str(n)
    a=0
    for i in n:
        i=int(i)
        if(i%2!=0 and i%3!=0 and i%5!=0)or(i==2)or(i==3)or(i==5):
            a+=i
    return a
