
# Exercise 7.0 - AI Tutor Conversation Summary

## AI tutor used
ChatGPT (OpenAI)

## Purpose
I used ChatGPT as a tutor to help me complete Exercise 7.0, understand file processing in Python and test my program.

## My decisions
I chose to create a finance-related program that records investment transactions.

I selected five columns:
- Asset
- Type
- Quantity
- Price
- Date

I wanted the program to save purchases and sales of financial assets so I could later analyze my investment activity.

I decided that:
- The CSV should have one header, created only when needed.
- New transactions should be added without deleting previous records.
- Invalid inputs should be rejected and the user asked to try again.

## How ChatGPT helped
ChatGPT helped me:
- Plan the program and answer the four questions.
- Write and organize the Python code.
- Understand input validation and error handling.
- Use the csv, pathlib and math libraries.
- Check indentation and correct mistakes.
- Test the program and verify the CSV output.

## Testing
I ran the program three times with different transactions:
1. Apple - Buy - 10 units - 150 - 2026-10-22
2. Microsoft - Buy - 5 units - 420 - 2026-10-21
3. Tesla - Sell - 3 units - 250 - 2026-10-20

I opened investment_transactions.csv and confirmed that it contained exactly one header and three transaction rows.

The program preserved previous transactions and successfully appended new ones.

## What I learned
I practiced collecting user input, validating values, using loops and handling errors.

I also learned how to create a CSV file, write its header once and append new rows without overwriting existing data.

## Final result
The program ran successfully and passed the required three-run test.

This document summarizes my AI-assisted work rather than reproducing the complete conversation.

---

# Exercise 7.1 — AI Tutor Conversation Summary

## AI tutor used
ChatGPT (OpenAI)

## Purpose
I used ChatGPT as a tutor to understand how to read, clean, sort and save data from a text file using Python.

## Problems identified in names.txt
- Inconsistent capitalization.
- Extra spaces and tabs.
- Empty lines.
- Duplicate names.
- Different name formats, including "Last, First".
- Multiword surnames such as "van Dijk".

## My decisions
I decided to:
- Remove blank lines and unnecessary spaces.
- Standardize capitalization.
- Remove duplicate names.
- Convert names written as "Last, First" into "First Last".
- Sort names alphabetically by surname.
- Save the results in a separate file without modifying the original.

## How ChatGPT helped
ChatGPT helped me:
- Understand the assignment requirements.
- Identify problems in the original file.
- Develop the Python program.
- Understand file reading, string cleaning and sorting.
- Resolve a FileNotFoundError caused by the input filename.
- Verify the output and document the results.

## Testing
I ran the program using the original names.txt file.

Results:
- Original file: 20 lines.
- Cleaned output: 14 unique names.
- First sorted name: Karim Benali.
- Last sorted name: Lucas van Dijk.
- Output file: cleaned_names.txt.

The program successfully created the cleaned file without modifying the original.

## What I learned
I practiced reading and writing text files, using loops, removing duplicates and sorting data with a custom function.

I also learned how to troubleshoot file paths and handle inconsistent data formats.

## Final result
The program ran successfully and produced the expected cleaned output.

This section summarizes my AI-assisted work rather than reproducing the complete conversation.