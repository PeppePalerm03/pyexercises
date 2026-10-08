"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which two pieces of information did you choose, and for what purpose?
       Imagine a real form in your future job. Not "name and age" unless you can
       say what you would do with them.

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user enters an initial investment amount and an annual interest rate.
# 2. Process: The program calculates the investment value after one year.
# 3. Out: A sentence displaying the initial investment and its value after one year.
# 4. My two fields, and what I would do with them:
# Initial investment (EUR) and annual interest rate (%).
# A financial advisor could use them to estimate investment growth.

# Your code below

investment = float(input("Enter your initial investment in EUR: "))
interest_rate = float(input("Enter the annual interest rate (%): "))

final_value = investment * (1 + interest_rate / 100)

print(f"An investment of EUR {investment:.2f} at an annual interest rate of {interest_rate}% will be worth EUR {final_value:.2f} after one year.")

# Testing observations:
# Test 1: Empty input caused a ValueError.
# Test 2: A single space caused a ValueError.
# Test 3: Entering "hello" caused a ValueError.
# These inputs cannot be converted into numbers using float().

# Adding 1 directly to input() causes a TypeError because input() returns a string.
# Using float() converts the input into a number, allowing calculations.