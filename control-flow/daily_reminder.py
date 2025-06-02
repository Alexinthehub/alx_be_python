# Prompt the user for the task description
task = input("Enter your task: ")

# Prompt for the priority level
priority = input("Priority (high/medium/low): ").lower()

# Ask if the task is time-bound
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Use match case to handle different priorities
match priority:
    case "high":
        reminder = f"Reminder: '{task}' is a high priority task"
    case "medium":
        reminder = f"Reminder: '{task}' is a medium priority task"
    case "low":
        reminder = f"Note: '{task}' is a low priority task"
    case _:
        reminder = f"'{task}' has an undefined priority"

# Modify reminder if time-bound
if time_bound == "yes":
    if priority in ("high", "medium"):
        reminder += " that requires immediate attention today!"
    elif priority == "low":
        reminder += ". Consider completing it soon as it is time-bound."
else:
    if priority == "low":
        reminder += ". Consider completing it when you have free time."

# Print the final reminder message
print(reminder)

