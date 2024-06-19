Two string values S1, S2 are passed as the input. The program must print first N characters present in S1 which are also present in S2.

Input Format:

The first line contains S1.
The second line contains S2.
The third line contains N.

Output Format:

The first line contains the N characters present in S1 which are also present in S2.

Boundary Conditions:

2 <= N <= 10
2 <= Length of S1, S2 <= 1000

Example Input/Output 1:

Input:

abcbde
cdefghbb
3

Output:

bcd
def find_common_characters(s1,s2,n):
    common=[]
    for char in s1:
        if char in s2 and char not in common:
            common.append(char)
            if len(common)==n:
                break
    return ''.join(common)
s1=input().strip()
s2=input().strip()
n=int(input())
print(find_common_characters(s1,s2,n))
