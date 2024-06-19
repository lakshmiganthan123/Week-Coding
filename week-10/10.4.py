Given an list, find peak element in it. A peak element is an element that is greater than its neighbors.

An element a[i] is a peak element if

A[i-1] <= A[i] >=a[i+1] for middle elements. [0<i<n-1]

A[i-1] <= A[i] for last element [i=n-1]

A[i]>=A[i+1] for first element [i=0]

Input Format

The first line contains a single integer n , the length of A .
The second line contains n space-separated integers,A[i].

Output Format

Print peak numbers separated by space.

Sample Input

5

8 9 10 2 6

Sample Output

10 6
def findpeak(arr):
    n=len(arr)
    peaks=[]
    for i in range(n):
        if (i==0 and arr[i]>= arr[i+1]) or (i==n-1 and arr[i]>=arr[i-1]) or (0<i<n-1 and arr[i]>= arr[i-1] and arr[i]>=arr[i+1]):
            peaks.append(arr[i])
    return peaks
n=int(input())
arr=list(map(int,input().split()))
peakele=findpeak(arr)
print(" ".join(map(str,peakele)))
