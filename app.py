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