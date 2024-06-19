Given an array of names of candidates in an election. A candidate name in the array represents a vote cast to the candidate. Print the name of candidates received Max vote. If there is tie, print a lexicographically smaller name.

Examples: 

Input :  votes[] = {"john", "johnny", "jackie",

                    "johnny", "john", "jackie",

                    "jamie", "jamie", "john",

                    "johnny", "jamie", "johnny",

                    "john"};

Output : John

We have four Candidates with name as 'John', 'Johnny', 'jamie', 'jackie'. The candidates John and Johny get maximum votes. Since John is alphabetically smaller, we print it. Use dictionary to solve the above problem

 

Sample Input:

10

John

John

Johny

Jamie

Jamie

Johny

Jack

Johny

Johny

Jackie

 

Sample Output:

Johny
n=int(input())
l=[]
while len(l)<n:
    l.append(input())
a=[]
for i in l:
    c=l.count(i)
    a.append(c)
b=max(a)
x=[]
for i in l:
    c=l.count(i)
    if(c==b):
        x.append(i)
x=set(x)
print(min(x))
