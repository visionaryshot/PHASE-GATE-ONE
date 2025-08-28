#Ask for number of students and subjects
#Store scores in 2D array
#Collect scores for each student
#Calculate totals and averages
#Ranking: get positions
#Display student results

students = int(input("How many Student do you have?: "))
subjects = int(input("How many Subject do they offer?:"))
scores = []


for counter in range(students):
    print(f"Student {counter + 1}")
    student_scores = []
    for sub in range(subjects):
        while True:
            score = int(input(f"Score for Subject {sub + 1}: "))
            if score == 0 and score == 100:
	    
                student_scores.append(score)
                break
            else:
                print("invalid input. Score must be between 0 - 100")
    scores.append(student_scores)

totals = [sum(row) for row in scores]
averages = [total / subjects for total in totals]

positions = []
for count in range(students):
    levels = 1
    for countee in range(students):
        if totals[countee] > totals[count]:
            levels += 1
    positions.append(levels)

