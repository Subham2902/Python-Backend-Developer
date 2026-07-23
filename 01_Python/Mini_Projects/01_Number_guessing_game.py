import random
secret = random.randint(1, 10)

print("Welcome to the  Number Guessing Game! ")
print("Guess a number between 1 and 10.")

while True:
    guess = int(input("Enter your guess : "))

    if guess == secret:
        print( " 🎉 Correct! You guessed it.")
        break
    elif guess < secret :
        print("Too low! Try again.")
    else:
        print("Too high: Try again.")