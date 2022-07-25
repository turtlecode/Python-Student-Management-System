import tkinter as tk
import sqlite3
from tkinter import ttk, messagebox

root = tk.Tk()
root.title("Management")

connection = sqlite3.connect("management.db")

TABLE_NAME = "management_table"
STUDENT_ID = "student_id"
STUDENT_NAME = "student_name"
STUDENT_COLLEGE = "student_college"
STUDENT_ADDRESS = "student_address"
STUDENT_PHONE = "student_phone"

connection.execute("CREATE TABLE IF NOT EXISTS " + TABLE_NAME + " (" + STUDENT_ID +
            " INTEGER PRIMARY KEY AUTOINCREMENT, " +
            STUDENT_NAME + " TEXT, " + STUDENT_COLLEGE + " TEXT, " +
            STUDENT_ADDRESS + " TEXT, " + STUDENT_PHONE + " INTEGER);" )

appLabel = tk.Label(root, text="Student Management System", fg="#06a099",width=35)
appLabel.config(font=("Sylfaen", 30))
appLabel.grid(row=0, columnspan=2, padx=(10,10), pady=(30,0))

class Student:
    studentName = ""
    collegeName = ""
    phoneNumber = 0
    address = ""

    def __init__(self, studentName, collegeName, phoneNumber, address):
        self.studentName = studentName
        self.collegeName = collegeName
        self.phoneNumber = phoneNumber
        self.address = address

nameLabel = tk.Label(root, text="Enter your name", width=40, anchor='w',
                font= ("Sylfaen",12)).grid(row=1, column=0, padx=(10,0),
                pady=(30,0))

collegeLabel = tk.Label(root, text="Enter your college", width=40, anchor='w',
                font= ("Sylfaen",12)).grid(row=2, column=0, padx=(10,0),
                pady=(30,0))

phoneLabel = tk.Label(root, text="Enter your phone", width=40, anchor='w',
                font= ("Sylfaen",12)).grid(row=3, column=0, padx=(10,0),
                pady=(30,0))

addressLabel = tk.Label(root, text="Enter your address", width=40, anchor='w',
                font= ("Sylfaen",12)).grid(row=4, column=0, padx=(10,0),
                pady=(30,0))

nameEntry = tk.Entry(root, width=30)
nameEntry.grid(row=1, column=1, padx=(0,10), pady=(30,20))

collegeEntry = tk.Entry(root, width=30)
collegeEntry.grid(row=2, column=1, padx=(0,10), pady=20)

phoneEntry = tk.Entry(root, width=30)
phoneEntry.grid(row=3, column=1, padx=(0,10), pady= 20)

addressEntry = tk.Entry(root, width=30)
addressEntry.grid(row=4, column=1, padx=(0,10), pady=20)

def takeNameInput():
    global nameEntry, collegeEntry, phoneEntry, addressEntry
    global list
    global TABLE_NAME, STUDENT_NAME, STUDENT_COLLEGE, STUDENT_ADDRESS, STUDENT_PHONE
    username = nameEntry.get()
    nameEntry.delete(0, tk.END)
    collegeName = collegeEntry.get()
    collegeEntry.delete(0, tk.END)
    phone = int(phoneEntry.get())
    phoneEntry.delete(0, tk.END)
    address = addressEntry.get()
    addressEntry.delete(0, tk.END)

    connection.execute("INSERT INTO " + TABLE_NAME + " ( " + STUDENT_NAME + ", " +
                    STUDENT_COLLEGE + ", " + STUDENT_ADDRESS + ", " +
                    STUDENT_PHONE + " ) VALUES ( '"
                    + username + "', '" + collegeName + "', '" +
                    address + "', " + str(phone) + " );")
    connection.commit()
    messagebox.showinfo("Success", "Data Saved Successfully.")

def destroyRootWindow():
    secondWindow = tk.Tk()

    secondWindow.title("Display results")

    appLabel = tk.Label(secondWindow, text="Student Management System",
                    fg="#06a099", width=40)
    appLabel.config(font=("Sylfaen",30))
    appLabel.pack()

    tree = ttk.Treeview(secondWindow)
    tree["columns"] = ("one", "two", "three", "four")

    tree.heading("one", text="Student Name")
    tree.heading("two", text="College Name")
    tree.heading("three", text="Address")
    tree.heading("four", text="Phone Number")

    cursor = connection.execute("SELECT * FROM " + TABLE_NAME + ";")
    i = 0

    for row in cursor:
        tree.insert('', i, text="Student " + str(row[0]),
        values=(row[1], row[2],
                row[3], row[4]))
        i = i + 1

    tree.pack()
    secondWindow.mainloop()

button = tk.Button(root, text="Take Input", command=lambda :takeNameInput())
button.grid(row=5, column=0, pady=20)

displayButton = tk.Button(root, text="Display result",
command=lambda : destroyRootWindow())
displayButton.grid(row=5, column=1)

root.mainloop()