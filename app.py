from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

def connect():
    return sqlite3.connect("portfolio.db")

def create_tables():
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS contact(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT,
        message TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS projects(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS certificates(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        description TEXT
    )
    """)

    conn.commit()
    conn.close()

create_tables()

@app.route("/contact", methods=["POST"])
def contact():
    data = request.json

    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO contact(name,email,message) VALUES(?,?,?)",
        (data["name"], data["email"], data["message"])
    )

    conn.commit()
    conn.close()

    return jsonify({"message":"Message Sent Successfully"})

@app.route("/projects", methods=["GET"])
def projects():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT title,description FROM projects")
    data = cur.fetchall()

    conn.close()

    return jsonify(data)

@app.route("/certificates", methods=["GET"])
def certificates():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT title,description FROM certificates")
    data = cur.fetchall()

    conn.close()

    return jsonify(data)

if __name__=="__main__":
    app.run(debug=True)
from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

# Create database
def init_db():
    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contact (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        message TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projects (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT NOT NULL
    )
    """)

    conn.commit()
    conn.close()

init_db()

# Home Route
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to B. Sai Tejaswi's Portfolio Backend"
    })

# Contact Form API
@app.route("/contact", methods=["POST"])
def contact():
    data = request.get_json()

    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO contact (name, email, message) VALUES (?, ?, ?)",
        (data["name"], data["email"], data["message"])
    )

    conn.commit()
    conn.close()

    return jsonify({"success": True, "message": "Message sent successfully!"})

# Get Projects API
@app.route("/projects", methods=["GET"])
def get_projects():

    conn = sqlite3.connect("portfolio.db")
    cursor = conn.cursor()

    cursor.execute("SELECT title, description FROM projects")
    projects = cursor.fetchall()

    conn.close()

    result = []

    for project in projects:
        result.append({
            "title": project[0],
            "description": project[1]
        })

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)