"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The list of 8 annual financial asset returns from Exercise 4.0.
# 2. Process: Reorder the list in four ways without changing the original.
# 3. Out: Four reordered lists and the unchanged original list.
# 4. My four orders are ascending, descending, reversed, and
#    ascending using sort() on a copy.
#    sorted() and slicing create new lists.
#    sort() modifies a list in place, but I apply it to a copy.


# Your code below

returns = [12, 18, 8, 6, 3, 5, 10, 7]

print("Original returns (%):", returns)
ascending = sorted(returns)

print("Ascending order (%):", ascending)
descending = sorted(returns, reverse=True)

print("Descending order (%):", descending)
reversed_returns = returns[::-1]

print("Reversed order (%):", reversed_returns)
copied_returns = returns.copy()

copied_returns.sort()

print("Sorted copy (%):", copied_returns)
print("Original list unchanged (%):", returns)