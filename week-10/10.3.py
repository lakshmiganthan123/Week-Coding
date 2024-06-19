Bubble Sort is the simplest sorting algorithm that works by repeatedly swapping the adjacent elements if they are in wrong order. You read an list of numbers. You need to arrange the elements in ascending order and print the result. The sorting should be done using bubble sort.

Input Format: The first line reads the number of elements in the array. The second line reads the array elements one by one.


Output Format: The output should be a sorted list.

a=int(input())
b=input().split()
b= [int(x) for x in b]
b.sort()
for i in b:
    print(i,end=" ")
