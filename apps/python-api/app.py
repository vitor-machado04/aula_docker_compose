from flask import Flask
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()

app = Flask(__name__)

@app.route('/')
def hello():
    db = mysql.connector.connect(
        user="root",
        host="dbmysql",
        password="root",
        database="flaskdb",
    )
    
    cursor = db.cursor()
    cursor.execute("SELECT 'Hello from Flask and MySQL!'")
    result = cursor.fetchone()
    cursor.close()
    db.close()
    return result[0]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
