The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]
Example 2:

Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
s=input()
x=len(s)
a=[]
for i in range(x):
    y=s[i:i+10]
    for j in range(x):
        z=s[j:j+10]
        if y==z:
            a.append(y)
c=0
f=[]
for i in a:
    c=a.count(i)
    if c>1:
        f.append(i)
f=set(f)
f=sorted(f)
for i in f:
    print(i)
