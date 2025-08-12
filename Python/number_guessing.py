import random

Lowest_num = 1
Highest_num = 100
answer = random.randint(Lowest_num, Highest_num)
guesses = 0
is_running = True
print("Number Guessing Game")
print(f"Select a number between {Lowest_num} and {Highest_num}")

while is_running:

    guess =  input("enter your guess:")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < Lowest_num or guess > Highest_num:
            print(f"Select a number between {Lowest_num} and {Highest_num}")
        elif guess < answer:
            print("Too low!")
        elif guess > answer:
            print("Too high!")
        else:
            print(f"Congratulations! You've guessed the number {answer} in {guesses} attempts.")
            is_running = False
    else:
        print("Invalid guess")
        print(f"Select a number between {Lowest_num} and {Highest_num}")