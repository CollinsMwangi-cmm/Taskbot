import json


tasks  = []
FILENAME  = "task.json"

# function for loading the task from the list into the file
def load_task():
    global tasks
    try:
        with open(FILENAME, "r") as file:
            tasks = json.load(file) # load the tasks from the file
    except FileNotFoundError:
        tasks = [] # return an empty list
    except json.JSONDecodeError:
        tasks = [] # handle empty or invalid JSON file

# function for saving the task in the list
def save_task():
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4) # save the tasks to the file



#function for adding a new task
def add_new_task(task: str):
    tasks.append({"Task":task, "Status":"pending"})
    save_task()
    return f" ✅'{task}' was added in the list "
    

#function for showing the list of task
def show_list():
    load_task()
    if not tasks:
        return "There is no any task currently"
    else:
        output = "\n".join([f"{i+1}. {t['Task']} - {t['Status']}" for i,t in enumerate(tasks)])
        return "Your to do list:\n" + output
        


def delete_task(index : int):
    load_task()
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index )
        save_task() 
        return f"task '{removed_task['Task']}' was removed"
    else:
        print( "❌ Task number was not found")  
        


def mark_task(index: int):
    load_task()
    if 0 <= index < len(tasks):
        tasks[index ]['Status'] = 'completed'
        save_task()
        return f"{tasks[index]['Task']} is marked as completed"
    else:
        return "❌ Task number was not found"




"""def main(): 
    load_task()
    print("Welcome to your to do list manager 📝")
    while True:
        print("-------------------------- \n \n ")
        print("Select one of the following below")
        print("1.Add a new task")
        print("2.Delete an existing task")
        print("3.Show available task")
        print("4.mark a task as completed")
        print("5.Exit")
        
        choice = input("what would you like? ")
        print("\n")
        if choice == "1":
            add_new_task()
        elif choice == "2":
            delete_task()
        elif choice == "3":
            show_list()
        elif choice == "4":
            mark_task()
        elif choice == "5":
            print("Existing the application")
            exit()
        else:
            print("Invalid output please select 1,2,3 or 4")
        print("goodbye👋👋")

main()"""