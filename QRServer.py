from flask import Flask, redirect, abort
import sqlite3

app = Flask(__name__)

def get_qr_data(unique_id):
    # Connect to the database and retrieve the client's URL and status
    conn = sqlite3.connect('qrcodes.db')
    cursor = conn.cursor()
    cursor.execute("SELECT client_url, status FROM qr_codes WHERE id=?", (unique_id,))
    result = cursor.fetchone()
    conn.close()
    return result if result else (None, None)

@app.route('/resource/<unique_id>')
def resource(unique_id):
    # Check the client's URL and status of the QR code ID
    client_url, status = get_qr_data(unique_id)

    if client_url and status == 'active':
        return redirect(client_url)  # Redirect to the client’s URL if active
    elif status == 'inactive':
        return "This QR code is inactive. Please contact support for access."
    else:
        return abort(404)  # If ID not found, return a 404 error

if __name__ == '__main__':
    app.run(debug=True)
