"""Exercise 2.1 — Transforming text (homework)

WHAT THE PROGRAM MUST DO
    Ask the user for a sentence, then display four different transformations of it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four transformations did you choose, and in what situation would each of
       them be useful? One line each.

WHAT THE AI CANNOT KNOW
    Your four transformations. Pick them yourself. Open ../examples/strings/string_methods.py
    to see what is available, then choose, then justify.

    A transformation that produces the same thing as another one does not count as two.

CHECK IT YOURSELF
    Run it with a sentence that has spaces at both ends and a capital in the middle.
    For each of your four results, say in a comment whether it is what you expected.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user enters a sentence.
# 2. Process: The program applies four different text transformations.
# 3. Out: Four transformed versions of the original sentence.
# 4. My four transformations, and when each is useful:
# upper(): Converts text to uppercase, useful for report headings.
# lower(): Converts text to lowercase, useful for standardizing data.
# strip(): Removes spaces at both ends, useful for cleaning input.
# replace(): Replaces specific words, useful for correcting terminology.

# Your code below
sentence = input("Enter a sentence: ")

print("Uppercase:", sentence.upper())
print("Lowercase:", sentence.lower())
print("Without outer spaces:", sentence.strip())
print("Replace investment with portfolio:", sentence.replace("investment", "portfolio"))

# Testing observations:
# 1. upper(): All letters became uppercase, as expected.
# 2. lower(): All letters became lowercase, as expected.
# 3. strip(): Only the outer spaces were removed, as expected.
# 4. replace(): "investment" became "portfolio", as expected.