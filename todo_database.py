import os
import psycopg2 as pg

class postgreSQL:
    def __init__(self, should_recreate=False):
        self.conn = pg.connect(
            host=os.environ['db_host'],
            database=os.environ['db_name'],
            user=os.environ['db_username'],
            password=os.environ['db_password'],
            port="5432"
        )
        cursor = self.conn.cursor()
        if should_recreate:
            cursor.execute("DROP TABLE IF EXISTS todo;")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS todo (
            id SERIAL PRIMARY KEY,
            taskName varchar(255),
            checked bool
        )
        """)
        self.conn.commit()

    def get_all_tasks(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM todo ORDER BY id")
        return cursor.fetchall()

    def create_task(self, task_name):
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO todo (taskName, checked) VALUES (%s, False)", (task_name,))
        self.conn.commit()

    def update_task(self, rowid, checked):
        cursor = self.conn.cursor()
        cursor.execute("UPDATE todo SET checked = %s WHERE id = %s", (checked, rowid))
        self.conn.commit()

    def delete_task(self, rowid):
        cursor = self.conn.cursor()
        if len(self.get_task_by_id(rowid)) == 1:
            cursor.execute("DELETE FROM todo WHERE id = %s", (rowid,))
            self.conn.commit()
        else:
            raise Exception("Invalid row id")

    def get_task_by_id(self, rowid):
        cursor = self.conn.cursor()
        cursor.execute("SELECT * FROM todo where id = %s", (rowid,))
        return cursor.fetchall()

    def clear_table(self):
        cursor = self.conn.cursor()
        cursor.execute("DROP TABLE todo")
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS todo (
            id SERIAL PRIMARY KEY,
            taskName varchar(255),
            checked bool
        )
        """)
        self.conn.commit()

class ToDoList:
    def __init__(self):
        self.db = postgreSQL()

    def get_tasks(self):
        return self.db.get_all_tasks()

    def add_task(self, task_name):
        self.db.create_task(task_name)

    def remove_task(self, rowid):
        self.db.delete_task(rowid)

    def toggle_task(self, rowid):
        result = self.db.get_task_by_id(rowid)
        if len(result) != 1:
            raise Exception("Invalid row id!")
        task = result[0]
        new_status = not task[2]
        self.db.update_task(rowid, new_status)

    def clear_list(self):
        self.db.clear_table()

