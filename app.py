from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    try:
        # Try connecting to MySQL (works locally)
        db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="A1HnZv16*",
            database="portfolio"
        )
        cursor = db.cursor()

        sql = "INSERT INTO contacts (name,email) VALUES (%s,%s)"
        val = (name, email)

        cursor.execute(sql, val)
        db.commit()

        return "Data Stored Successfully (Local DB)"

    except:
        # If DB fails on Render
        return "Form submitted (DB not connected on cloud)"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)