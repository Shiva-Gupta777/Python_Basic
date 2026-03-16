#Q.1 At the start of the day you have a checklist The tasks which you were able to finish, should get added to completed_tasks The tasks which you were not able to finish, should get added to incomplete_tasks This project is about organizing your daily tasks into two categories: completed tasks and incomplete tasks. Here’s how it works: 1. At the start of the day, you create a checklist of tasks you want to accomplish. 2. At the end of the day, you review which tasks you could finish and which you couldn’t. – If a task is finished, you move it to the completed tasks list. – If a task is not finished, you move it to the incomplete tasks list. This way, by the end of each day, you’ll have a clear overview of what you completed and what still needs attention.# Question:


# At the start of the day you have a checklist of tasks.
# If the task is finished → add it to completed_tasks
# If the task is not finished → add it to incomplete_tasks

checklist = ["Study Python", "Exercise", "Read Book", "Clean Room", "Practice Coding"]

completed_tasks = []
incomplete_tasks = []

for task in checklist:

    status = input(f"Did you complete '{task}'? (yes/no): ")     #f-string (formatted string).

    if status == "yes":
        completed_tasks.append(task)
    else:
        incomplete_tasks.append(task)

print("\nCompleted Tasks:")
print(completed_tasks)

print("\nIncomplete Tasks:")
print(incomplete_tasks)