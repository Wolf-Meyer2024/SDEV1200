#
# Name Wolfgang Meyer
# Date 5-4-25
# Relational Database Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.

# Import the sqlite3 module to work with SQLite databases in Python
import sqlite3

# Function to create the database and required tables
def create_database():
    # Connect to (or create) the database file named 'student_info.db'
    conn = sqlite3.connect('student_info.db')
    
    # Enable foreign key constraints for referential integrity
    conn.execute("PRAGMA foreign_keys = ON")
    
    # Create a cursor object to execute SQL commands
    c = conn.cursor()

    # Create the Majors table if it doesn't already exist
    c.execute('''CREATE TABLE IF NOT EXISTS Majors (
                    MajorID INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL)''')

    # Create the Departments table if it doesn't already exist
    c.execute('''CREATE TABLE IF NOT EXISTS Departments (
                    DeptID INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL)''')

    # Create the Students table with foreign keys to Majors and Departments
    c.execute('''CREATE TABLE IF NOT EXISTS Students (
                    StudentID INTEGER PRIMARY KEY,
                    Name TEXT NOT NULL,
                    MajorID INTEGER,
                    DeptID INTEGER,
                    FOREIGN KEY (MajorID) REFERENCES Majors(MajorID),
                    FOREIGN KEY (DeptID) REFERENCES Departments(DeptID))''')

    # Save changes and close the database connection
    conn.commit()
    conn.close()

# Call the function to set up the database and tables
create_database()


# ---------------- MAJOR FUNCTIONS ----------------

# Add a new major to the Majors table
def add_major(name):
    with sqlite3.connect('student_info.db') as conn:
        conn.execute("INSERT INTO Majors (Name) VALUES (?)", (name,))
        print("Major added.")

# Search for a major by its ID
def search_major(major_id):
    with sqlite3.connect('student_info.db') as conn:
        result = conn.execute("SELECT * FROM Majors WHERE MajorID = ?", (major_id,)).fetchone()
        print("Result:", result)

# Update the name of an existing major by its ID
def update_major(major_id, new_name):
    with sqlite3.connect('student_info.db') as conn:
        conn.execute("UPDATE Majors SET Name = ? WHERE MajorID = ?", (new_name, major_id))
        print("Major updated.")

# Delete a major by its ID
def delete_major(major_id):
    with sqlite3.connect('student_info.db') as conn:
        conn.execute("DELETE FROM Majors WHERE MajorID = ?", (major_id,))
        print("Major deleted.")

# List all majors in the table
def list_majors():
    with sqlite3.connect('student_info.db') as conn:
        results = conn.execute("SELECT * FROM Majors").fetchall()
        for row in results:
            print(row)


# ---------------- DEPARTMENT FUNCTIONS ----------------

# Add a new department to the Departments table
def add_department(name):
    with sqlite3.connect('student_info.db') as conn:
        conn.execute("INSERT INTO Departments (Name) VALUES (?)", (name,))
        print("Department added.")

# Search for a department by its ID
def search_department(dept_id):
    with sqlite3.connect('student_info.db') as conn:
        result = conn.execute("SELECT * FROM Departments WHERE DeptID = ?", (dept_id,)).fetchone()
        print("Result:", result)

# Update the name of an existing department by its ID
def update_department(dept_id, new_name):
    with sqlite3.connect('student_info.db') as conn:
        conn.execute("UPDATE Departments SET Name = ? WHERE DeptID = ?", (new_name, dept_id))
        print("Department updated.")

# Delete a department by its ID
def delete_department(dept_id):
    with sqlite3.connect('student_info.db') as conn:
        conn.execute("DELETE FROM Departments WHERE DeptID = ?", (dept_id,))
        print("Department deleted.")

# List all departments in the table
def list_departments():
    with sqlite3.connect('student_info.db') as conn:
        results = conn.execute("SELECT * FROM Departments").fetchall()
        for row in results:
            print(row)


# ---------------- STUDENT FUNCTIONS ----------------

# Add a new student, ensuring valid major and department IDs are used
def add_student(name, major_id, dept_id):
    with sqlite3.connect('student_info.db') as conn:
        conn.execute("PRAGMA foreign_keys = ON")  # Ensure foreign key constraints are enforced
        conn.execute("INSERT INTO Students (Name, MajorID, DeptID) VALUES (?, ?, ?)", (name, major_id, dept_id))
        print("Student added.")

# Search for a student by their ID
def search_student(student_id):
    with sqlite3.connect('student_info.db') as conn:
        result = conn.execute("SELECT * FROM Students WHERE StudentID = ?", (student_id,)).fetchone()
        print("Result:", result)

# Update a student's information
def update_student(student_id, new_name, new_major_id, new_dept_id):
    with sqlite3.connect('student_info.db') as conn:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.execute("UPDATE Students SET Name = ?, MajorID = ?, DeptID = ? WHERE StudentID = ?",
                     (new_name, new_major_id, new_dept_id, student_id))
        print("Student updated.")

# Delete a student by their ID
def delete_student(student_id):
    with sqlite3.connect('student_info.db') as conn:
        conn.execute("DELETE FROM Students WHERE StudentID = ?", (student_id,))
        print("Student deleted.")

# List all students in the table
def list_students():
    with sqlite3.connect('student_info.db') as conn:
        results = conn.execute("SELECT * FROM Students").fetchall()
        for row in results:
            print(row)
