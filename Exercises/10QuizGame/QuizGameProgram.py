questions = ("How many elements are in the periodic table?",
             "Which animal is the biggest on planet Earth?",
             "How many colors in the rainbow?")
options = (("A. 116", "B. 117", "C. 118"),
           ("A. Elephant", "B. Lion", "C. Blue Whale"),
           ("A. 9", "B. 7", "C. 12"))
answers = ("B", "C", "B")
score = 0
question_num = 0

for question in questions:
    print("=====================")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter your answer(A,B,C): ").upper()
    if guess == answers[question_num]:
        score += 10
        print("Correct Answer! Score increased by 10 point!")
    else:
        print("Wrong Answer!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("========================")
print(f"    Your score: {score}/30")
print("========================")
