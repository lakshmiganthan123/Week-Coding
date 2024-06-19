Coders here is a simple task for you, Given string str. Your task is to check whether it is a binary string or not by using python set.

Examples:  

Input: str = "01010101010"

Output: Yes



Input: str = "REC101"

Output: No

a=input()
x=0
for i in a:
    if i=="1" or i=="0":
        x+=1
b=len(a)
if(x==b):
    print("Yes")
else:
    print("No")
