import sqlite3

# Connect to the database
conn = sqlite3.connect('qrcodes.db')
cursor = conn.cursor()

# Select all entries in the qr_codes table
cursor.execute("SELECT * FROM qr_codes")
rows = cursor.fetchall()

# Close the connection
conn.close()

# Print out the contents of the table
if rows:
    print("Contents of the qr_codes table:")
    for row in rows:
        print(f"ID: {row[0]}, Status: {row[1]}")
else:
    print("The qr_codes table is empty.")
