import sqlite3

# Replace 'your_database.db' with the desired database file name
db_file = 'your_database.db'

# Connect to the database (this will create the file if it doesn't exist)
conn = sqlite3.connect(db_file)

# Close the connection
conn.close()

print(f"SQLite database file '{db_file}' created.")
