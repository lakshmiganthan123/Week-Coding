Assume that the given string has enough memory.

 

Don't use any extra space(IN-PLACE)

 

Sample Input 1

 

a2b4c6

 

Sample Output 1

 

aabbbbcccccc

ip=input()
exp=''
i=0
while i<len(ip): 
    char=ip[i]
    count=''
    i+=1
    while i<len(ip) and ip[i].isdigit():
        count+=ip[i]
        i+=1
    count=int(count)
    exp+=char*count
print(exp)
