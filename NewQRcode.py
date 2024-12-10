import qrcode
import sqlite3
import uuid

# Step 1: Collect the client URL
client_url = input("Enter the client's URL (e.g., https://SynthForgeStudios.com): ").strip()

# Step 2: Generate a unique ID for the QR code
unique_id = str(uuid.uuid4())
qr_url = f"http://127.0.0.1:5000/resource/{unique_id}"  # Change to your public server URL when hosted

# Step 3: Generate the QR code pointing to the server URL
qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(qr_url)
image = qr.make_image(fill_color='black', back_color='white')

# Step 4: Save the QR code as a PNG file
filename = f"{unique_id}.png"
image.save(filename)
print(f"QR code saved as {filename} with URL: {qr_url}")

# Step 5: Store the unique ID, client URL, and status in the database
conn = sqlite3.connect('qrcodes.db')
cursor = conn.cursor()

# Insert the new QR code ID with the client's URL and an initial status of 'active'
status = 'active'
cursor.execute("INSERT INTO qr_codes (id, status, client_url) VALUES (?, ?, ?)", (unique_id, status, client_url))

# Commit the changes and close the connection
conn.commit()
conn.close()

print(f"QR code for {client_url} saved to the database with ID {unique_id} and status 'active'.")
