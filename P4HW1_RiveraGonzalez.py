# Luis Rivera Gonzalez
# 3/25/2025
# P4HW1
# Use nested loops to get valid grades from user


'''
Pseudocode

Create variable num_scores (int) -> user input number of scores
Create an empty list -> scores_list
for each in range(num_scores)
    score = int(input(f"Enter score # {each+1}"))
    while score is invalid - less than 0 or score greater than 100
        output to user score is invalid
        output to user score must be 0-100
        score = int(input(f"Enter score # {each+1} again"))
    scores_list.append(score)
print scores_list to ensure correctness

Get the lowest score in list -> assign it to a variable
Remove the lowest score from the list

Get average of list after removing lowest score
Use average to determine letter grade
'''

# Get user input (list) and validate it
num_scores = int(input('How many scores do you want to enter? '))
scores_list = []
for each in range(num_scores):
    score = int(input(f"Enter score #{each + 1}: "))
    while score < 0 or score > 100:
        print("INVALID Score entered!!!\nScore should be between 0 and 100")
        score = int(input(f"Enter score #{each + 1} again: "))
    scores_list.append(score)

# Print Results
print()
print(14*'-' + "Results" + 14*'-')
lowest_score = min(scores_list)
print(f"{'Lowest Score':<15} : {lowest_score}")
scores_list.remove(lowest_score)
print(f"{'Modified Score':<15} : {scores_list}")
average_score = sum(scores_list) / len(scores_list)
print(f"{'Score Averages':<15} : {average_score:.2f}")
if average_score >= 90:
 
    print(f"{'Grade':<15} : A")
elif average_score >= 80:
 
     print(f"{'Grade':<15} : B")
elif average_score >= 70:
 
     print(f"{'Grade':<15} : C")
elif average_score >= 60:
 
     print(f"{'Grade':<15} : D")
else:
 
    print(f"{'Grade':<15} : F")
print(36*'-')