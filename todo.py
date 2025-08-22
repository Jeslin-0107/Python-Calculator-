todo_list = []

def show_task():
    if not todo_list:
        print("Not yet assigned")
    else:
        for i, task in enumerate(todo_list,1):
            print(f"{i}.{task}")

def add_task(task):
    todo_list.append(task)
    print("Task added")

def delete_task(index):
    if 0 < index <= len(todo_list):
        removed = todo_list.pop(index - 1)
        print(f"Deleted : {removed}")
    else :
        print("invalid task number")

while True:

    print("___Todo List___")
    print("1. Show task")
    print("2. Add task")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter your choice (1-4) : ")

    if choice == '1':
        show_task()
    elif choice == '2':
        task = input("Enter your task : ")
        add_task(task)
    elif choice == '3':
        idx = int(input("Enter the number to delete the task : "))
        delete_task(idx)
    elif choice == '4':
        print("Goodbye !!!")
        break


    