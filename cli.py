"""
cli.py

This file provides the main command-line interface for interacting with the habit tracker.
It connects user input to core logic from the Habit, HabitManager, and analytics modules.

Author: Hina Kamal
"""

from manager import HabitManager
from habit import Habit
import analytics


def display_menu():
    """
    Displays the main menu of options.
    """
    print("\n--- Habit Tracker Menu ---")
    print("1. View all habits")
    print("2. View habits by periodicity")
    print("3. Add a new habit")
    print("4. Delete a habit")
    print("5. Complete a habit")
    print("6. View longest streak (overall)")
    print("7. View longest streak for a habit")
    print("8. Save and Exit")


def main():
    """
    Main function to run the Habit Tracker CLI.
    """
    manager = HabitManager()
    manager.load_from_file()

    while True:
        display_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == '1':
            all_habits = analytics.list_all_habits(manager.habits)
            print("All Habits:", all_habits or "No habits found.")

        elif choice == '2':
            period = input("Enter periodicity (daily/weekly): ").strip()
            result = analytics.filter_by_periodicity(manager.habits, period)
            print(f"{period.title()} Habits:", result or "No matching habits found.")

        elif choice == '3':
            name = input("Enter the name of the new habit: ").strip()
            period = input("Enter the periodicity (daily/weekly): ").strip()
            new_habit = Habit(name, period)
            manager.add_habit(new_habit)
            print(f"Habit '{name}' added.")

        elif choice == '4':
            name = input("Enter the name of the habit to delete: ").strip()
            manager.delete_habit(name)
            print(f"Habit '{name}' deleted.")

        elif choice == '5':
            name = input("Enter the name of the habit to complete: ").strip()
            if manager.complete_habit(name):
                print(f"Habit '{name}' marked as complete.")
            else:
                print(f"Habit '{name}' not found.")

        elif choice == '6':
            streak = analytics.longest_streak(manager.habits)
            print(f"The longest streak across all habits is: {streak}")

        elif choice == '7':
            name = input("Enter the name of the habit: ").strip()
            habit = manager.get_habit(name)
            if habit:
                streak = analytics.longest_streak_by_habit(habit)
                print(f"The longest streak for '{name}' is: {streak}")
            else:
                print(f"Habit '{name}' not found.")

        elif choice == '8':
            manager.save_to_file()
            print("Habits saved. Exiting...")
            break

        else:
            print("Invalid input. Please enter a number from 1 to 8.")


if __name__ == "__main__":
    main()
