To find the frequency of numbers in a list and display in sorted order.

Constraints: 

1<=n, arr[i]<=100 

Input: 

1 68 79 4 90 68 1 4 5 

output:

 1 2

 4 2

 5 1

 68 2

 79 1 

90 1

nums=list(map(int,input().split()))
fre={}
for num in nums:
    if num in fre:
        fre[num]+=1
    else:
        fre[num]=1
sortfre=dict(sorted(fre.items()))
for num,freq in sortfre.items():
    print(f"{num} {freq}")
