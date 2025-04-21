#
# Name Wolfgang Meyer
# Date
# Phone Book Database Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program.

# phonebook_crud.py
# setup_phonebook.py
import sqlite3

def create_phonebook_db():
    conn = sqlite3.connect('phonebook.db')
    cur = conn.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS Entries (
                    Name TEXT PRIMARY KEY,
                    PhoneNumber TEXT
                )''')

    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_phonebook_db()
    print("phonebook.db and Entries table created.")


def connect_db():
    return sqlite3.connect('phonebook.db')

def add_entry(cur):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    try:
        cur.execute("INSERT INTO Entries (Name, PhoneNumber) VALUES (?, ?)", (name, phone))
        print("Entry added successfully.")
    except sqlite3.IntegrityError:
        print("That name already exists in the phonebook.")

def lookup_entry(cur):
    name = input("Enter name to look up: ")
    cur.execute("SELECT PhoneNumber FROM Entries WHERE Name = ?", (name,))
    result = cur.fetchone()
    if result:
        print(f"{name}'s phone number is: {result[0]}")
    else:
        print("No entry found for that name.")

def update_entry(cur):
    name = input("Enter name to update: ")
    new_phone = input("Enter new phone number: ")
    cur.execute("UPDATE Entries SET PhoneNumber = ? WHERE Name = ?", (new_phone, name))
    if cur.rowcount > 0:
        print("Phone number updated.")
    else:
        print("No entry found for that name.")

def delete_entry(cur):
    name = input("Enter name to delete: ")
    cur.execute("DELETE FROM Entries WHERE Name = ?", (name,))
    if cur.rowcount > 0:
        print("Entry deleted.")
    else:
        print("No entry found for that name.")

def show_all_entries(cur):
    cur.execute("SELECT * FROM Entries ORDER BY Name")
    rows = cur.fetchall()
    if rows:
        print("\nPhonebook Entries:")
        for row in rows:
            print(f"{row[0]:20} {row[1]}")
    else:
        print("The phonebook is empty.")

def main():
    conn = connect_db()
    cur = conn.cursor()

    while True:
        print("\nPhonebook Menu:")
        print("1. Add Entry")
        print("2. Look Up Phone Number")
        print("3. Update Phone Number")
        print("4. Delete Entry")
        print("5. Show All Entries")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_entry(cur)
        elif choice == '2':
            lookup_entry(cur)
        elif choice == '3':
            update_entry(cur)
        elif choice == '4':
            delete_entry(cur)
        elif choice == '5':
            show_all_entries(cur)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please select again.")

        conn.commit()

    conn.close()
    print("Goodbye!")

if __name__ == '__main__':
    main()
