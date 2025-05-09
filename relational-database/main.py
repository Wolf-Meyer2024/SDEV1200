from flask import Flask, request, redirect, render_template_string
import sqlite3
import os

app = Flask(__name__)

# Initialize database and tables
def init_db():
    conn = sqlite3.connect('student_info.db')
    conn.execute("PRAGMA foreign_keys = ON")
    c = conn.cursor()

    # Create tables
    c.execute('''CREATE TABLE IF NOT EXISTS Majors (
                    MajorID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT NOT NULL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS Departments (
                    DeptID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT NOT NULL)''')

    c.execute('''CREATE TABLE IF NOT EXISTS Students (
                    StudentID INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name TEXT NOT NULL,
                    MajorID INTEGER,
                    DeptID INTEGER,
                    FOREIGN KEY (MajorID) REFERENCES Majors(MajorID),
                    FOREIGN KEY (DeptID) REFERENCES Departments(DeptID))''')

    # Add sample data if empty
    if not c.execute('SELECT 1 FROM Majors').fetchone():
        c.execute("INSERT INTO Majors (Name) VALUES ('Computer Science'), ('Mathematics')")
    if not c.execute('SELECT 1 FROM Departments').fetchone():
        c.execute("INSERT INTO Departments (Name) VALUES ('STEM'), ('Arts')")

    conn.commit()
    conn.close()

# Get connection with row access by name
def get_db_connection():
    conn = sqlite3.connect('student_info.db')
    conn.row_factory = sqlite3.Row
    return conn

# HTML template embedded as a string
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
    <title>Student DB</title>
    <style>
        body { font-family: Arial; margin: 40px; }
        table { border-collapse: collapse; width: 60%; margin-bottom: 20px; }
        th, td { padding: 8px 12px; border: 1px solid #ccc; }
    </style>
</head>
<body>
    <h1>Student Records</h1>
    <table>
        <tr><th>ID</th><th>Name</th><th>Major</th><th>Department</th></tr>
        {% for s in students %}
        <tr>
            <td>{{ s.StudentID }}</td>
            <td>{{ s.Name }}</td>
            <td>{{ s.Major or 'N/A' }}</td>
            <td>{{ s.Department or 'N/A' }}</td>
        </tr>
        {% endfor %}
    </table>

    <h2>Add Student</h2>
    <form method="POST" action="/add">
        Name: <input type="text" name="name" required><br><br>
        Major:
        <select name="major_id">
            {% for m in majors %}
            <option value="{{ m.MajorID }}">{{ m.Name }}</option>
            {% endfor %}
        </select><br><br>
        Department:
        <select name="dept_id">
            {% for d in departments %}
            <option value="{{ d.DeptID }}">{{ d.Name }}</option>
            {% endfor %}
        </select><br><br>
        <button type="submit">Add Student</button>
    </form>
</body>
</html>
'''

@app.route('/')
def index():
    conn = get_db_connection()
    students = conn.execute('''
        SELECT Students.StudentID, Students.Name,
               Majors.Name AS Major,
               Departments.Name AS Department
        FROM Students
        LEFT JOIN Majors ON Students.MajorID = Majors.MajorID
        LEFT JOIN Departments ON Students.DeptID = Departments.DeptID
    ''').fetchall()
    majors = conn.execute('SELECT * FROM Majors').fetchall()
    departments = conn.execute('SELECT * FROM Departments').fetchall()
    conn.close()
    return render_template_string(HTML_TEMPLATE, students=students, majors=majors, departments=departments)

@app.route('/add', methods=['POST'])
def add_student():
    name = request.form['name']
    major_id = request.form['major_id']
    dept_id = request.form['dept_id']
    conn = get_db_connection()
    conn.execute('INSERT INTO Students (Name, MajorID, DeptID) VALUES (?, ?, ?)',
                 (name, major_id, dept_id))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    if not os.path.exists('student_info.db'):
        init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
