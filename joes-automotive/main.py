#
# Name Wolfgang Meyer
# Date 4-1-25
# Joe's Automotive Programming Project
# SDEV 1200
#
# Use comments liberally throughout the program.  
# The code below was auto-generated. 
# Delete/adjust unnecessary code.

import tkinter as tk
from tkinter import messagebox

def calculate_total():
    total = 0
    for var, price in services:
        if var.get():
            total += price
    total_label.config(text=f"Total Charges: ${total:.2f}")

# Create the main window
root = tk.Tk()
root.title("Joe's Automotive Services")
root.geometry("350x350")

# Define services and prices
services = [
    (tk.BooleanVar(), 30.00),  # Oil Change
    (tk.BooleanVar(), 20.00),  # Lube Job
    (tk.BooleanVar(), 40.00),  # Radiator Flush
    (tk.BooleanVar(), 100.00), # Transmission Flush
    (tk.BooleanVar(), 35.00),  # Inspection
    (tk.BooleanVar(), 200.00), # Muffler Replacement
    (tk.BooleanVar(), 20.00)   # Tire Rotation
]

service_labels = [
    "Oil Change - $30.00",
    "Lube Job - $20.00",
    "Radiator Flush - $40.00",
    "Transmission Flush - $100.00",
    "Inspection - $35.00",
    "Muffler Replacement - $200.00",
    "Tire Rotation - $20.00"
]

# Frame to hold checkboxes
frame = tk.Frame(root)
frame.pack(pady=10, padx=10)

# Create checkboxes
for i, (var, price) in enumerate(services):
    tk.Checkbutton(frame, text=service_labels[i], variable=var).pack(anchor='w')

# Calculate button
calculate_button = tk.Button(root, text="Calculate Total", command=calculate_total)
calculate_button.pack(pady=10)

# Label to display total
total_label = tk.Label(root, text="Total Charges: $0.00", font=("Arial", 12, "bold"))
total_label.pack()

# Run the application
root.mainloop()
