# To-Do List App

## Overview
This is a personal project that started off as practice for object oriented programming using classes.
It then transformed into a serverless To-Do List application using AWS Lambda and PostgreSQL. It allows users to:
- View tasks
- Add tasks
- Remove tasks
- Toggle task completion
- Clear the list

## Features
- **Serverless Design:** The app leverages AWS Lambda for scalability and minimal server maintenance.
- **Database Integration:** Uses PostgreSQL to store and manage tasks persistently.
- **Event-Based Operations:** Processes user actions via structured JSON events.
---
## Setup Instructions
Follow these steps to set up the project:

1. **Clone the repository.**
```bash
git clone https://github.com/haimiee/toDoList
cd toDoList
```
2. **Install Dependencies:** Use `pip` to install the required Python packages:
```bash
 pip install -r requirements.txt
 ```
3. **Configure environment variables**: Create a `.env` file in the root directory and add your database credentials. Example:
```
db_host=...
db_name=...
db_username=...
db_password=...
```
*Note*: I learned it's good to make sure `.env` is included in `.gitignore` to avoid exposing sensitive information.

4. **Run the program locally**: Execute the main Lambda handler file.
   ```bash
   python3 lambda_handler.py
---
## How to Use the App
The program processes tasks based on structured JSON input. Here's a breakdown of supported operations:

### 1. Adding Tasks
The `add` operation in the operation field adds tasks to the database. The `arguments` field accepts an array of strings representing the task names to be added.

### 2. Viewing Tasks
The `view` operation lists all tasks currently in the database. No arguments are needed.

### 3. Removing Tasks
The `remove` operation deletes specific tasks from the database using their task IDs. The `arguments` field should include an array of task IDs in string format to be removed.

### 4. Clearing the List
The `clear` operation removes all tasks from the database. No arguments are required.

### 5. Toggling Task Completion
The `toggle` operation marks tasks as completed (`✅`) or incomplete (`❌`). The `arguments` field should include an array of task IDs in string format to be toggled.

---
## Examples

**Input code:**
```json
{
  "operation": "add",
  "arguments": ["wake up", "brush teeth", "meditate"]
}
```
** Output to the console:
```
Welcome to your To Do List program! :D
You have added the following tasks to the list:
 - wake up
 - brush teeth
 - meditate
```
---


## Project Highlights and Skills Gained

This To-Do List project began as a simple exercise in object-oriented programming and evolved into a robust, serverless application. Along the way, I developed key skills and implemented features such as:

- **Object-Oriented Design:** Created the foundation using Python classes to manage tasks.
- **Database Integration:** Learned to use PostgreSQL for persistent storage, both locally and online.
- **API Development:** Built and deployed a serverless API on AWS Lambda to handle task operations.
- **Event Handling and JSON:** Processed structured JSON events to manage tasks flexibly.
- **Secure Development Practices:** Used `.env` files to safeguard sensitive credentials.
- **Scalability and Performance:** Focused on designing a scalable, serverless architecture.

This project was a turning point in my programming journey, connecting theory and practice to create a functional, real-world application.

