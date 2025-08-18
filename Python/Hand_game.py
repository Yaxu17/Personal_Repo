import random

option =   ("rock", "paper", "scissors")
running = True

while running:
    player = input("Enter your choice (rock, paper, scissors): ")
    computer = random.choice(option)

    while player not in option:
        player = input("Please enter rock, paper, or scissors: ")
    
    print (f"Player : {player}")
    print (f"Computer : {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print("You win!")
    else:
        print("You lose!")

    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        print("Thanks for playing!")
        running = False