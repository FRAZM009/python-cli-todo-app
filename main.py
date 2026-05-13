from task_manager import (
    view_tasks,
    add_task,
    complete_task,
    delete_task,
    search_tasks
)

from storage import load_tasks, save_tasks
from utils import clear_screen, pause


def show_menu():
    print("=" * 40)
    print("        CLI TODO APPLICATION")
    print("=" * 40)
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Complete Task")
    print("4. Delete Task")
    print("5. Search Tasks")
    print("6. Exit")
    print("=" * 40)


def main():
    tasks = load_tasks()

    while True:
        clear_screen()
        show_menu()

        choice = input("Choose an option: ").strip()

        if choice == "1":
            clear_screen()
            view_tasks(tasks)
            pause()

        elif choice == "2":
            clear_screen()
            add_task(tasks)
            save_tasks(tasks)
            pause()

        elif choice == "3":
            clear_screen()
            complete_task(tasks)
            save_tasks(tasks)
            pause()

        elif choice == "4":
            clear_screen()
            delete_task(tasks)
            save_tasks(tasks)
            pause()

        elif choice == "5":
            clear_screen()
            search_tasks(tasks)
            pause()

        elif choice == "6":
            save_tasks(tasks)
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option. Try again.")
            pause()


if __name__ == "__main__":
    main()