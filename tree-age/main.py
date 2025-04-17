#
# Name Wolfgang Meyer
# Date 4-17-25
# Tree Age Programming Project
# SDEV 1200
#

# Use comments liberally throughout the program. 

import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Tree Growth Rings")

# Set up canvas
canvas_width = 400
canvas_height = 400
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Center of the canvas
center_x = canvas_width // 2
center_y = canvas_height // 2

# Number of years / rings
years = 5
ring_spacing = 20  # Distance between rings

# Draw rings and label them
for i in range(years):
    radius = (i + 1) * ring_spacing
    # Draw oval (ring)
    canvas.create_oval(
        center_x - radius, center_y - radius,
        center_x + radius, center_y + radius,
        outline="brown"
    )
    # Label the ring with year number
    canvas.create_text(
        center_x + radius - 10, center_y,
        text=f"Year {i+1}",
        fill="green",
        font=("Arial", 10, "bold")
    )

# Start the GUI loop
root.mainloop()
