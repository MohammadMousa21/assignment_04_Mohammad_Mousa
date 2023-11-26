class Task:
    task_counter = 0
    def __init__(self, description, priority):
        Task.task_counter += 1
        self.task_id = Task.task_counter
        self.description = description
        self.priority = priority
        self.completed = False
    def set_mark_completed(self):
        self.completed = True
    def get_task_id(self):
        return self.task_id
    def get_description(self):
        return self.description
    def get_priority(self):
        return self.priority
    def is_completed(self):
        return self.completed
while True:
    print("""
1. Adding a new task to the task manager.
2. Getting a task from the queue given a task id
3. Marking the highest priority task as completed and putting
it in the task history.
4. Displaying all tasks in order of priority.
5. Displaying only the tasks that are not completed.
6. Displaying the last completed task.
7. Exit
""")
    choice = int(input("Enter your choice (1-7): "))
    if choice ==1:
        description = input("Enter task description: ")
        priority = int(input("Enter task priority (integer): "))
        new_task = Task(description, priority)
    elif choice == '2':
        task_id = int(input("Enter task id: "))
        task = self.get_description(task_id)
        if task:
            print("task id = "+task_id+" description= "+task+" priority= "+self.get_priority(task_id))
    elif choice == 7:
        break

    


 
