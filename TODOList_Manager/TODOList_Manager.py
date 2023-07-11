import sqlite3

# Establish a connection to the SQLite database
conn = sqlite3.connect('todo.db')

# Create a cursor object
cursor = conn.cursor()

# Execute SQL statements
# TODO: Add the SQL statements here
create_table_query = '''
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task TEXT NOT NULL,
        completed INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP)
'''
cursor.execute(create_table_query)

# Insert a task into the table
insert_task_query = "INSERT INTO tasks (task) VALUES ('Complete project')"
cursor.execute(insert_task_query)
tasks = cursor.fetchall()

# Print the tasks
for task in tasks:
    print(task)

# Commit the changes to the database
conn.commit()

# Close the database connection
conn.close()
