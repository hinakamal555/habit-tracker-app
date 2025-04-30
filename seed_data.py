"""
seed_data.py

Creates predefined habits with 4 weeks of sample data for testing.
Run this script once to populate your habit tracker with test data.

Author: Hina Kamal
"""

from datetime import datetime, timedelta
from habit import Habit
from manager import HabitManager

# Create manager instance
manager = HabitManager()

# Define 5 habits
habit1 = Habit("Drink Water", "daily")
habit2 = Habit("Read Book", "daily")
habit3 = Habit("Exercise", "daily")
habit4 = Habit("Clean Room", "weekly")
habit5 = Habit("Call Family", "weekly")

# Simulate 4 weeks of completions
for i in range(28):  # 28 days = 4 weeks
    habit1.completed_dates.append(datetime.now() - timedelta(days=i))
    habit2.completed_dates.append(datetime.now() - timedelta(days=i))
    if i % 2 == 0:
        habit3.completed_dates.append(datetime.now() - timedelta(days=i))
for i in range(0, 28, 7):
    habit4.completed_dates.append(datetime.now() - timedelta(days=i))
    habit5.completed_dates.append(datetime.now() - timedelta(days=i))

# Add to manager
manager.add_habit(habit1)
manager.add_habit(habit2)
manager.add_habit(habit3)
manager.add_habit(habit4)
manager.add_habit(habit5)

# Save data
manager.save_to_file()

print("✅ Dummy habits created and saved.")
