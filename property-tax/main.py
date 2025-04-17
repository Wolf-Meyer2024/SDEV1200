#
# Name Wolfgang Meyer
# Date 4-17-25
# Property Tax Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

import tkinter as tk
from tkinter import messagebox

def calculate_tax():
    try:
        actual_value = float(entry_actual.get())
        assessment_value = actual_value * 0.6
        property_tax = (assessment_value / 100) * 0.75

        label_assessment_value.config(text=f"Assessment Value: ${assessment_value:,.2f}")
        label_property_tax.config(text=f"Property Tax: ${property_tax:,.2f}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the actual value.")

# Create main window
root = tk.Tk()
root.title("Property Tax Calculator")

# Set window size and padding
root.geometry("350x200")
root.resizable(False, False)
root.configure(padx=20, pady=20)

# Input for actual property value
label_actual = tk.Label(root, text="Enter Actual Property Value ($):")
label_actual.pack()

entry_actual = tk.Entry(root)
entry_actual.pack()

# Calculate Button
button_calculate = tk.Button(root, text="Calculate Tax", command=calculate_tax)
button_calculate.pack(pady=10)

# Labels to show results
label_assessment_value = tk.Label(root, text="Assessment Value: $0.00")
label_assessment_value.pack()

label_property_tax = tk.Label(root, text="Property Tax: $0.00")
label_property_tax.pack()

# Run the app
root.mainloop()
