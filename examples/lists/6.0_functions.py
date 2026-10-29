"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of annual investment returns (percentages).
# 2. Process: Calculate the sum of returns and divide by the number of returns.
# 3. Out: The arithmetic average annual return as a percentage.
# 4. My function name: calculate_average_return.
# The name clearly describes what the function calculates.
# Return makes the result reusable in other calculations.
# Print only displays the result on screen.
# An empty list returns 0 to avoid division by zero.
# This is a chosen convention, not an actual observed return.

# Your code below

def calculate_average_return(returns):
    if len(returns) == 0:
        return 0
    return sum(returns) / len(returns)

# Original list from Exercise 4.0
returns = [12, 18, 8, 6, 3, 5, 10, 7]

# Call the function three times with different inputs
print("Average of all returns:", calculate_average_return(returns))
print("Average of first 3 returns:", calculate_average_return(returns[:3]))
print("Average of last 3 returns:", calculate_average_return(returns[-3:]))

# Test with an empty list
print("Average of empty list:", calculate_average_return([]))

# CHECK IT YOURSELF:
# Input: []
# Result: 0
# This behavior is acceptable for this exercise because it
# prevents division by zero. However, 0 is a convention,
# not the mathematical average of an empty list.
