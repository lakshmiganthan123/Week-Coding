Write a program to convert strings to an integer and float and display its type.

Sample Input:

10

10.9

Sample Output:

10,<class 'int'>

10.9,<class 'float'>

a=int(input())
b=float(input())
print(a,type(a),sep=",")
print(round(b,1),type(b),sep=",")
