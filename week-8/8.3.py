Create a student dictionary  for n students with the student name as key and their test mark assignment mark and lab mark as values. Do the following computations and display the result.

1.Identify the student with the  highest average score

2.Identify the student who as the highest Assignment marks

3.Identify the student with the Lowest lab marks

4.Identify the student with the lowest average score

Note:

If more than one student has the same score display all the student names



Sample input:

4

James 67 89 56

Lalith 89 45 45

Ram 89 89 89

Sita 70 70 70

Sample Output:

Ram

James Ram

Lalith

Lalith
n = int(input())
s_dict = {}

for _ in range(n):
    data = input().split()
    name = data[0]
    scores = list(map(int, data[1:]))
    s_dict[name] = scores

#result = student_scores(s_dict)
averages = {name: sum(scores) / len(scores) for name, scores in s_dict.items()}
    # Identify the student with the highest average score
highest_avg_students = [name for name, avg in averages.items() if avg == max(averages.values())]
    # Identify the student with the highest Assignment marks
assign_student = [name for name, scores in s_dict.items() if scores[1] == max([s[1] for s in s_dict.values()])]
   # Identify the student with the lowest lab marks
labmark_student = [name for name, scores in s_dict.items() if scores[2] == min([s[2] for s in s_dict.values()])]
    # Identify the student with the lowest average score
lowest_avg_students = [name for name, avg in averages.items() if avg == min(averages.values())]
# Display the results
#print("\n".join([" ".join(sorted(students)) for students in result]))
labmark_student=sorted(labmark_student)

for i in highest_avg_students:
    print(i,end=" ")
print()
for i in (assign_student):
    print(i,end=" ")
print()
for i in (labmark_student):
    print(i,end=" ")
print()
for i in (lowest_avg_students):
    print(i,end=" ")
