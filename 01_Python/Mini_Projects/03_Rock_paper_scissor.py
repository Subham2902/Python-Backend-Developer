import random

choices = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(choices)
    user = input("Enter rock, paper, or scissors: ").lower()

    if user not in choices:
        print("Invalid choice!")
        continue

    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You Win!")
    else:
        print("You Lose!")

    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break