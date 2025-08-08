questions = ("How many elements are in periodic table:?",
             "Which animal lays largest eggs?:",
             "What is the most abundant gas on earth's atmosphere?:",
             "How many bones are in human body?:",
             "Which is the hotest planet in our solar system?:")

options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Crocodile","C. Elephant","D. Ostrich"),
           ("A. N","B. O","C. CO₂","D. H" ),
           ("A. 206","B. 207","C. 208","D. 209"),
           ("A. Mercury","B. Venus","C. Earth","D. Mars"))


answers = ("C","D","A","A","A")
guesses =[]
score = 0
question_number = 0


for question in questions:
    print("-----------------------------------------------")
    print(question)
    for option in options[question_number]:
        print(option)

    guess = input("Enter (A,B,c,D):").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRCECT")
        print(f"{answers[question_number]} is the correct answer")

    question_number += 1

print("-----------------------")
print("       RESULTS         ")
print("-----------------------")

print("answers:",end="")
for answer in answers:
    print(answer, end="")
print()

print("Guesses:",end="")
for guess in guesses:
    print(guess, end="")
print()

score = int(score/ len(questions)*100)
print(f"Your score is:{score}%")