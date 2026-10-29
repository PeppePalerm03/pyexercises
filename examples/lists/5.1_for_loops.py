"""Exercise 5.1 — Doing the same thing to every item

WHAT THE PROGRAM MUST DO
    Take the list you built in exercise 4.0 and, for every item, display a line that
    combines the item, its position, and something computed about it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What did you compute for each item, and what does the reader learn from that line?

WHAT THE AI CANNOT KNOW
    Your list from 4.0, and what is worth computing about its items. Length of the name,
    share of a total, position in a ranking, whether the item passes a threshold you set.
    Open your 4.0 file, copy the list across, and say in a comment what you decided.

CHECK IT YOURSELF
    Count the lines your program printed. There must be exactly as many as items in your
    list. If there is one more or one less, you have an off-by-one, and it is worth
    understanding now rather than in the exam.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: A list of 8 annual returns (%) from financial assets.
# 2. Process: Loop through each return, identify its position,
#    and calculate its difference from the average return.
# 3. Out: One line per asset showing its position, return,
#    and difference from the average.
# 4. I compute how far each return is above or below the average.
#    This helps compare the performance of the 8 assets.


# Your code below
returns = [12, 18, 8, 6, 3, 5, 10, 7]

average_return = sum(returns) / len(returns)
for position, annual_return in enumerate(returns, start=1):
    difference = annual_return - average_return
    print(f"Asset {position}: Return = {annual_return}%, Difference from average = {difference:.2f} percentage points")

# This list comes from Exercise 4.0.
# I calculate the average return before the loop.
# The loop goes through each asset and calculates its
# difference from the average return.

# Check it yourself:
# Tested with 8 returns.
# The program printed exactly 8 lines, one per asset.
# The average return was 8.625%.
# The first asset's difference was +3.375 percentage points.
