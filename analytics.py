"""
analytics.py

Provides pure functional programming utilities for analyzing Habit data.
These functions operate on collections of Habit objects to extract insights.

Author: Hina Kamal
"""

from typing import List
from habit import Habit


def list_all_habits(habits: List[Habit]) -> List[str]:
    """
    Returns the names of all currently tracked habits.

    Args:
        habits (List[Habit]): List of Habit objects.

    Returns:
        List[str]: List of habit names.
    """
    return [habit.name for habit in habits]


def filter_by_periodicity(habits: List[Habit], periodicity: str) -> List[str]:
    """
    Filters habits by periodicity (daily or weekly).

    Args:
        habits (List[Habit]): List of Habit objects.
        periodicity (str): 'daily' or 'weekly'.

    Returns:
        List[str]: Names of habits with the given periodicity.
    """
    return [habit.name for habit in habits if habit.periodicity.lower() == periodicity.lower()]


def longest_streak(habits: List[Habit]) -> int:
    """
    Finds the longest habit streak across all habits.

    Args:
        habits (List[Habit]): List of Habit objects.

    Returns:
        int: The highest streak value found.
    """
    if not habits:
        return 0
    return max(habit.get_streak() for habit in habits)


def longest_streak_by_habit(habit: Habit) -> int:
    """
    Finds the longest streak for a specific habit.

    Args:
        habit (Habit): A Habit object.

    Returns:
        int: The longest streak for that habit.
    """
    return habit.get_streak()
