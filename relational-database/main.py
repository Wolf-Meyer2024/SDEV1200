import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox

# ---------- Database Setup ----------
DB_NAME = 'student_info.db'

def run_query(query, params=()):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute("PRAGMA foreign_keys = ON")
        cursor.execute(query, params)
        conn.commit()
        return cursor

# ---------- GUI ----------
class StudentDatabaseApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Info Management System")
        self.root.geometry("700x500")

        tab_control = ttk.Notebook(root)
        self.student_tab = ttk.Frame(tab_control)
        self.major_tab = ttk.Frame(tab_control)
        self.dept_tab = ttk.Frame(tab_control)

        tab_control.add(self.student_tab, text='Students')
        tab_control.add(self.major_tab, text='Majors')
        tab_control.add(self.dept_tab, text='Departments')
        tab_control.pack(expand=1, fill='both')

        self.build_student_tab()
        self.build_major_tab()
        self.build_department_tab()

    def build_student_tab(self):
        frame = self.student_tab

        ttk.Label(frame, text="Name").grid(row=0, column=0)
        self.student_name = ttk.Entry(frame)
        self.student_name.grid(row=0, column=1)

        ttk.Label(frame, text="MajorID").grid(row=1, column=0)
        self.student_major = ttk.Entry(frame)
        self.student_major.grid(row=1, column=1)

        ttk.Label(frame, text="DeptID").grid(row=2, column=0)
        self.student_dept = ttk.Entry(frame)
        self.student_dept.grid(row=2, column=1)

        ttk.Button(frame, text="Add Student", command=self.add_student).grid(row=3, column=0, columnspan=2, pady=5)
        self.student_tree = self.create_treeview(frame, ["ID", "Name", "MajorID", "DeptID"], 5)
        self.refresh_students()

    def add_student(self):
        name = self.student_name.get()
        major_id = self.student_major.get()
        dept_id = self.student_dept.get()
        if name and major_id and dept_id:
            try:
                run_query("INSERT INTO Students (Name, MajorID, DeptID) VALUES (?, ?, ?)",
                          (name, int(major_id), int(dept_id)))
                self.refresh_students()
                messagebox.showinfo("Success", "Student added!")
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showwarning("Missing Data", "Please fill out all fields.")

    def refresh_students(self):
        for i in self.student_tree.get_children():
            self.student_tree.delete(i)
        rows = run_query("SELECT * FROM Students").fetchall()
        for row in rows:
            self.student_tree.insert('', 'end', values=row)

    def build_major_tab(self):
        frame = self.major_tab

        ttk.Label(frame, text="Major Name").grid(row=0, column=0)
        self.major_name = ttk.Entry(frame)
        self.major_name.grid(row=0, column=1)

        ttk.Button(frame, text="Add Major", command=self.add_major).grid(row=1, column=0, columnspan=2)
        self.major_tree = self.create_treeview(frame, ["ID", "Name"], 2)
        self.refresh_majors()

    def add_major(self):
        name = self.major_name.get()
        if name:
            try:
                run_query("INSERT INTO Majors (Name) VALUES (?)", (name,))
                self.refresh_majors()
                messagebox.showinfo("Success", "Major added!")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def refresh_majors(self):
        for i in self.major_tree.get_children():
            self.major_tree.delete(i)
        rows = run_query("SELECT * FROM Majors").fetchall()
        for row in rows:
            self.major_tree.insert('', 'end', values=row)

    def build_department_tab(self):
        frame = self.dept_tab

        ttk.Label(frame, text="Department Name").grid(row=0, column=0)
        self.dept_name = ttk.Entry(frame)
        self.dept_name.grid(row=0, column=1)

        ttk.Button(frame, text="Add Department", command=self.add_department).grid(row=1, column=0, columnspan=2)
        self.dept_tree = self.create_treeview(frame, ["ID", "Name"], 2)
        self.refresh_departments()

    def add_department(self):
        name = self.dept_name.get()
        if name:
            try:
                run_query("INSERT INTO Departments (Name) VALUES (?)", (name,))
                self.refresh_departments()
                messagebox.showinfo("Success", "Department added!")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def refresh_departments(self):
        for i in self.dept_tree.get_children():
            self.dept_tree.delete(i)
        rows = run_query("SELECT * FROM Departments").fetchall()
        for row in rows:
            self.dept_tree.insert('', 'end', values=row)

    def create_treeview(self, parent, columns, row):
        tree = ttk.Treeview(parent, columns=columns, show='headings', height=10)
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=100)
        tree.grid(row=row, column=0, columnspan=2, pady=10)
        return tree


if __name__ == '__main__':
    root = tk.Tk()
    app = StudentDatabaseApp(root)
    root.mainloop()
