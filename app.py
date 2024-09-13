from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('todo.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS todos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        completed BOOLEAN DEFAULT 0
    )''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = get_db_connection()
    todos = conn.execute('SELECT * FROM todos ORDER BY id ASC').fetchall()
    conn.close()
    return render_template('index.html', todos=todos)

@app.route('/todos', methods=['POST'])
def add_todo():
    title = request.json['title']
    description = request.json.get('description')

    if not title:
        return jsonify({'error': 'Title is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO todos (title, description) VALUES (?, ?)', (title, description))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Todo added successfully'})

@app.route('/todos/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    title = request.json.get('title')
    description = request.json.get('description')
    completed = request.json.get('completed')

    conn = get_db_connection()
    cursor = conn.cursor()

    if title:
        cursor.execute('UPDATE todos SET title = ? WHERE id = ?', (title, todo_id))
    if description:
        cursor.execute('UPDATE todos SET description = ? WHERE id = ?', (description, todo_id))
    if completed is not None:
        cursor.execute('UPDATE todos SET completed = ? WHERE id = ?', (completed, todo_id))

    conn.commit()
    conn.close()

    return jsonify({'message': 'Todo updated successfully'})

@app.route('/todos/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM todos WHERE id = ?', (todo_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Todo deleted successfully'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)