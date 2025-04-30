"""
test_manager.py

Unit tests for the HabitManager class using pytest.
Covers adding, deleting, retrieving, and completing habits.
"""

import pytest
from manager import HabitManager
from habit import Habit

def test_add_and_get_habit():
    """Test adding a habit and retrieving it by name."""
    manager = HabitManager()
    habit = Habit("Test", "daily")
    manager.add_habit(habit)
    assert manager.get_habit("Test") == habit

def test_delete_habit():
    """Test deleting a habit by name."""
    manager = HabitManager()
    habit = Habit("DeleteMe", "daily")
    manager.add_habit(habit)
    manager.delete_habit("DeleteMe")
    assert manager.get_habit("DeleteMe") is None

def test_complete_habit():
    """Test completing a habit and updating the completed dates."""
    manager = HabitManager()
    habit = Habit("CompleteMe", "daily")
    manager.add_habit(habit)
    result = manager.complete_habit("CompleteMe")
    assert result is True
    assert len(habit.completed_dates) == 1
