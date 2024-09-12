print("WELCOME TO QUIZ GAME YOU HAVE TO ANSWER 5 QUESTION ")
Q1="Q1)What is the capital of France?"
Q2="Q2)What is 2 + 2?"
Q3="Q3)What is the boiling point of water"
QUESTIONS=[Q1,Q2,Q3]
ANSWER=["PARIS","4","100"]
score=0
i=0
for item in QUESTIONS:
    print(item)
    user=input("enter answer for the questions :").upper().strip()
    if user == ANSWER[i].upper():
        score+=1
        i+=1
        print(f"you answered right your score is {score}")
    else:
        print(f"you answer wrong the answer is {ANSWER[i]}")
if score == len(QUESTIONS):
        print(f"you answered all the question right")
else:
     print(f"yor answer {score} question right ")
        
    