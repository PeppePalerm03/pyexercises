"""Exercise 3.1 — Odd or even (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a number N, then say for every number from 1 to N whether it is
    odd or even.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should happen if the user types 0, a negative number, or 5000?
       Decide the three behaviours before writing anything.

WHAT THE AI CANNOT KNOW
    Your three decisions. An assistant asked for "odd or even from 1 to N" will produce
    a program that behaves absurdly on 0 and on -4, and will happily print five thousand
    lines. Those are your calls, not its.

CHECK IT YOURSELF
    Run it with 6. You should see three odd and three even. Count them.
    Then run it with your three edge cases and confirm each does what you decided.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user enters a whole number N.
# 2. Process: The program checks every number from 1 to N
# to determine whether it is odd or even.
# 3. Out: A list showing whether each number is odd or even.
# 4. If N is 0 or negative, the program displays an error message.
# If N is greater than 100, it displays a message explaining
# that the maximum allowed number is 100.


# Your code below

N = int(input("Enter a whole number: "))
if N <= 0:
    print("Please enter a positive number.")

elif N > 100:
    print("The maximum allowed number is 100.")

else:
    for number in range(1, N + 1):
        if number % 2 == 0:
            print(number, "is even")
        else:
            print(number, "is odd")