class Task:
    task_counter = 0
    def __init__(self, description, priority):
        Task.task_counter += 1
        self.task_id = Task.task_counter
        self.description = description
        self.priority = priority
        self.completed = False
    def mark_completed(self):
        self.completed = True
    def get_task_id(self):
        return self.task_id
    def get_description(self):
        return self.description
    def get_priority(self):
        return self.priority
    


 
