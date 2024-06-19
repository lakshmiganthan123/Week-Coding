A number is considered to be ugly if its only prime factors are 2, 3 or 5.

[1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15, …] is the sequence of ugly numbers.

Task:

complete the function which takes a number n as input and checks if it's an ugly number.

return ugly if it is ugly, else return not ugly

Hint:

An ugly number U can be expressed as: U = 2^a * 3^b * 5^c, where a, b and c are nonnegative integers.

def checkUgly(n):
    while (n%2==0):
        n//=2
    while (n%3==0):
        n//=3
    while (n%5==0):
        n//=5
    if(n==1):
        return 'ugly'
    else:
        return 'not ugly'
    
