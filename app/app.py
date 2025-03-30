from flask import Flask, jsonify
import mysql.connector
import time

app = Flask(__name__)

# รอ MySQL ให้พร้อม
while True:
    try:
        db = mysql.connector.connect(
            host="db_server",
            user="root",
            password="rootpassword",
            database="unidb"
        )
        break  # ออกจาก loop ถ้าเชื่อมต่อสำเร็จ
    except mysql.connector.Error:
        print("Waiting for database...")
        time.sleep(3)

@app.route('/')
def hello():
    return "Hello from Flask Backend!"

@app.route('/api/users')
def get_users():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM student")
    users = cursor.fetchall()
    return jsonify(users)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

