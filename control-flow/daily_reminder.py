while True:
    Task = input("Enter your task (or type 'exit' to quit): ")

    if task.lower() == "exit":
        print("Goodbye! Stay productive!")
        break
     
    Time_Bound = input("Is it time-bound? (yes/no): ").lower()
     
    Priority = input("Priority (high/medium/low): ").lower()
    
    match Priority:
        case "high":
            if Time_Bound == "yes":
                print(f"Reminder: '{Task}' is a HIGH priority task that requires immediate attention today!")
            else:
                print(f"Reminder: '{Task}' is a HIGH priority task. Make sure to handle it as soon as possible.")
        case "medium":
            if Time_Bound == "yes":
                print(f"Reminder: '{Task}' is a MEDIUM priority task that should be done today.")
            else:
                print(f"Reminder: '{Task}' is a MEDIUM priority task. Plan to do it soon.")
        case "low":
            if Time_Bound == "yes":
                print(f"Reminder: '{Task}' is a LOW priority task but it is time-sensitive. Try to finish it today.")
            else:
                print(f"Note: '{Task}' is a LOW priority task. Consider completing it when you have free time.")
        case _:
            print("Invalid priority level. Please enter high, medium, or low.")

    print()