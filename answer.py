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
                
class PriorityQueue:
    def __init__(self):
        self.tasks = []
    def add_task(self, task):
        if task.priority >self.tasks[-1,"priority"]:
            self.tasks.append(task)
        elif for i in range(len(self.tasks)):
               if task.priority <= self.tasks[i]:
                  self.tasks.insert(i,task)
     def incompleted_tasks(self):
        for i in range(len(self.tasks)
            if tasks[i,"completed"] == True :
                print(tasks[i])
    def get_highest_priority_task(self):
        if self.tasks:
            return self.tasks[0]
        else:
            return None
    def remove_highest_priority_task(self):
        if self.tasks:
            return self.tasks.pop(0)
        else:
            return None
    def display_all_tasks():
       if not tasks:
          print("no tasks found")
       elif for i in range(len(self.tasks)):
          print(tasks[i])

class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def add(self, item):
        for i in range(len(self.tasks))
           self.items.append(item)

    
    

        
                
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
    if choice == 1:
        description = input("Enter task description: ")
        priority = int(input("Enter task priority (integer): "))
        new_task = Task(description, priority)
        add_task(Task)
        
    elif choice == 2:
        task_id = int(input("Enter task id: "))
        task = self.get_description(task_id)
        if task:
            print("task id = "+task_id+" description= "+task+" priority= "+self.get_priority(task_id))
    elif choice == 3:
       completed_task= self.remove_highest_priority_task()
        if completed_task:
          add(completed_task)
          print("you have finished "+ completed_task)
          set_completed_task(completed_task) 
    elif choice == 4:
       self.display_all_tasks()
    elif choice == 5:
       self.incompleted_tasks()
    elif choice == 6:
       self.items[-1]
    elif choice == 7:
        break

    


 
