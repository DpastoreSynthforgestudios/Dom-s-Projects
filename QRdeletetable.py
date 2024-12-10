import sqlite3

# Connect to the database
conn = sqlite3.connect('qrcodes.db')
cursor = conn.cursor()

# Clear all entries in the qr_codes table
cursor.execute("DELETE FROM qr_codes")
conn.commit()

print("All entries in the qr_codes table have been cleared.")

# Now, check if the table is empty
cursor.execute("SELECT * FROM qr_codes")
rows = cursor.fetchall()

# Close the connection
conn.close()

# Print out the contents of the table to confirm it's empty
if rows:
    print("Contents of the qr_codes table after clearing:")
    for row in rows:
        print(f"ID: {row[0]}, Status: {row[1]}")
else:
    print("The qr_codes table is now empty.")

