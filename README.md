# To-Do List App

## Overview
This is a serverless To-Do List application using AWS Lambda and PostgreSQL. It allows users to:
- View tasks
- Add tasks
- Remove tasks
- Toggle task completion
- Clear the list

## Setup Instructions
1. Clone the repository.
2. Install the required Python software using `pip install -r requirements.txt`.
3. Configure your own database by setting the following environment variables:
   - `db_host`
   - `db_name`
   - `db_username`
   - `db_password`
4. Run the program using:
   ```bash
   python3 lambda_handler.py

## How It's Used (Locally)
- This program runs by processing an event in JSON format. Here's an example:
    
```bash
{
  "operation": "add",
  "arguments": ["wake up", "brush teeth", "meditate"]
}
```
## Technologies Used
- Python
- PostgreSQL
- AWS Lambda