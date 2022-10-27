# read if ulser is saying yes or no
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response =="n":
            response = "no"
            return response
        else:
            print("Please enter yes or no ")
# shows instructions to ulsers
def instructions():
    print("*** How to play ***\n")
    print("""when your given a questions answer with A B C or D\n""")
    return ""
# starts a new game
def start_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# checks if the answer is right
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("Incorrect!")
        return 0

# displays the score to the ulser at end of quiz
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# asks if the ulser if they want to play again
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# asks if you have played before
played_before = yes_no("Have you takin this quiz before? ")
if played_before == "no":
    instructions()

questions = {
 "what is 11 x 6?: ": "A",
 "what is 6 + 91?: ": "B",
 "what is 345 + 123?: ": "C",
 "what is 50% of 642?: ": "A",

 "what is 11 x 7?: ": "B",
 "what is 89 + 61?: ": "C",
 "what is 245 x 2?: ": "A",
 "what is 10% of 100?: ": "D"
}

options = [["A. 66", "B. 69", "C. 6543", "D. none of the above"],
          ["A. 88", "B. 97", "C. 20", "D. 43"],
          ["A.  469", "B. 2543", "C. 468", "D. 355"],
          ["A. 321","B. 532", "C. 124", "D. 98"],

          ["A. 78", "B. 77", "C. 76", "D. none of the above"],
          ["A. 867", "B. 124", "C. 150", "D. 143"],
          ["A.  490", "B. 643", "C. 468", "D. 334"],
          ["A. 33","B. 12", "C. 14", "D. 10"]]

start_game()

while play_again():
    new_game()

print("thx for taking me quiz!")

# -------------------------
