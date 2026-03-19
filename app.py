from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="A1HnZv16*",
    database="portfolio"
)

cursor = db.cursor()

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']

    sql = "INSERT INTO contacts (name,email) VALUES (%s,%s)"
    val = (name, email)

    cursor.execute(sql, val)
    db.commit()

    return "Data Stored Successfully"

if __name__ == "__main__":
    app.run(debug=True)