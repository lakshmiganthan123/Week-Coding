Give a dictionary with value lists, sort the keys by summation of values in value list.

 Input : test_dict = {‘Gfg’ : [6, 7, 4], ‘best’ : [7, 6, 5]}

Output : {‘Gfg’: 17, ‘best’: 18}

Explanation : Sorted by sum, and replaced.

 Input : test_dict = {‘Gfg’ : [8,8], ‘best’ : [5,5]}

Output : {‘best’: 10, ‘Gfg’: 16}

Explanation : Sorted by sum, and replaced.

 Sample Input:

2

Gfg 6 7 4

Best 7 6 5

Sample Output

Gfg 17

Best 18
n = int(input())
s_dict = {}

for _ in range(n):
    data = input().split()
    name = data[0]
    scores = list(map(int, data[1:]))
    s_dict[name] = scores

# Function to sort dictionary by summation of values
averages = {name: sum(scores) for name, scores in s_dict.items()}

highest_avg_students = [name for name,avg in averages.items() if avg == max(averages.values())]
lowest_avg_students = [name for name, avg in averages.items() if avg == min(averages.values())]
for i in lowest_avg_students:
    print(i,min(averages.values()))
for i in highest_avg_students:
    print(i,max(averages.values()))
