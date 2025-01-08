import json
from todo_database import ToDoList

def lambda_handler(event, context):
    output = []
    to_do_list = ToDoList()

    my_event = json.loads(event["body"]) # get event from curl/user

    operation = my_event["operation"]
    arguments = my_event["arguments"]

    output.append("Welcome to your To Do List program! :D")
    if operation == "view": # get tasks
        result = to_do_list.get_tasks()
        if len(result) == 0:
            output.append("Your To Do list is empty.")
        else:
            output.append("Here's your To Do list:")
        for i, task in enumerate(result):
            task_status_symbol = "❌"
            if task[2] == True:
                task_status_symbol = "✅"
            output.append(f"{task[0]}: {task[1]} {task_status_symbol}")
    elif operation == "add": # add tasks
        output.append("You have added the following tasks to the list:")
        for task in arguments:
            to_do_list.add_task(task)
            output.append(f" - {task}")
    elif operation == "remove": # remove tasks
        for rowid in arguments:
            try:
                to_do_list.remove_task(rowid)
                output.append(f"Task at '{rowid}' removed.")
            except Exception:
                output.append(f"Task at '{rowid}' doesn't exist!")
    elif operation == "toggle": # toggle tasks
        for rowid in arguments:
            try:
                to_do_list.toggle_task(rowid)
                output.append(f"Task at '{rowid}' toggled.")
            except Exception:
                output.append(f"Task at '{rowid}' doesn't exist!")
    elif operation == "clear": # clear entire task list
        to_do_list.clear_list()
        output.append("List has been cleared!")
    else:
        output.append("Invalid option. Try again.")
        
    return {
        'statusCode': 200,
        'body': "\n".join(output) # get tasks and send back to curl/user (should be the response)
    }

if __name__ == "__main__":
    from dotenv import load_dotenv
    load_dotenv()
    event = {}  
    event['body'] = """
    {
        "operation": "view",
        "arguments": ["7", "8", "9"]
    }
    """
    print(lambda_handler(event, None)['body'])