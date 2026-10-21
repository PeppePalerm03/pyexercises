"""Exercise 6.1 — Small functions working together

WHAT THE PROGRAM MUST DO
    Write three small functions, each doing one thing, and a fourth that uses the other
    three to answer one question about your data.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?  (say which function does what, in order)
    3. What comes out?
    4. What question does your fourth function answer, and why does splitting it into
       three make it easier to check?

WHAT THE AI CANNOT KNOW
    Your question and your split. Ask an assistant for "three functions" and it will
    invent three; they will not be the three your question needs. Decide the split first,
    on paper, then ask.

    One function, one job. If you cannot describe what one of yours does in a single
    sentence without using the word "and", it is doing two things.

CHECK IT YOURSELF
    Test each of the three small functions on its own before combining them. Write in a
    comment the input and expected output you used for each. That is three test cases,
    and they are part of the deliverable.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of annual investment returns (percentages).

# 2. Process, function by function:
# Function 1 calculates the average return.
# Function 2 counts returns above a given threshold.
# Function 3 calculates the total number of returns.
# Function 4 combines the other three functions.

# 3. Out: The number of returns above average,
# the average return, and the total number of returns.

# 4. The question my fourth function answers:
# How many annual returns are above the average?
# Splitting the work into three functions makes testing easier
# because each function has one specific responsibility.


# Your code below
def calculate_average(returns):
    if len(returns) == 0:
        return 0
    return sum(returns) / len(returns)


def count_above_threshold(returns, threshold):
    count = 0
    for value in returns:
        if value > threshold:
            count += 1
    return count


def count_returns(returns):
    return len(returns)
# Original data from Exercise 4.0
returns = [12, 18, 8, 6, 3, 5, 10, 7]

# TEST 1: Input [10, 20, 30] -> Expected average: 20
print("Test 1:", calculate_average([10, 20, 30]))

# TEST 2: Input [5, 10, 15], threshold 10 -> Expected count: 1
print("Test 2:", count_above_threshold([5, 10, 15], 10))

# TEST 3: Input [4, 8, 12, 16] -> Expected count: 4
print("Test 3:", count_returns([4, 8, 12, 16]))

def analyze_returns(returns):
    average = calculate_average(returns)
    above_average = count_above_threshold(returns, average)
    total = count_returns(returns)

    return average, above_average, total
# Analyze the investment returns from Exercise 4.0
average, above_average, total = analyze_returns(returns)

print("\n--- INVESTMENT ANALYSIS ---")
print("Average annual return:", average, "%")
print("Returns above average:", above_average)
print("Total returns analyzed:", total)