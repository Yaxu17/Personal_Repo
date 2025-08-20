import random

dice_art = {
    1: (
        "┌───────────┐",
        "│           │",
        "│     ●     │",
        "│           │",
        "└───────────┘",
    ),
    2: (
        "┌───────────┐",
        "│ ●         │",
        "│           │",
        "│         ● │",
        "└───────────┘",
    ),
    3: (
        "┌───────────┐",
        "│ ●         │",
        "│     ●     │",
        "│         ● │",
        "└───────────┘",
    ),
    4: (
        "┌───────────┐",
        "│ ●       ● │",
        "│           │",
        "│ ●       ● │",
        "└───────────┘",
    ),
    5: (
        "┌───────────┐",
        "│ ●       ● │",
        "│     ●     │",
        "│ ●       ● │",
        "└───────────┘",
    ),
    6: (
        "┌───────────┐",
        "│ ●       ● │",
        "│ ●       ● │",
        "│ ●       ● │",
        "└───────────┘",
    ),
}

dice = []
total = 0
num_of_dice = int(input("How many dice do you want to roll? "))

# Roll dice
for _ in range(num_of_dice):
    dice.append(random.randint(1, 6))

# Print dice side by side
for line in range(5):  # Each die art has 5 lines
    for die in dice:
        print(dice_art[die][line], end="  ")
    print()  # Newline after each row of dice

# Calculate and print total
total = sum(dice)
print(f"\nTotal: {total}")