import json
from datetime import datetime
from time import sleep
# The class that is responsible for the to-do list operations such as adding, viewing, deleting, etc.
class ToDoList:
    # Initialized variables that will be used in this class
    def __init__(self):
        self.to_do_list = []
        self.weekdays= {
                    1: "Monday",
                    2: "Tuesday",
                    3: "Wednesday",
                    4: "Thursday",
                    5: "Friday",
                    6: "Saturday",
                    7: "Sunday"
        }
    # The function that adds a new task into the to-do list
    def add_task(self, function):
        task = function("Task", "task")
        category = function("Category", f"category of {task}")
        priority = function("Priority", f"priority of {task}(High/Medium/Low)")
        deadline = function("Deadline", f"deadline of {task} in this format -> YYYY-MM-DD HH:MM(The hour and minute part is optional.)")
        print(f"\nThe task {task} has been added into the to-do list.(ID: {len(self.to_do_list)+1})")
        self.to_do_list.append({"ID": len(self.to_do_list)+1, "Task": task, "Category": category, "Priority": priority, "Deadline": deadline, "Weekday": self.weekdays[deadline.isoweekday()], "Done": "Pending..."})
    # The function that displays the tasks
    def display_tasks(self, parameter=None, parameter_value=None, option=None):
        if not self.to_do_list:
            print("\nNo data found.")
            return
        if parameter == None:
            print("\nTo-Do List: \n")
            print("ID  |  Task  |  Category  |  Priority  |   Deadline    |  Weekday  |  Done  ")
            for task_info in self.to_do_list:
                print(f"{task_info['ID']})   {task_info['Task']}    {task_info['Category']}       {task_info['Priority']}     {task_info['Deadline']}   {task_info['Weekday']}  {task_info['Done']}")
        if callable(parameter_value):
            variable = parameter_value(parameter, f"{parameter} to display the tasks")
            if not [task_info for task_info in self.to_do_list if task_info[parameter] == variable]:
                print("\nNo data found.")
                return
            print(f"\nTo-Do List({parameter} -> {variable}): \n")
            print("ID  |  Task  |  Category  |  Priority  |   Deadline    |  Weekday  |  Done  ")
            for task_info in self.to_do_list:
                if task_info[parameter] == variable:
                    print(f"{task_info['ID']})   {task_info['Task']}    {task_info['Category']}       {task_info['Priority']}     {task_info['Deadline']}   {task_info['Weekday']}  {task_info['Done']}")
        if option == "10":
            if not [task_info for task_info in self.to_do_list if task_info[parameter] == parameter_value]:
                print("\nNo data found.")
                return
            print(f"\nTo-Do List(Pending): \n")
            print("ID  |  Task  |  Category  |  Priority  |   Deadline    |  Weekday  |  Done  ")
            for task_info in self.to_do_list:
                if task_info[parameter] == parameter_value:
                    print(f"{task_info['ID']})   {task_info['Task']}    {task_info['Category']}       {task_info['Priority']}     {task_info['Deadline']}   {task_info['Weekday']}  {task_info['Done']}")
        elif option == '11':
            if not [task_info for task_info in self.to_do_list if parameter_value in task_info[parameter]]:
                print("\nNo data found.")
                return
            print(f"\nTo-Do List(Complete): \n")
            print("ID  |  Task  |  Category  |  Priority  |   Deadline    |  Weekday  |  Done  ")
            for task_info in self.to_do_list:
                if parameter_value in task_info[parameter]:
                    print(f"{task_info['ID']})   {task_info['Task']}    {task_info['Category']}       {task_info['Priority']}     {task_info['Deadline']}   {task_info['Weekday']}  {task_info['Done']}")
        elif option == '12':    
            if not [task_info for task_info in self.to_do_list if task_info[parameter].date() == datetime.now().date()]:
                print("\nNo data found.")
                return
            print(f"\nTo-Do List({datetime.now().date()}): \n")
            print("ID  |  Task  |  Category  |  Priority  |   Deadline    |  Weekday  |  Done  ")
            for task_info in self.to_do_list:
                if task_info["Deadline"].date() == datetime.now().date():
                    print(f"{task_info['ID']})   {task_info['Task']}    {task_info['Category']}       {task_info['Priority']}     {task_info['Deadline']}   {task_info['Weekday']}  {task_info['Done']}")
        elif option == '13':
            if not [task_info for task_info in self.to_do_list if task_info[parameter] < datetime.now()]:
                print("\nNo data found to proceed.")
                return
            print(f"\nTo-Do List(Before {datetime.now()}): \n")
            print("ID  |  Task  |  Category  |  Priority  |   Deadline    |  Weekday  |  Done  ")
            for task_info in self.to_do_list:
                if task_info["Deadline"] < datetime.now():
                    print(f"{task_info['ID']})   {task_info['Task']}    {task_info['Category']}       {task_info['Priority']}     {task_info['Deadline']}   {task_info['Weekday']}  {task_info['Done']}")
        elif option == '14':
            if not [task_info for task_info in self.to_do_list if task_info["Deadline"] > datetime.now()]:
                print("\nNo data found to proceed.")
                return
            print(f"\nTo-Do List(After {datetime.now()}): \n")
            print("ID  |  Task  |  Category  |  Priority  |   Deadline    |  Weekday  |  Done  ")
            for task_info in self.to_do_list:
                if task_info["Deadline"] > datetime.now():
                    print(f"{task_info['ID']})   {task_info['Task']}    {task_info['Category']}       {task_info['Priority']}     {task_info['Deadline']}   {task_info['Weekday']}  {task_info['Done']}")
    # The function that deletes a task
    def delete_task(self, function):
        if not self.to_do_list:
            print("\nNo data found to proceed.")
            return
        self.display_tasks()
        task_id = function(self.to_do_list)
        for task_info in self.to_do_list:
            if task_info["ID"] == task_id:
                self.to_do_list.remove(task_info)
                print(f"\nThe task with the task ID {task_id} has been deleted.")
                self.reload_ids()
                break
    # The function thar clears the entire to-do list
    def clear_tasks(self, function):
        if not self.to_do_list:
            print("\nNo data found to proceed.")
            return
        if function() == 'y':
            self.to_do_list.clear()
            print("\nThe to-do list has been cleared.")
            return
        print("\nOk we will proceed as usual.")
    # The function that can edit a task
    def edit_task(self, function, function2, function3):
        if not self.to_do_list:
            print("\nNo data found to proceed.")
            return
        category = function()
        self.display_tasks()
        task_id = function2(self.to_do_list)
        for task_info in self.to_do_list:
            if task_info["ID"] != task_id:
                continue
            initial_value = task_info[category]
            final_value = function3(category, f"new version of the {category.lower()} for the task with the task ID {task_id}")
            if initial_value == final_value:
                print(f"\nThe {category.lower()} of the task with the task ID {task_id} is already the same.")
                break
            task_info[category] = final_value
            if category == "Deadline":
                task_info["Weekday"] = self.weekdays[final_value.isoweekday()]
            print(f"\nThe task with the task ID {task_id} has had it's {category.lower()} edited.")
            break
    # The function that marks a task as done
    def mark_task(self, function):
        if not self.to_do_list:
            print("\nNo data found to proceed.")
            return
        self.display_tasks()
        task_id = function(self.to_do_list)
        for task_info in self.to_do_list:
            if task_info["ID"] != task_id:
                continue
            if "Complete" in task_info['Done']:
                print("\nThe task is already marked as done.")
                break
            print(f"\nThe task with the ID {task_id} has been marked as done.")
            if task_info["Deadline"] < datetime.now():
                task_info["Done"] = "Complete(OVERDUE)"
                break
            task_info["Done"] = "Complete"
            break
    # The function that unmarks a task
    def unmark_task(self, function):
        if not self.to_do_list:
            print("\nNo data found to proceed.")
            return
        self.display_tasks()
        task_id = function(self.to_do_list)
        for task_info in self.to_do_list:
            if task_info["ID"] != task_id:
                continue
            if task_info["Done"] == "Pending...":
                print("\nThe task is already not marked.")
                break
            task_info["Done"] = "Pending..."
            print(f"\nThe task with the ID {task_id} has been unmarked.")
            break
    # The function that reloads the ID's after deleting
    def reload_ids(self):
        for index, task_info in enumerate(self.to_do_list, start=1):
            task_info["ID"] = index
# The class that is responsible for the CLI commands which are mostly user inputs
class ToDoListCLI:
    # Initialized attributes that will be used in this class 
    def __init__(self):
        self.to_do = ToDoList()
        self.data = ToDoListJSON()
    # The function that asks the user for an input while handling edge cases
    def user_input(self, parameter: str, text: str):
        categories = {
            "Task": None,
            "Category": None,
            "Priority": ("High", "Medium", "Low"),
            "Deadline": datetime.fromisoformat
        }
        while True:
            if callable(categories[parameter]):
                try:
                    variable = categories[parameter](input(f"Enter the {text} ->: "))
                    if variable.date() >= datetime.now().date():
                        return variable
                    print(f"Enter a deadline that doesn't have a date that is before than {datetime.now().date()}.")
                except ValueError as e:
                    print(f"\n{e}\n")
            elif categories[parameter] == None:
                variable = input(f"Enter the {text} ->: ").capitalize().strip()
                if variable:
                    return variable
                print("Enter a valid input.")
            else:
                variable = input(f"Enter the {text} ->: ").capitalize().strip()
                if variable in categories[parameter]:
                    return variable
                print("Invalid priority.(Options: High/Medium/Low)")
    # The function that asks for an ID input
    def id_input(self, storage: list) -> int:
        while True:
            try:
                id_input = int(input("Enter the ID ->: "))
                if 0 < id_input <= len(storage):
                    return id_input
                print("Enter a valid ID.")
            except ValueError:
                print("Invalid ID, pick again.")
    # The function that checks whether the user actually wants to clear the to-do list or not
    def clear_task_input(self) -> str:
        while True:
            clear_task_input = input("Are you sure you want to clear the entire to-do list(y/n) ->: ").lower().strip()
            if clear_task_input in ("y", "n"):
                return clear_task_input
            print("Enter a valid option.")
    # The function that asks what attribute to edit
    def edit_task_attribute_input(self):
        while True:
            attribute_input = input("Enter the attribute that you would like to edit(Task, Category, Priority, Deadline)->: ").capitalize().strip()
            if attribute_input in ("Task", "Category", "Priority", "Deadline"):
                return attribute_input
            print("Enter a valid option.(Options: Task, Category, Priority, Deadline)")
    # The function that displays the options
    def display_options(self):
        print("""
1. Add a task\n2. View tasks\n3. Delete a task\n4. Clear all tasks\n5. Edit a task\n6. Mark a task as done\n7. Unmark a task\n8. View tasks according to a specific category\n9. View tasks according to a specific priority\n10. View tasks that are pending\n11. View tasks that are complete\n12. View tasks that are due today\n13. View tasks that are overdue\n14. View tasks for the future\n15. Exit
""")
    # The function that runs the entire program
    def run_program(self):
        print("--- TO-DO LIST ---")
        self.to_do.to_do_list = self.data.read_file()
        while True:
            self.display_options()
            option = input('Enter your option(1-15) ->: ').strip()
            if option == '1':
                self.to_do.add_task(self.user_input)
            elif option == '2':
                self.to_do.display_tasks()
            elif option == '3':
                self.to_do.delete_task(self.id_input)
            elif option == '4':
                self.to_do.clear_tasks(self.clear_task_input)
            elif option == '5':
                self.to_do.edit_task(self.edit_task_attribute_input, self.id_input, self.user_input)
            elif option == '6':
                self.to_do.mark_task(self.id_input)
            elif option == '7':
                self.to_do.unmark_task(self.id_input)
            elif option == '8':
                self.to_do.display_tasks("Category", self.user_input)
            elif option == '9':
                self.to_do.display_tasks("Priority", self.user_input)
            elif option == '10':
                self.to_do.display_tasks("Done", "Pending...", option)
            elif option == '11':
                self.to_do.display_tasks("Done", "Complete", option)
            elif option in ('12', '13', '14'):
                self.to_do.display_tasks("Deadline", None, option)
            elif option == '15':
                print("Ok wait a moment...")
                sleep(1.5)
                print("Saving data...")
                self.data.write_file(self.to_do.to_do_list)
                sleep(2)
                print("Exiting...")
                sleep(1.5)
                break
            else:
                print("\nInvalid option.\n")
# The class that is responsible for the JSON data saving/parsing
class ToDoListJSON:
    # The function that validates the JSON structure before loading it
    def validate_json(self, storage: list) -> bool:
        if type(storage) is not list:
            return False
        for index, task_info in enumerate(storage, start=1):
            if type(task_info) is not dict:
                return False
            if set(task_info.keys()) != {"ID", "Task", "Category", "Priority", "Deadline", "Weekday", "Done"}:
                return False
            if type(task_info["ID"]) is not int or type(task_info["Task"]) is not str or type(task_info['Category']) is not str or type(task_info['Priority']) is not str or type(task_info['Deadline']) is not str or type(task_info['Weekday']) is not str or type(task_info["Done"]) is not str:
                return False
            if task_info["ID"] != index:
                return False
        return True
    # The function that reads the data from the file and loads it into the program
    def read_file(self):
        try:
            with open("to_do_list.json", encoding="utf-8") as f:
                storage = json.load(f)
                if self.validate_json(storage):
                    for task_info in storage:
                        task_info["Deadline"] = datetime.fromisoformat(task_info["Deadline"])
                    return storage
                return []
        except FileNotFoundError:
            return []
        except OSError as e:
            print(f"\n{e}\n")
            return []
        except json.JSONDecodeError as e:
            print(f"\n{e}\nIt seems that the file contains corrupted JSON data.\nThis could happen if the creator of this program has updated the structure.\nTherefore the to-do list will be reset.\nThank you for your understanding.\n")
            return []
    # The function that retrieves the data from the program and loads it into the file
    def write_file(self, storage: list):
        try:
            with open("to_do_list.json", "w", encoding="utf-8") as f:
                json.dump(storage, f, ensure_ascii=False, sort_keys=True, default=datetime.isoformat, indent=4)
        except OSError as e:
            print(f'\n{e}\n')
ToDoListCLI().run_program()
