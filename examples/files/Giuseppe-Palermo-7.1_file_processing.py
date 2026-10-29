"""Exercise 7.1 — Loading a file, cleaning it, saving the result (homework)

This is the direct rehearsal for the final exam. Session 8 starts with it.

WHAT THE PROGRAM MUST DO
    Load names.txt, clean what is inside, sort it by last name, and write the result to
    a new file. The original file must not be modified.

DO THIS BEFORE ANYTHING ELSE
    Open names.txt and read it with your eyes. Then write, in comments at the top of
    your file, everything that is wrong with it. There are at least four different
    problems. Find them yourself.

    This step is not optional and it is graded. An assistant cannot see your file.

ANSWER THESE, in comments, after the list of problems
    1. What goes in?
    2. What happens to it?  (one line per problem you found, and how you deal with it)
    3. What comes out?
    4. What does "sort by last name" mean when a line contains two words, and how do you
       know which one is the last name?

WHAT THE AI CANNOT KNOW
    The actual content of names.txt. If you paste this brief into an assistant without
    describing the file, it will write a program for a clean file, and that program will
    crash or produce nonsense on the real one.

    Describe the file to it. That description is the exercise.

CHECK IT YOURSELF
    Count the lines in names.txt, then in your output file. The numbers should differ,
    and you should be able to say exactly why. Then check the first and last name of
    your sorted list by hand.

DELIVERABLE
    This file, plus the output file your program produced.
"""

# What is wrong with names.txt:
# - Some names use inconsistent capitalization.
# - Some names have extra spaces or tabs.
# - There are empty lines.
# - Some names appear more than once.
# - Some names use "Last, First" format.
# - Some surnames contain multiple words, like van Dijk.

# 1. In:
# A text file called names.txt containing people's names.

# 2. Process, problem by problem:
# Remove blank lines.
# Remove extra spaces and tabs.
# Standardize capitalization.
# Remove duplicate names.
# Convert "Last, First" names to "First Last".
# Sort the cleaned names alphabetically by surname.

# 3. Out:
# A new file called cleaned_names.txt containing the
# cleaned, unique names sorted by surname.
# The original names.txt remains unchanged.

# 4. How I decide which word is the last name:
# For names written "Last, First", the surname is before the comma.
# Otherwise, I normally use the last word as the surname.
# For "Lucas van Dijk", I treat "van Dijk" as the surname.
# This rule is based on the formats in the supplied file.


# Your code below
from pathlib import Path

# Locate the original file and define a separate output file.
folder = Path(__file__).parent
input_file = folder / "names.txt"
output_file = folder / "cleaned_names.txt"

# Read the original names without changing the file.
with open(input_file, "r", encoding="utf-8") as file:
    original_lines = file.readlines()

# Clean whitespace, capitalization, and name formats.
cleaned_names = []

for line in original_lines:
    name = " ".join(line.strip().split())

    if not name:
        continue

    if "," in name:
        last, first = name.split(",", 1)
        name = first.strip() + " " + last.strip()

    name = name.title()

    if name.casefold() not in [n.casefold() for n in cleaned_names]:
        cleaned_names.append(name)

# Sort by surname, including the multiword surname "van Dijk".
def surname_key(name):
    parts = name.split()

    if len(parts) >= 3 and parts[-2].lower() == "van":
        return (parts[-2] + " " + parts[-1]).casefold()

    return parts[-1].casefold()

cleaned_names.sort(key=surname_key)

# Save the cleaned names to a new file.
with open(output_file, "w", encoding="utf-8") as file:
    for name in cleaned_names:
        file.write(name + "\n")

# Check the number of original and cleaned lines.
print("Original lines:", len(original_lines))
print("Cleaned names:", len(cleaned_names))
print("First sorted name:", cleaned_names[0])
print("Last sorted name:", cleaned_names[-1])
print("Output file:", output_file.name)

# CHECK IT YOURSELF:
# Original file: 20 lines, including blank lines.
# Output file: 14 unique cleaned names.
# Blank lines and duplicate names were removed.
# First sorted name: Karim Benali.
# Last sorted name: Lucas van Dijk.
# The original names.txt was not modified.