# FINAL PROJECT: SURVIVE THE QUARTER
# Name: Giuseppe Palermo
# Group: A
# Special feature chosen: D - Difficulty selection
#
# 1. WHAT GOES IN?
# The program reads scenarios_A.csv, a comma-separated file
# containing 14 columns:
# ID, Scenario, OptionA, OptionB, OptionC,
# BudgetA, BudgetB, BudgetC,
# ReputationA, ReputationB, ReputationC,
# FeedbackA, FeedbackB, FeedbackC.
# Each row describes a marketing crisis with three possible decisions.
# Budget and reputation changes are signed integers, such as -800 or 15.
# The player also enters a name, difficulty level and choices A, B or C.
#
# 2. WHAT HAPPENS TO THE INPUT?
# The program loads and shuffles the scenarios, then presents
# one situation per day for up to 10 days.
# Each choice changes the player's budget and reputation.
# The game stops if either reaches zero or after day 10.
#
# 3. WHAT COMES OUT?
# The game displays each decision's consequences, updated budget
# and reputation, the final outcome and the best and worst moves.
# It appends one row per game to results.csv, containing:
# name, budget, reputation, title, date.
# Example: Giuseppe,10000,100,Viral Legend,2026-10-30
#
# 4. WHAT COULD GO WRONG?
# The player might enter something other than A, B or C,
# so the program keeps asking until the choice is valid.
# The CSV file might be missing or contain invalid numbers,
# which could prevent the game from loading correctly.
# The player's reputation might exceed 100,
# so the program limits it to a maximum of 100.
# The budget or reputation might fall to zero or below,
# so the game checks both values and ends immediately.
#
# MY CHOSEN FEATURE:
# Difficulty selection: Easy starts with 15000 euros,
# while Hard starts with 6000 euros.
# I chose this feature because it lets players decide
# how challenging they want the game to be.
# It is also simple to implement and test.

import csv
import random
from datetime import datetime
from pathlib import Path

# Find the scenario file in the same folder as this program.
FOLDER = Path(__file__).parent
SCENARIO_FILE = FOLDER / "scenarios_A.csv"
RESULTS_FILE = FOLDER / "results.csv"


# Load the marketing scenarios from the CSV file.

def load_scenarios(filename):
    scenarios = []

    try:
        with open(filename, "r", encoding="utf-8-sig", newline="") as file:
            reader = csv.DictReader(file)

            required_columns = [
                "ID", "Scenario",
                "OptionA", "OptionB", "OptionC",
                "BudgetA", "BudgetB", "BudgetC",
                "ReputationA", "ReputationB", "ReputationC",
                "FeedbackA", "FeedbackB", "FeedbackC"
            ]

            if not reader.fieldnames or any(
                column not in reader.fieldnames for column in required_columns
            ):
                print("Error: The CSV file has missing columns.")
                return []

            for row in reader:
                try:
                    for choice in "ABC":
                        int(row["Budget" + choice])
                        int(row["Reputation" + choice])
                    scenarios.append(row)
                except (ValueError, TypeError, KeyError):
                    print(f"Warning: Skipping invalid scenario {row.get('ID')}")
                    
    except FileNotFoundError:
        print(f"Error: Scenario file not found: {filename}")
    except (OSError, UnicodeError, csv.Error) as error:
        print(f"Error reading the CSV file: {error}")

    return scenarios



# Calculate how a decision changes the two gauges.
# Return both updated values as a tuple.
def apply_choice(budget, reputation, scenario, choice):
    budget_change = int(scenario["Budget" + choice])
    reputation_change = int(scenario["Reputation" + choice])

    budget += budget_change
    reputation += reputation_change

    return budget, reputation

# Ask the player to choose a difficulty level.
def choose_difficulty():
    while True:
        difficulty = input("Choose difficulty (Easy/Hard): ").strip().lower()

        if difficulty == "easy":
            return 15000
        elif difficulty == "hard":
            return 6000

        print("Please enter Easy or Hard.")


# Display the situation and its three possible choices.
def display_scenario(day, budget, reputation, scenario):
    print(f"\n--- Day {day} ---")
    print(f"Budget: {budget} EUR | Reputation: {reputation}/100")
    print(scenario["Scenario"])

    for letter in ["A", "B", "C"]:
        option = (
            scenario["Option" + letter],
            int(scenario["Budget" + letter]),
            int(scenario["Reputation" + letter]),
            scenario["Feedback" + letter]
        )

        print(f"{letter}: {option[0]}")


# Ask for a valid choice and reject incorrect answers.
def get_player_choice():
    while True:
        choice = input("Your choice (A, B or C): ").strip().upper()

        if choice in ["A", "B", "C"]:
            return choice

        print("Please type A, B or C.")

        # Run the game for up to 10 randomly selected days.
def play_game():
    print("=== SURVIVE THE QUARTER ===")
    name = input("Enter your name: ").strip()

    budget = choose_difficulty()
    reputation = 50
    history = []

    scenarios = load_scenarios(SCENARIO_FILE)

    # Stop safely if the CSV contains no valid scenarios.
    if not scenarios:
        print("No valid scenarios available. Game cannot start.")
        return name, budget, reputation, history
    
    # Do not save a result if the game never started.
    if not history:
        print("No game was played. Nothing will be saved.")
        return
    random.shuffle(scenarios)

    for day, scenario in enumerate(scenarios[:10], start=1):
        display_scenario(day, budget, reputation, scenario)

        choice = get_player_choice()

        # Store the selected option as a tuple.
        option = (
            scenario["Option" + choice],
            int(scenario["Budget" + choice]),
            int(scenario["Reputation" + choice]),
            scenario["Feedback" + choice]
        )

        # Update both gauges using our earlier function.
        budget, reputation = apply_choice(
            budget, reputation, scenario, choice
        )

        # Reputation cannot exceed 100.
        reputation = min(100, reputation)

        # Record the day, option and reputation change.
        history.append((day, option[0], option[2]))

        print(f"\n{option[3]}")
        print(f"Budget: {budget} EUR")
        print(f"Reputation: {reputation}/100")

        # Check whether the player has been fired.
        if budget <= 0:
            print("\nYOU'RE FIRED! The company ran out of money.")
            break

        if reputation <= 0:
            print("\nYOU'RE FIRED! Your reputation collapsed.")
            break

    return name, budget, reputation, history

    # Calculate the player's final score and assign a job title.
def calculate_title(budget, reputation):
    score = reputation + budget // 200

    if score < 95:
        title = "Eternal Intern"
    elif score < 120:
        title = "Growth Hacker"
    elif score < 140:
        title = "CMO Material"
    else:
        title = "Viral Legend"

    return score, title


# Display the final results and the best and worst decisions.
def show_final_results(budget, reputation, history):
    print("\n========== FINAL RESULTS ==========")

    print(f"Final budget: {budget} EUR")
    print(f"Final reputation: {reputation}/100")
    print(f"Days played: {len(history)}")

    if budget <= 0 or reputation <= 0:
        print("Outcome: FIRED")
    elif len(history) == 10:
        print("Outcome: SURVIVED THE QUARTER!")
    else:
        print("Outcome: GAME ENDED EARLY")

    if budget <= 0 or reputation <= 0:
        print("Final result: Fired")
    else:
        score, title = calculate_title(budget, reputation)
        print(f"Final score: {score}")
        print(f"Your title: {title}")

    if history:
        best_move = max(history, key=lambda move: move[2])
        worst_move = min(history, key=lambda move: move[2])

        print("\nBEST DECISION:")
        print(f"Day {best_move[0]}: {best_move[1]}")
        print(f"Reputation change: {best_move[2]:+d}")

        print("\nWORST DECISION:")
        print(f"Day {worst_move[0]}: {worst_move[1]}")
        print(f"Reputation change: {worst_move[2]:+d}")

    print("===================================")

    from datetime import datetime


# Save the player's result without deleting previous games.
def save_results(name, budget, reputation, title):
    file_exists = RESULTS_FILE.exists()

    with open(RESULTS_FILE, "a", encoding="utf-8", newline="") as file:
        writer = csv.writer(file)

        # Write the header only when creating a new file.
        if not file_exists or RESULTS_FILE.stat().st_size == 0:
            writer.writerow(["name", "budget", "reputation", "title", "date"])

        writer.writerow([
            name,
            budget,
            reputation,
            title,
            datetime.now().strftime("%Y-%m-%d")
        ])


# Connect the game, final results and CSV saving.
def main():
    name, budget, reputation, history = play_game()

    show_final_results(budget, reputation, history)

    if budget <= 0 or reputation <= 0:
        title = "Fired"
    else:
        score, title = calculate_title(budget, reputation)

    save_results(name, budget, reputation, title)

    print("\nYour result has been saved to results.csv!")


# Start the game when this Python file is executed.
if __name__ == "__main__":
    main()