import sqlite3

# The unique ID of the QR code you want to update
unique_id = input("Enter the unique ID of the QR code to update: ").strip()

# New status to set ('active' or 'inactive')
new_status = input("Enter the new status ('active' or 'inactive'): ").strip().lower()

# Connect to the database with a 5-second timeout to avoid locking issues
conn = sqlite3.connect('qrcodes.db', timeout=5)
cursor = conn.cursor()

# Update the status of the specified QR code
cursor.execute("UPDATE qr_codes SET status = ? WHERE id = ?", (new_status, unique_id))

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"Status of QR code {unique_id} updated to '{new_status}'.")
