"""
manager.py

Contains the HabitManager class which handles the creation, deletion, tracking,
and persistence of multiple Habit objects.

Author: Hina Kamal
"""

import json
import os
from habit import Habit


class HabitManager:
    """
    Manages a collection of Habit objects. Supports operations such as adding,
    deleting, completing, saving, and loading habits from persistent storage.

    Attributes:
        habits (list): A list of Habit objects.
    """

    def __init__(self):
        """
        Initializes an empty HabitManager instance.
        """
        self.habits = []

    def add_habit(self, habit: Habit):
        """
        Adds a new habit to the manager.

        Args:
            habit (Habit): The habit object to add.
        """
        self.habits.append(habit)

    def delete_habit(self, habit_name: str):
        """
        Deletes a habit from the list based on its name.

        Args:
            habit_name (str): The name of the habit to delete.
        """
        self.habits = [habit for habit in self.habits if habit.name.lower() != habit_name.lower()]

    def complete_habit(self, habit_name: str):
        """
        Marks a habit as completed.

        Args:
            habit_name (str): The name of the habit to mark as completed.
        """
        for habit in self.habits:
            if habit.name.lower() == habit_name.lower():
                habit.complete()
                return True
        return False

    def get_habit(self, habit_name: str):
        """
        Retrieves a habit by name.

        Args:
            habit_name (str): The name of the habit to retrieve.

        Returns:
            Habit or None: The matching Habit object, or None if not found.
        """
        for habit in self.habits:
            if habit.name.lower() == habit_name.lower():
                return habit
        return None

    def save_to_file(self, file_path='data/habits.json'):
        """
        Saves all current habits to a JSON file.

        Args:
            file_path (str): Path to the file where habits will be saved.
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as f:
            json.dump([habit.to_dict() for habit in self.habits], f, indent=4)

    def load_from_file(self, file_path='data/habits.json'):
        """
        Loads habits from a JSON file and populates the manager.

        Args:
            file_path (str): Path to the file from which habits will be loaded.
        """
        if not os.path.exists(file_path):
            return

        with open(file_path, 'r') as f:
            data = json.load(f)
            self.habits = [Habit.from_dict(item) for item in data]
