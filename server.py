from flask import Flask, render_template, request
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
@app.route('/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/guestbook', methods=['POST'])
def guestbook():
    name = request.form.get('name')
    message = request.form.get('message')
    
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    cur = conn.cursor()
    
    
    cur.execute("CREATE TABLE IF NOT EXISTS GUEST(id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, message TEXT NOT NULL)")
    conn.commit()
    
    
    cur.execute('INSERT INTO GUEST (name, message) VALUES (%s, %s)', (name, message))
    conn.commit()
    
    conn.close()
    
    return render_template('hello.html', name=name, message=message)

@app.route('/getmessages', methods=['GET'])
def getmessages():
    conn = psycopg2.connect(os.environ['DATABASE_URL'])
    cur = conn.cursor()
    
    cur.execute("SELECT name, message FROM GUEST")
    rows = cur.fetchall()
    
    conn.close()
    
    # Convert rows to list of dictionaries for easier template access
    messages = [{'name': row[0], 'message': row[1]} for row in rows]
    
    return render_template('hello.html', messages=messages)