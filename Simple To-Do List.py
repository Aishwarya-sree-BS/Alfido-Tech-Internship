import json
import os

class TodoList:
    def __init__(self, filename):
        self.filename = filename
        self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                self.tasks = json.load(file)
        else:
            self.tasks = []

    def save_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file)

    def add_task(self, task):
        self.tasks.append(task)
        self.save_tasks()
        print(f"Task '{task}' added.")

    def remove_task(self, task_number):
        try:
            task_number = int(task_number)
            if task_number > 0 and task_number <= len(self.tasks):
                task = self.tasks.pop(task_number - 1)
                self.save_tasks()
                print(f"Task '{task}' removed.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Invalid task number.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")

def main():
    filename = 'tasks.json'
    todo_list = TodoList(filename)

    while True:
        print("\nOptions:")
        print("1. Add task")
        print("2. Remove task")
        print("3. View tasks")
        print("4. Quit")

        option = input("Choose an option: ")

        if option == '1':
            task = input("Enter a task: ")
            todo_list.add_task(task)
        elif option == '2':
            task_number = input("Enter the task number to remove: ")
            todo_list.remove_task(task_number)
        elif option == '3':
            todo_list.view_tasks()
        elif option == '4':
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
