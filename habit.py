"""
habit.py

Defines the Habit class using Object-Oriented Programming principles.
This class represents a single habit with tracking capabilities such as completion status,
periodicity, creation date, and history of completions.

Author: Hina Kamal
"""

from datetime import datetime, timedelta


class Habit:
    """
    Represents a user-defined habit that needs to be completed periodically (daily or weekly).
    Tracks completion dates and supports streak calculation.

    Attributes:
        name (str): The title of the habit.
        periodicity (str): The frequency of the habit. Accepts "daily" or "weekly".
        created_at (datetime): Timestamp when the habit was created.
        completed_dates (list): List of datetime objects representing when the habit was completed.
    """

    def __init__(self, name: str, periodicity: str):
        """
        Initializes a new Habit instance.

        Args:
            name (str): The name of the habit.
            periodicity (str): Either "daily" or "weekly".
        """
        self.name = name
        self.periodicity = periodicity.lower()
        self.created_at = datetime.now()
        self.completed_dates = []

    def complete(self):
        """
        Marks the habit as completed for the current date and time.
        """
        now = datetime.now()
        self.completed_dates.append(now)

    def get_streak(self) -> int:
        """
        Calculates the current streak (consecutive periods without missing completion).

        Returns:
            int: Number of consecutive days or weeks the habit has been completed.
        """
        if not self.completed_dates:
            return 0

        # Sort the dates in descending order (latest first)
        sorted_dates = sorted(self.completed_dates, reverse=True)
        streak = 1
        current_date = sorted_dates[0]

        for date in sorted_dates[1:]:
            delta = (current_date - date).days
            if self.periodicity == 'daily' and delta == 1:
                streak += 1
            elif self.periodicity == 'weekly' and 0 < delta <= 7:
                streak += 1
            else:
                break
            current_date = date

        return streak

    def to_dict(self) -> dict:
        """
        Converts the habit object to a dictionary for easy serialization (e.g. JSON storage).

        Returns:
            dict: A dictionary representation of the habit.
        """
        return {
            'name': self.name,
            'periodicity': self.periodicity,
            'created_at': self.created_at.isoformat(),
            'completed_dates': [dt.isoformat() for dt in self.completed_dates]
        }

    @staticmethod
    def from_dict(data: dict):
        """
        Creates a Habit instance from a dictionary (e.g. when loading from JSON).

        Args:
            data (dict): A dictionary with habit attributes.

        Returns:
            Habit: An instance of Habit initialized with provided data.
        """
        habit = Habit(data['name'], data['periodicity'])
        habit.created_at = datetime.fromisoformat(data['created_at'])
        habit.completed_dates = [datetime.fromisoformat(dt) for dt in data['completed_dates']]
        return habit
