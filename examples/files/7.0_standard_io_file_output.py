"""Exercise 7.0 — Collecting data and saving it

WHAT THE PROGRAM MUST DO
    Ask the user for the information needed to record one entry, then save it to a CSV
    file. Running the program twice must produce two entries, not overwrite the first.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?  (name your file, and list your columns)
    4. Which columns did you choose, and what would you actually do with this file once
       it has two hundred rows in it?

WHAT THE AI CANNOT KNOW
    Your columns. They must be the ones you would really need to collect for a purpose
    you can state. See 7.0_student_data.csv for the shape of a header line, not for
    the columns to use.

    Two behaviours are yours to decide, and an assistant will guess them wrong:
    what happens the very first time, when the file does not exist yet and needs its
    header line, and what happens when a value the user typed is not acceptable.

CHECK IT YOURSELF
    Run your program three times with different values. Then open the file and count
    the lines. You should have three entries and exactly one header line. If you have
    three header lines, or one entry, your program is wrong.

DELIVERABLE
    This file, plus the CSV your program produced.
"""

# 1. In:
# The user enters an asset name, transaction type (Buy or Sell),
# quantity, price per unit, and transaction date.

# 2. Process:
# The program checks that the inputs are valid.
# It creates a CSV file with headers if the file does not exist.
# It then adds each transaction as a new row without deleting previous data.
# Invalid inputs are rejected and the user is asked to try again.

# 3. Out, file name and columns:
# File: investment_transactions.csv
# Columns: Asset, Type, Quantity, Price, Date

# 4. Why these columns, and what this file is for:
# These columns allow me to record purchases and sales of financial assets.
# With 200 transactions, I could analyze trading activity,
# calculate transaction values, and review my investment history.


# Your code below

# Import libraries to save transactions and check the file.
import csv
import math
from pathlib import Path

# Define the output file and its column names.
file_path = Path(__file__).with_name("investment_transactions.csv")
columns = ["Asset", "Type", "Quantity", "Price", "Date"]

# Ask for the asset name and reject empty answers.
asset = input("Enter asset name: ").strip()

while not asset:
    print("Asset name cannot be empty.")
    asset = input("Enter asset name: ").strip()

# Ask whether the transaction is a purchase or sale.
transaction_type = input("Enter transaction type (Buy/Sell): ").strip().capitalize()

while transaction_type not in ["Buy", "Sell"]:
    print("Please enter Buy or Sell.")
    transaction_type = input("Enter transaction type (Buy/Sell): ").strip().capitalize()

    # Ask for a positive quantity and reject invalid inputs.
while True:
    try:
        quantity = float(input("Enter quantity: "))
        if math.isfinite(quantity) and quantity > 0:
            break
        print("Quantity must be greater than zero.")
    except ValueError:
        print("Please enter a valid number.")

# Ask for a positive price and reject invalid inputs.
while True:
    try:
        price = float(input("Enter price per unit: "))
        if math.isfinite(price) and price > 0:
            break
        print("Price must be greater than zero.")
    except ValueError:
        print("Please enter a valid number.")

        # Ask for a date and check that it follows YYYY-MM-DD.
from datetime import datetime

while True:
    date = input("Enter transaction date (YYYY-MM-DD): ").strip()

    try:
        valid_date = datetime.strptime(date, "%Y-%m-%d")
        if valid_date.strftime("%Y-%m-%d") == date:
            break
        print("Please use the YYYY-MM-DD format.")
    except ValueError:
        print("Invalid date. Please use YYYY-MM-DD.")

        # Check whether the CSV already exists and contains data.
write_header = not file_path.exists() or file_path.stat().st_size == 0

# Open the CSV in append mode to preserve previous transactions.
with open(file_path, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)

    # Write the column names only when the file is new or empty.
    if write_header:
        writer.writerow(columns)

    # Save the transaction as one new row.
    writer.writerow([asset, transaction_type, quantity, price, date])

# Confirm that the transaction was saved.
print("Transaction saved successfully!")
print("File:", file_path.name)

# Check it yourself - Test results:
# I ran the program three times with different transactions.
# I opened investment_transactions.csv and checked the results.
# The file contains exactly one header and three transaction rows.
# Each new transaction was added without overwriting previous data.
# The test passed successfully.