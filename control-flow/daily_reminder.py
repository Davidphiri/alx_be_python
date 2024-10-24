#Prompts user for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time bound? (yes/no): ")

#Processes the task based on 
match priority:
    
    case "high":
       if time_bound == "yes":
         print(f" The task is '{task}' is of high priority that requires immediate attention today!.")
       else:
           print(f"{task} is a low priority task. Consider completing it when you have free time.")
    case "medium":
       if time_bound == 'yes':
         print(f" The task is '{task}' is of medium priority.")
       else:
           print(f"{task} is a low priority task. Consider completing it when you have time. ")
    case "low":
       if time_bound == 'yes':
         print(f" The task is '{task}' is of low priority.")
       else:
           print(f"{task} is a low priority task. Consider completing it when you have free time.")

