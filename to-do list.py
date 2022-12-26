# Initialize the task list
tasks = ["Take out the trash", "Buy milk", "Send email"]

def add_task():
  # Prompt the user to enter a task
  task = input("Enter a task: ")
  
  # Add the task to the list
  tasks.append(task)

def delete_task():
  # Prompt the user to enter a task
  task = input("Enter a task to delete: ")
