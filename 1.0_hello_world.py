"""Exercise 1.0 — Hello World

WHAT THE PROGRAM MUST DO
    Display a message of your choice, five times, with each line numbered.

ANSWER THESE FIRST, in comments at the top of your file, before any code
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What message did you choose, and why that one?

WHAT THE AI CANNOT KNOW
    The message is yours. Choose something you would actually want a program to say,
    not "Hello, World!". Your comment has to justify it.

CHECK IT YOURSELF
    Count the lines your program produced. Five, not four and not six.
    Then change the number to 3 and run it again. If you had to rewrite more than one
    character, your program is not built the way it should be.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:message "I love finance"
# 2. Process:use a loop to repeat the message 5 times
# 3. Out: 5 lines showing the same message with a number at the beginning of the line
# 4. My message, and why: "I love finance" because it is interesting


# Your code below
message = "I love finance"
for i in range(5):
    print(f"{i + 1}, {message}")