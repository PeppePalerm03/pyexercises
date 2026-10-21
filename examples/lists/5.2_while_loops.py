"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user enters a secret word.
# 2. Process: The program checks whether the word is correct.
# 3. Out: A success or failure message and a summary of attempts.
# 4. My stop condition, my attempt limit, my summary:
# Stop when the word is correct or after 5 attempts.
# The summary shows whether the user succeeded and how many attempts were used.


# Your code below
secret_word = "python"
attempts = 0
max_attempts = 5
guessed_correctly = False
while attempts < max_attempts and not guessed_correctly:
    guess = input("Guess the secret word: ")
    guess = guess.strip().lower()

    attempts += 1

    if guess == secret_word:
        guessed_correctly = True
        print("Congratulations! You guessed correctly!")
    else:
        print("Incorrect guess. Try again!")

print("\n--- GAME SUMMARY ---")
print("Total attempts:", attempts)

if guessed_correctly:
    print("Result: You won!")
else:
    print("Result: You lost!")
    print("The secret word was:", secret_word)