def view_tasks(tasks):
    print("\n===== YOUR TASKS =====")

    if not tasks:
        print("No tasks available.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "✓" if task["done"] else " "

        print(f"{index}. [{status}] {task['title']}")


def add_task(tasks):
    print("\n===== ADD TASK =====")

    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    task = {
        "title": title,
        "done": False
    }

    tasks.append(task)

    print("Task added successfully!")


def complete_task(tasks):
    print("\n===== COMPLETE TASK =====")

    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:
        number = int(input("\nEnter task number to complete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        tasks[number - 1]["done"] = True

        print("Task marked as completed!")

    except ValueError:
        print("Please enter a valid number.")


def delete_task(tasks):
    print("\n===== DELETE TASK =====")

    if not tasks:
        print("No tasks available.")
        return

    view_tasks(tasks)

    try:
        number = int(input("\nEnter task number to delete: "))

        if number < 1 or number > len(tasks):
            print("Invalid task number.")
            return

        removed_task = tasks.pop(number - 1)

        print(f"Deleted task: {removed_task['title']}")

    except ValueError:
        print("Please enter a valid number.")


def search_tasks(tasks):
    print("\n===== SEARCH TASKS =====")

    if not tasks:
        print("No tasks available.")
        return

    keyword = input("Enter keyword to search: ").strip().lower()

    found = []

    for index, task in enumerate(tasks, start=1):
        if keyword in task["title"].lower():
            found.append((index, task))

    if not found:
        print("No matching tasks found.")
        return

    print("\nMatching Tasks:")

    for index, task in found:
        status = "✓" if task["done"] else " "

        print(f"{index}. [{status}] {task['title']}")