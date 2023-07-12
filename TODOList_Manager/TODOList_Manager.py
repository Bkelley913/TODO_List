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

select_query = "SELECT * FROM tasks"
cursor.execute(select_query)

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

def display_task():
    # Establish a connection to the SQLite database
    conn = sqlite3.connect('todo.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Select all rows from the tasks table
    select_query = "SELECT * FROM tasks"
    cursor.execute(select_query)
    
    # Fetch all the rows as a list of tuples
    rows = cursor.fetchall()

    # Print the data
    for row in rows:
        print(row)

    # Close the database connection
    conn.close()

# Call the function to display the tasks
display_task()

def add_task(*args):
    # Establish a connection to the SQLite database
    conn = sqlite3.connect('todo.db')

    # Create a cursor object
    cursor = conn.cursor()

    # Execute the INSERT statement
    for task in args:
        insert_query = "INSERT INTO tasks (task) VALUES (TEXT)"
        cursor.execute(insert_query, (task,))

    # Commit the changes to the database
    conn.commit()

    # Close the database connection
    conn.close()

# Call the function to add multiple tasks
add_task("Complete project", "Review documentation", "Submit report")