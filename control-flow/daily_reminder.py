
Task = input("Enter your task: ")
TimeBound = input("Is it time-bound? (yes/no): ").lower()
Priority = input("Priority (high/medium/low): ").lower()

match Priority:
    case "high":
        reminder = f"'{Task}' is a HIGH priority task."
    case "medium":
        reminder = f"'{Task}' is a MEDIUM priority task."
    case "low":
        reminder = f"'{Task}' is a LOW priority task."
    case _:
        reminder = "Invalid priority level."
        
if TimeBound == "yes" and priority in ["high", "medium", "low"]:
    reminder += " It requires immediate attention today!"
elif TimeBound == "no" and priority in ["high", "medium", "low"]:
    reminder += " Plan to do it when possible."
print("Reminder:", reminder)
