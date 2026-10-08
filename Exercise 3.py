"""Exercise 3.0 — Computing with what the user typed

WHAT THE PROGRAM MUST DO
    Ask for two numbers and display the result of the four operations.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What should your program do when the second number is zero? Decide, write your
       decision down, and only then implement it.

WHAT THE AI CANNOT KNOW
    Your answer to question 4. There are at least three defensible ones: refuse the
    value and ask again, display a message instead of a result, or stop the program.
    Pick one and be able to defend it.

CHECK IT YOURSELF
    Compute 7 divided by 2 in your head. Run your program with 7 and 2. If your program
    shows 3, it is not wrong by accident: find out why, and write the reason in a comment.
    Then run it with 0 as the second number.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user enters two numbers.
# 2. Process: The program adds, subtracts, multiplies and divides them.
# 3. Out: The results of the four operations.
# 4. If the second number is zero, the program displays
# a message explaining that division by zero is impossible.

# Your code below
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print("Addition:", number1 + number2)
print("Subtraction:", number1 - number2)
print("Multiplication:", number1 * number2)

if number2 != 0:
    print("Division:", number1 / number2)
else:
    print("Division by zero is not possible.")

    # Testing observations:
# Test 1: With 7 and 2, all four operations worked correctly.
# Division returned 3.5 because / performs regular division.
# Using // would return 3.0 because it performs floor division.
# Test 2: With 7 and 0, the program displayed a message
# instead of dividing by zero, as intended.