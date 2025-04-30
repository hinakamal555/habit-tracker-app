"""
test_habit.py

Unit tests for the Habit class using pytest.
Covers habit creation, streak logic, and serialization.
"""

import pytest
from habit import Habit
from datetime import datetime, timedelta

def test_habit_initialization():
    """Test initialization of Habit object."""
    habit = Habit("Test Habit", "daily")
    assert habit.name == "Test Habit"
    assert habit.periodicity == "daily"
    assert isinstance(habit.created_at, datetime)

def test_complete_and_streak_daily():
    """Test streak logic for a daily habit with 3 consecutive completions."""
    habit = Habit("Workout", "daily")
    today = datetime.now()
    habit.completed_dates = [today - timedelta(days=i) for i in range(3)]
    assert habit.get_streak() == 3

def test_complete_and_streak_weekly():
    """Test streak logic for a weekly habit with 4 weekly completions."""
    habit = Habit("Weekly Meeting", "weekly")
    habit.completed_dates = [datetime.now() - timedelta(days=i*7) for i in range(4)]
    assert habit.get_streak() == 4

def test_to_dict_and_from_dict():
    """Test serialization and deserialization of a Habit object."""
    habit = Habit("Test", "daily")
    habit.complete()
    d = habit.to_dict()
    loaded = Habit.from_dict(d)
    assert loaded.name == habit.name
    assert loaded.periodicity == habit.periodicity
    assert loaded.created_at == habit.created_at
    assert len(loaded.completed_dates) == 1
