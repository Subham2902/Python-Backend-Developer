questions = {
    "What is the capital of India? ": "delhi",
    "Which keyword is used to create a function in Python? ": "def",
    "What is 5 * 6? ": "30",
    "Which data type stores True or False? ": "bool",
    "Who created Python? ": "guido van rossum"
}

score = 0

print("===== Python Quiz Game =====")

for question, answer in questions.items():
    user_answer = input(question).strip().lower()

    if user_answer == answer:
        print("Correct!\n")
        score += 1
    else:
        print(f"Wrong! Correct answer: {answer}\n")

print(f"Your Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100
print(f"Percentage: {percentage:.2f}%")