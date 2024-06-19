String should contain only the words are not palindrome.

 

Sample Input 1

 

Malayalam is my mother tongue

 

Sample Output 1

 

is my mother tongue

s=input()
s=s.lower()
l=s.split()
for i in l:
    if(i!=i[::-1]):
        print(i,end=' ')
        
