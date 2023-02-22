#Motor Vehicle Administration

#correct answers
correctAns = ["A", "B", "D", "A", "B", "B", "B", "C", "C", "D"]

#Dictionary of Scores and Student IDs
stuScore={}

while True:
    #ask for ID of Student
    stuID = input("Enter Student ID, Enter 0 to exit:\n")
    if stuID == "0":
        break
    answers = []
    for m in range(10):
        ans = input(f"Question {m+1}: ")
        while ans.upper() not in ["A", "B", "C", "D"]:
            print("Please Enter a valid option (A, B, C, or D)")
            ans = input(f"Question {m+1}: ")
        answers.append(ans.upper())
            
    score = 0
    for m in range(10) :
        if answers[m] == correctAns[m]:
            score += 1
    stuScore[stuID] = score
    
passC = 0
for stuID, score in stuScore.items():
    if score >= 8:
        result = "Pass"
        passC += 1
    else:
        result = "Fail"
    print(f"ID: {stuID} Correct: {score} Wrong: {10-score} Pass/Fail: {result}")
    
totalStu = len(stuScore)
percent_pass = (passC / totalStu) * 100
print(f"{percent_pass:.1f}% of students passed the test.")