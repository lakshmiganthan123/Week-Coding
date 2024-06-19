Reverse a string without affecting special characters
 Given a string S, containing special characters and all the alphabets, reverse the string without affecting the positions of the special characters.
Input:
A&B
Output:
B&A
Explanation: As we ignore '&' and
As we ignore '&' and then reverse, so answer is "B&A".

s=list(input())
i=0
j=len(s)-1
while(i<=j):
    if(s[i].isalpha()):
        while(not s[j].isalpha()):
            j-=1
        s[i],s[j]=s[j],s[i]
    i+=1
print(''.join(s))
