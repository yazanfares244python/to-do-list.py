# Important modules
from pathlib import Path
from datetime import datetime, date, time
import json
# Unimportant module
from time import sleep
# Creating the class that is responsible for the main critical points about the to-do list(adding, viewing, deleting, etc.)
class ToDoList:
    # Initializing each variable thats gonna be used in this class
    def __init__(self):
        self.weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        self.to_do_list = []
        self.task_info = {}
        self.task = None
        self.category = None
        self.priority = None
        self.year = 0
        self.month = 0
        self.day = 0
        self.hour = 0
        self.minute = 0
        self.date = None
        # This variable is from the ToDoListCLI class
        self.option = None
    # Creating the function that adds a new task
    def add_new_task(self):
        # Asking for the task while checking if its valid or not
        while True:
            self.task = input("Enter the task that you want to add into the to-do list ->: ").capitalize()
            if not self.task:
                print("Enter a valid task")
            else:
                break
        # Asking for the category while checking if its valid or not
        while True:
            self.category = input(f"Enter the category of {self.task}(School, Programming, Sports, etc.) ->: ").capitalize()
            if not self.category:
                print("Enter a valid category")
            else:
                break
        # Asking for the priority while checking if its valid or not
        while True:
            self.priority = input(f"Enter the priority of {self.task}(High/Medium/Low) ->: ").capitalize().strip()
            if self.priority not in ("High", "Medium", "Low"):
                print("Enter a valid priority")
            else:
                break
        # Asking for the year, month and day for the due date and the hour and minute for the due time
        while True:
            try:
                self.year = int(input("Enter the year ->: "))
                self.month = int(input("Enter the month ->: "))
                self.day = int(input("Enter the day ->: "))
                self.hour = int(input("Enter the hour ->: "))
                self.minute = int(input("Enter the minute ->: "))
                self.date = datetime(self.year, self.month, self.day, self.hour, self.minute)
                # Checking if the date is older than the current date
                if datetime.now() > self.date:
                    print(f"Enter a date that isn't in the past(Today's date: {datetime.now()})")
                else:
                    break
            except ValueError:
                print("Invalid parameters therefore we will start over")
        self.task_info = {"Task": self.task, "Category": self.category, "Priority": self.priority, "Due Date": self.date.date(), "Due Time": self.date.time(), "Due Weekday": self.weekdays[self.date.weekday()], "Done": 'Pending...'}
        if self.task_info in self.to_do_list:
            print("\nTask information already found")
        else:
            self.to_do_list.append(self.task_info)
            print(f"\nThe task {self.task} has been added into the to-do list alongside it's information")
    # Creating the function that displays all of the tasks
    def display_tasks(self):
        print("\nTo-Do list: ")
        # Check if to-do list data exists
        if not self.to_do_list:
            print("\nNo data found to proceed")
        else:
            # Looping through each task information
            for task_info in self.to_do_list:
                print() # <- this is to separate each task information for clearer structure
                for task_info_key, task_info_value in task_info.items():
                    print(f"{task_info_key} -> {task_info_value}")
    # Creating the function that deletes a task from the to-do list
    def delete_task(self):
        # Asking for the task while checking if its valid or not
        while True:
            self.task = input("Enter the task that you want to delete ->: ").capitalize()
            if not self.task:
                print("Enter a valid task")
            else:
                break
        # Asking for the category while checking if its valid or not
        while True:
            self.category = input(f"Enter the category of {self.task}(School, Programming, Sports, etc.) ->: ").capitalize()
            if not self.category:
                print("Enter a valid category")
            else:
                break
        # Asking for the priority while checking if its valid or not
        while True:
            self.priority = input(f"Enter the priority of {self.task}(High/Medium/Low) ->: ").capitalize().strip()
            if self.priority not in ("High", "Medium", "Low"):
                print("Enter a valid priority")
            else:
                break
        # Asking for the due date while checking if its valid or not
        while True:
            try:
                self.year = int(input("Enter the year ->: "))
                self.month = int(input("Enter the month ->: "))
                self.day = int(input("Enter the day ->: "))
                self.hour = int(input("Enter the hour ->: "))
                self.minute = int(input("Enter the minute ->: "))
                self.date = datetime(self.year, self.month, self.day, self.hour, self.minute)
                break
            except ValueError:
                print("Invalid parameters therefore we will start over")
        # Checking if the task information is found or not
        if not any(self.task == task_info["Task"] and self.category == task_info["Category"] and self.priority == task_info["Priority"] and self.date.date() == task_info["Due Date"] and self.date.time() == task_info["Due Time"] for task_info in self.to_do_list):
            print("\nNo such task information found")
        else:
            # Looping through each task information
            for task_info in self.to_do_list:
                if task_info["Task"] == self.task and task_info["Category"] == self.category and task_info["Priority"] ==  self.priority and task_info["Due Date"] == self.date.date() and task_info["Due Time"] == self.date.time():
                    self.to_do_list.remove(task_info)
                    print(f"\nThe task {self.task} has been deleted alongside it's information")
                    break
                else:
                    continue
    # Creating the function that clears all tasks from the to-do list
    def clear_all_tasks(self):
        # Check if to-do list exists
        if not self.to_do_list:
            print("\nNo data found to proceed")
        else:
            self.to_do_list.clear()
            print("\nThe to-do list has been cleared")
    # Creating the function that edit's an task's attribute(Name/Category/Priority/Due Date/Due Time)
    def edit_task_attribute(self):
        # Asking for the task while checking if its valid or not
        while True:
            self.task = input("Enter the task whose attribute you would like to edit ->: ").capitalize()
            if not self.task:
                print("Enter a valid task")
            else:
                break
        # Asking for the category while checking if its valid or not
        while True:
            self.category = input(f"Enter the category of {self.task}(School, Programming, Sports, etc.) ->: ").capitalize()
            if not self.category:
                print("Enter a valid category")
            else:
                break
        # Asking for the priority while checking if its valid or not
        while True:
            self.priority = input(f"Enter the priority of {self.task}(High/Medium/Low) ->: ").capitalize().strip()
            if self.priority not in ("High", "Medium", "Low"):
                print("Enter a valid priority")
            else:
                break
        # Asking for the due date while checking if its valid or not
        while True:
            try:
                self.year = int(input("Enter the year ->: "))
                self.month = int(input("Enter the month ->: "))
                self.day = int(input("Enter the day ->: "))
                self.hour = int(input("Enter the hour ->: "))
                self.minute = int(input("Enter the minute ->: "))
                self.date = datetime(self.year, self.month, self.day, self.hour, self.minute)
                break
            except ValueError:
                print("Invalid parameters therefore we will start over")
        # Check if the task information exists
        if not any(self.task == task_info["Task"] and self.category == task_info["Category"] and self.priority == task_info["Priority"] and self.date.date() == task_info["Due Date"] and self.date.time() == task_info["Due Time"] for task_info in self.to_do_list):
            print("\nNo such task information found")
        else:
            # Looping through each task information
            for task_info in self.to_do_list:
                if task_info["Task"] == self.task and task_info["Category"] == self.category and task_info["Priority"] == self.priority and task_info["Due Date"] == self.date.date() and task_info["Due Time"] == self.date.time():
                    self.option = input(f"Enter the attribute of {self.task} that you would like to edit(Enter N for Name, C for Category, P for Priority, DD for Due Date, DT for Due Time) ->: ").upper().strip()
                    if self.option == 'N':
                        # Asking for the task while checking if its valid or not
                        while True:
                            self.task = input(f"Enter the new version of {task_info['Task']} ->: ").capitalize()
                            if not self.task:
                                print("Enter a valid task")
                            elif task_info["Task"] == self.task:
                                print("\nThe task name is already the same")
                                break
                            else:
                                print(f"\nThe task {task_info['Task']} has been edited to {self.task}")
                                task_info["Task"] = self.task
                                break
                    elif self.option == 'C':
                        # Asking for the category while checking if its valid or not
                        while True:
                            self.category = input(f"Enter the category of {self.task}(School, Programming, Sports, etc.) ->: ").capitalize()
                            if not self.category:
                                print("Enter a valid category")
                            elif task_info["Category"] == self.category:
                                print("\nThe task category is already the same")
                                break
                            else:
                                print(f"\nThe task {self.task}'s category {task_info['Category']} has been edited to {self.category}")
                                task_info['Category'] = self.category
                                break
                    elif self.option == 'P':
                        # Asking for the priority while checking if its valid or not
                        while True:
                            self.priority = input(f"Enter the priority of {self.task}(High/Medium/Low) ->: ").capitalize().strip()
                            if self.priority not in ("High", "Medium", "Low"):
                                print("Enter a valid priority")
                            elif task_info["Priority"] == self.priority:
                                print("\nThe task priority is already the same")
                                break
                            else:
                                print(f"\nThe task {self.task}'s priority {task_info['Priority']} has been edited to {self.priority}")
                                task_info["Priority"] = self.priority
                                break
                    elif self.option == 'DD':
                        # Asking for the year, month and day while checking if its valid or not
                        while True:
                            try:
                                self.year = int(input("Enter the year ->: "))
                                self.month = int(input('Enter the month ->: '))
                                self.day = int(input('Enter the day ->: '))
                                self.date = date(self.year, self.month, self.day)
                                # Check if the date input is the same as the due date that exists
                                if task_info["Due Date"] == self.date:
                                    print("\nThe task's due date is already the same")
                                else:
                                    print(f"\nThe task {self.task}'s due date {task_info['Due Date']} has been edited to {self.date} including the weekday")
                                    task_info["Due Date"] = self.date
                                    task_info["Due Weekday"] = self.weekdays[self.date.weekday()]
                                break
                            except ValueError:
                                print("Invalid parameters therefore we will start over")
                    elif self.option == 'DT':
                        # Asking for the hour and minute while checking if its valid or not
                        while True:
                            try:
                                self.hour = int(input("Enter the hour ->: "))
                                self.minute = int(input("Enter the minute ->: "))
                                self.date = time(self.hour, self.minute)
                                # Check if the time input is the same as the due time that exists
                                if task_info['Due Time'] == self.date:
                                    print("\nThe task due time is already the same")
                                else:
                                    print(f"\nThe task {self.task}'s due time {task_info['Due Time']} has been edited to {self.date}")
                                    task_info["Due Time"] = self.date
                                break
                            except ValueError:
                                print('Invalid parameters therefore we will start over')
                    else:
                        print("\nInvalid option")
                    break
    # Creating the function that marks a task as done
    def mark_task(self):
        # Asking for the task while checking if its valid or not
        while True:
            self.task = input("Enter the task that you want to mark as done ->: ").capitalize()
            if not self.task:
                print("Enter a valid task")
            else:
                break
        # Asking for the category while checking if its valid or not
        while True:
            self.category = input(f"Enter the category of {self.task} ->: ").capitalize()
            if not self.category:
                print("Enter a valid category")
            else:
                break
        # Asking for the priority while checking if its valid or not
        while True:
            self.priority = input(f"Enter the priority of {self.task}(High/Medium/Low) ->: ").capitalize().strip()
            if self.priority not in ("High", "Medium", "Low"):
                print("Enter a valid priority")
            else:
                break
        # Asking for the due date while checking if its valid or not
        while True:
            try:
                self.year = int(input("Enter the year ->: "))
                self.month = int(input("Enter the month ->: "))
                self.day = int(input("Enter the day ->: "))
                self.hour = int(input("Enter the hour ->: "))
                self.minute = int(input("Enter the minute ->: "))
                self.date = datetime(self.year, self.month, self.day, self.hour, self.minute)
                break
            except ValueError:
                print("Invalid parameters therefore we will start over")
        # Check if the task information exists
        if not any(self.task == task_info["Task"] and self.category == task_info["Category"] and self.priority == task_info['Priority'] and self.date.date() == task_info["Due Date"] and self.date.time() == task_info["Due Time"] for task_info in self.to_do_list):
            print("\nNo such task information found")
        else:
            # Looping through each task information
            for task_info in self.to_do_list:
                if task_info["Task"] == self.task and task_info["Category"] == self.category and task_info["Priority"] == self.priority and task_info["Due Date"] == self.date.date() and task_info["Due Time"] == self.date.time():
                    if task_info["Done"] == "Pending...":
                        # Checking if the task was marked late
                        if datetime.now() > self.date:
                            task_info["Done"] = "Complete(DONE LATE⚠️  )"
                        else:
                            task_info["Done"] = "Complete✅"
                        print("\nThe task has been marked as complete")
                    else:
                        print("\nThe task already marked as complete")
                    break
                else:
                    continue  
    # Creating the function that unmarks a task as done
    def unmark_task(self):
        # Asking for the task while checking if its valid or not
        while True:
            self.task = input("Enter the task that you want to unmark as done ->: ").capitalize()
            if not self.task:
                print("Enter a valid task")
            else:
                break
        # Asking for the category while checking if its valid or not
        while True:
            self.category = input(f"Enter the category of {self.task}(School, Programming, Sports, etc.) ->: ").capitalize()
            if not self.category:
                print("Enter a valid category")
            else:
                break
        # Asking for the priority while checking if its valid or not
        while True:
            self.priority = input(f"Enter the priority of {self.task}(High/Medium/Low) ->: ").capitalize().strip()
            if self.priority not in ("High", "Medium", "Low"):
                print("Enter a valid priority")
            else:
                break
        # Asking for the due date while checking if its valid or not
        while True:
            try:
                self.year = int(input("Enter the year ->: "))
                self.month = int(input("Enter the month ->: "))
                self.day = int(input("Enter the day ->: "))
                self.hour = int(input("Enter the hour ->: "))
                self.minute = int(input("Enter the minute ->: "))
                self.date = datetime(self.year, self.month, self.day, self.hour, self.minute)
                break
            except ValueError:
                print("Invalid parameters therefore we will start over")
        # Checking if the task information exists
        if not any(self.task == task_info["Task"] and self.category == task_info["Category"] and self.priority == task_info["Priority"] and self.date.date() == task_info["Due Date"] and self.date.time() == task_info["Due Time"] for task_info in self.to_do_list):
            print("\nNo such task information found")
        else:
            # Looping through each task information
            for task_info in self.to_do_list:
                if task_info["Task"] == self.task and task_info["Category"] == self.category and task_info["Priority"] == self.priority and task_info["Due Date"] == self.date.date() and task_info["Due Time"] == self.date.time():
                    if "Complete" in task_info["Done"]:
                        task_info["Done"] = "Pending..."
                        print("\nThe task has been unmarked as complete")
                    else:
                        print("\nThe task is already unmarked")
                    break
                else:
                    continue
    # Creating the function that displays tasks according to a specific category
    def display_tasks_category(self):
        # Check if to-do list data exists
        if not self.to_do_list:
            print("\nNo data found to proceed")
        else:
            # Asking for the category while checking if its valid or found
            while True:
                self.category = input("Enter the category to display the tasks ->: ").capitalize()
                if not self.category:
                    print("Enter a valid category")
                elif all(self.category != task_info["Category"] for task_info in self.to_do_list):
                    print("\nNo such category found")
                    break
                else:
                    print(f"\nTo-Do List({self.category}): ")
                    # Looping through each task information
                    for task_info in self.to_do_list:
                        if task_info["Category"] == self.category:
                            print()
                            # Looping through each key and value
                            for task_info_key, task_info_value in task_info.items():
                                print(f"{task_info_key} -> {task_info_value}")
                        else:
                            continue
                    break
    # Creating the function that displays tasks according to a specific priority
    def display_tasks_priority(self):
        # Check if to-do list data exists
        if not self.to_do_list:
            print("\nNo data found to proceed")
        else:
            # Asking for the priority while checking if its valid or not
            while True:
                self.priority = input("Enter the priority to display the tasks ->: ").capitalize().strip()
                if self.priority not in ("High", "Medium", "Low"):
                    print("Enter a valid priority")
                else:
                    print(f"\nTo-Do List(Priority: {self.priority}): ")
                    # Looping through each task information 
                    for task_info in self.to_do_list:
                        if task_info["Priority"] == self.priority:
                            print()
                            # Looping through each key and value
                            for task_info_key, task_info_value in task_info.items():
                                print(f"{task_info_key} -> {task_info_value}")
                        else:
                            continue
                    break
    # Creating the function that displays tasks that are pending
    def display_tasks_pending(self):
        print("\nTo-Do List(Pending Tasks): ")
        # Check if to-do list data exists
        if not self.to_do_list:
            print("\nNo data found to proceed")
        else:
            # Looping through each task information
            for task_info in self.to_do_list:
                if task_info["Done"] == "Pending...":
                    print()
                    # Looping through each key and value
                    for task_info_key, task_info_value in task_info.items():
                        print(f"{task_info_key} -> {task_info_value}")
                else:
                    continue
    # Creating the function that displays tasks that are done
    def display_tasks_done(self):
        print("\nTo-Do List(Done Tasks): ")
        # Check if to-do list data exists
        if not self.to_do_list:
            print("\nNo data found to proceed")
        else:
            # Looping through each task information
            for task_info in self.to_do_list:
                if "Complete" in task_info["Done"]:
                    print()
                    # Looping through each key and value 
                    for task_info_key, task_info_value in task_info.items():
                        print(f"{task_info_key} -> {task_info_value}")
                else:
                    continue
    # Creating the function that displays tasks that are for today
    def display_tasks_today(self):
        print("\nTo-Do List(Today): ")
        # Check if to-do list data exists
        if not self.to_do_list:
            print("\nNo data found to proceed")
        else:
            # Looping through each task information
            for task_info in self.to_do_list:
                if task_info["Due Date"] == datetime.now().date():
                    print()
                    # Looping through each key and value
                    for task_info_key, task_info_value in task_info.items():
                        print(f"{task_info_key} -> {task_info_value}")
                else:
                    continue
    # Creating the function that displays tasks that are overdue(in the past)
    def display_tasks_overdue(self):
        print("\nTo-Do List(Overdue): ")
        # Check if to-do list data exists
        if not self.to_do_list:
            print("\nNo data found to proceed")
        else:
            # Looping through each task information
            for task_info in self.to_do_list:
                if task_info["Due Date"] < datetime.now().date() or (task_info["Due Date"] == datetime.now().date() and task_info["Due Time"]  < datetime.now().time()):
                    print()
                    # Looping through each key and value
                    for task_info_key, task_info_value in task_info.items():
                        print(f"{task_info_key} -> {task_info_value}")
                else:
                    continue
    # Creating the function that displays the tasks that are in the future
    def display_tasks_future(self):
        print("\nTo-Do List(Future): ")
        # Check if to-do list data exists
        if not self.to_do_list:
            print("\nNo data found to proceed")
        else:
            # Looping through each task information
            for task_info in self.to_do_list:
                if task_info["Due Date"] > datetime.now().date() or (task_info["Due Date"] == datetime.now().date() and task_info["Due Time"] > datetime.now().time()):
                    print()
                    # Looping through each key and value
                    for task_info_key, task_info_value in task_info.items():
                        print(f"{task_info_key} -> {task_info_value}")
                else:
                    continue
# Creating the class that is responsible for the CLI commands while inheriting most of the variables from the ToDoList class to avoid AttributeError's
class ToDoListCLI(ToDoList):
    # Creating the function that asks the user what they want
    def display_menu(self):
        ToDoListData.read_data(self)
        print("--- To-Do List ---")
        while True:
            print("\n1. Add a new task")
            print("2. View all tasks")
            print("3. Delete a task")
            print("4. Clear all tasks")
            print("5. Edit a task's attribute(Name/Category/Priority/Due Date/Due Time)")
            print("6. Mark a task as done")
            print("7. Unmark a task")
            print("8. View tasks according to a specific category")
            print("9. View tasks according to a specific priority")
            print("10. View tasks that are pending")
            print("11. View tasks that are done")
            print("12. View today's tasks")
            print("13. View overdue tasks")
            print("14. View future tasks")
            print("15. Exit")
            self.option = input("Enter your option(1-15) ->: ")
            if self.option == '1':
                ToDoList.add_new_task(self)
            elif self.option == '2':
                ToDoList.display_tasks(self)
            elif self.option == '3':
                ToDoList.delete_task(self)
            elif self.option == '4':
                ToDoList.clear_all_tasks(self)
            elif self.option == '5':
                ToDoList.edit_task_attribute(self)
            elif self.option == '6':
                ToDoList.mark_task(self)
            elif self.option == '7':
                ToDoList.unmark_task(self)
            elif self.option == '8':
                ToDoList.display_tasks_category(self)
            elif self.option == '9':
                ToDoList.display_tasks_priority(self)
            elif self.option == '10':
                ToDoList.display_tasks_pending(self)
            elif self.option == '11':
                ToDoList.display_tasks_done(self)
            elif self.option == '12':
                ToDoList.display_tasks_today(self)
            elif self.option == '13':
                ToDoList.display_tasks_overdue(self)
            elif self.option == '14':
                ToDoList.display_tasks_future(self)
            elif self.option == '15':
                print("Ok wait a moment...")
                sleep(1.5)
                print("Saving data...")
                ToDoListData.write_data(self)
                sleep(2)
                print("Exiting...")
                sleep(1.5)
                break
            else:
                print("\nInvalid option")
# Creating the class that is responsible for the data saving
class ToDoListData:
    # Initializing one variable thats gonna be used in this class
    def __init__(self):
        self.to_do_list = []
    # Creating the function that reads the data from the file and writes it into the program
    def read_data(self):
        # Check if file exists
        if Path("to_do_list.json").is_file():
            with open("to_do_list.json", "r") as f:
                # Loading the data before converting the strings into date and time objects
                self.to_do_list = json.load(f)
                # Looping through each task information
                for task_info in self.to_do_list:
                    # Looping through the keys and values
                    for task_info_key, task_info_value in task_info.items():
                        if task_info_key == "Due Date":
                            task_info[task_info_key] = date.fromisoformat(task_info_value)
                        elif task_info_key == "Due Time":
                            task_info[task_info_key] = time.fromisoformat(task_info_value)
    # Creating the function that reads the data from the program and writes it into the file
    def write_data(self):
        with open("to_do_list.json", "w") as f:
            # Looping through each task information
            for task_info in self.to_do_list:
                # Looping through the keys and values
                for task_info_key, task_info_value in task_info.items():
                    if task_info_key == "Due Date":
                        task_info[task_info_key] = date.isoformat(task_info_value)
                    elif task_info_key == 'Due Time':
                        task_info[task_info_key] = time.isoformat(task_info_value)
                    else:
                        continue
            # Saving the data after the date and time objects are converted into strings to avoid TypeError's
            json.dump(self.to_do_list, f)
to_do_list = ToDoListCLI().display_menu()   
