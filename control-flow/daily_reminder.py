#Prompts user for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time bound? (yes/no): ")

reminder = "Reminder: "
#Processes the task based on 
match priority:
    
    case "high":
        reminder += "This task has high priority."
    case "medium":
        reminder += "This task has medium priority."
    case "low":
        reminder += "This task has medium priority."
        
if time_bound == "yes":
    reminder == "This requires immediate attention today."
elif time_bound == "no":
    reminder == "You can attend to it later"
else:
    reminder += "Time bound status not recognised."
print(reminder)