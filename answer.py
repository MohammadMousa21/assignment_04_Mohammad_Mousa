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
    def get_priority(self):
        return self.priority
    def is_completed(self):
        return self.completed
while True:
    print("\nTask Manager Menu:")
    print("1. Add a new task")
    print("2. Get a task from the queue given a task id")
    print("3. Mark the highest priority task as completed")
    print("4. Display all tasks in order of priority")
    print("5. Display only the tasks that are not completed")
    print("6. Display the last completed task")
    print("7. Exit")
    


 
