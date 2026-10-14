"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of 8 annual returns from financial assets.
# 2. Process: Select an item, sort the returns, and calculate their average.
# 3. Out: The full list, one return, the sorted list, and the average.
# 4. My list contains annual returns (%) of 8 financial assets.
#    I computed the average return to compare their performance.


# Your code below
returns = [12, 18, 8, 6, 3, 5, 10, 7]

print("Annual returns (%):", returns)

print("First asset return (%):", returns[0])
print("Third asset return (%):", returns[2])
sorted_returns = sorted(returns)

print("Sorted annual returns (%):", sorted_returns)
average_return = sum(returns) / len(returns)

print("Average annual return (%):", average_return)
first_three = returns[:3]

check_average = sum(first_three) / len(first_three)

print("Average of first 3 returns (%):", check_average)