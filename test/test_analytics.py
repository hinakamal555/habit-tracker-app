"""
test_analytics.py

Unit tests for analytics functions in the analytics module using pytest.
Covers listing habits, filtering, and longest streak logic.
"""

import pytest
from analytics import (
    list_all_habits,
    filter_by_periodicity,
    longest_streak,
    longest_streak_by_habit,
)
from habit import Habit
from datetime import datetime, timedelta

def create_habit(name, period, days):
    """Helper function to create a habit with a given streak."""
    h = Habit(name, period)
    h.completed_dates = [datetime.now() - timedelta(days=i) for i in range(days)]
    return h

def test_list_all_habits():
    """Test that all habit names are listed correctly."""
    habits = [Habit("A", "daily"), Habit("B", "weekly")]
    result = list_all_habits(habits)
    assert result == ["A", "B"]

def test_filter_by_periodicity():
    """Test filtering habits by 'daily' periodicity."""
    habits = [Habit("A", "daily"), Habit("B", "weekly"), Habit("C", "daily")]
    result = filter_by_periodicity(habits, "daily")
    assert result == ["A", "C"]

def test_longest_streak():
    """Test finding the longest streak across multiple habits."""
    h1 = create_habit("H1", "daily", 3)
    h2 = create_habit("H2", "daily", 5)
    result = longest_streak([h1, h2])
    assert result == 5

def test_longest_streak_by_habit():
    """Test streak calculation for a single habit."""
    h = create_habit("Solo", "daily", 4)
    result = longest_streak_by_habit(h)
    assert result == 4
