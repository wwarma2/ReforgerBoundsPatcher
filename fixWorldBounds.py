import tkinter as tk
from tkinter import filedialog, messagebox
import re

def convert_km_to_meters(map_size, y_min, y_max):
"""Convert the entered map size from km to meters and return formatted boundMins and boundMaxs."""
try:
width, depth = map_size.lower().split("x")
width_m = float(width.strip()) * 1000
depth_m = float(depth.strip()) * 1000

bound_mins = f"boundMins 0 {y_min} 0"
bound_maxs = f"boundMaxs {width_m} {y_max} {depth_m}"

return bound_mins, bound_maxs
except ValueError:
messagebox.showerror("Invalid Input", "Please enter a valid map size in the format: 10x10")
return None, None

def select_file():
"""Open file dialog to select a file."""
file_path = filedialog.askopenfilename(title="Select a file to update")
file_entry.delete(0, tk.END)
file_entry.insert(0, file_path)

def update_file():
"""Find and update the existing `GenericWorldEntity world {` block in the file."""
file_path = file_entry.get()
map_size = map_size_entry.get()
y_min = y_min_entry.get()
y_max = y_max_entry.get()

if not file_path:
messagebox.showwarning("No File Selected", "Please select a file to update.")
return

if not y_min or not y_max:
messagebox.showwarning("Missing Height Values", "Please enter valid Y Min and Y Max values.")
return

try:
y_min = float(y_min)
y_max = float(y_max)
except ValueError:
messagebox.showerror("Invalid Input", "Y Min and Y Max must be numbers.")
return

bound_mins, bound_maxs = convert_km_to_meters(map_size, y_min, y_max)
if not bound_mins or not bound_maxs:
return

try:
with open(file_path, "r") as file:
lines = file.readlines()

inside_world_block = False
updated_lines = []

for line in lines:
if "GenericWorldEntity world {" in line:
inside_world_block = True
updated_lines.append(line.strip())  # Keep opening line

elif inside_world_block:
continue  # Skip old values

# Insert new values after `GenericWorldEntity world {`
updated_lines.append(f" {bound_mins}")
updated_lines.append(f" {bound_maxs}")

updated_lines.append(line.strip())  # Keep the rest of the block

if "}" in line:  # End of block
inside_world_block = False

else:
updated_lines.append(line.strip())

# Reconstruct file content
updated_content = "\n".join(updated_lines)

# Save back to the file
with open(file_path, "w") as file:
file.write(updated_content)

messagebox.showinfo("Success", f"Updated {file_path} successfully.")

except Exception as e:
messagebox.showerror("Error", f"Could not update file: {e}")

# --- GUI Setup ---
root = tk.Tk()
root.title("World Bounds Editor")
root.geometry("800x800")
root.resizable(False, False)

# Header Label
tk.Label(root, text="World Bounds Editor", font=("Arial", 24, "bold")).pack(pady=20)

# Map Size Input (with "km" label)
frame_map_size = tk.Frame(root)
frame_map_size.pack(pady=20)

tk.Label(frame_map_size, text="Enter Map Size (e.g., 10x10):", font=("Arial", 14)).pack(side=tk.LEFT, padx=10)
map_size_entry = tk.Entry(frame_map_size, font=("Arial", 14), width=15)
map_size_entry.pack(side=tk.LEFT)
tk.Label(frame_map_size, text="km", font=("Arial", 14)).pack(side=tk.LEFT)

# Y Min & Y Max Input
frame_y_values = tk.Frame(root)
frame_y_values.pack(pady=20)

tk.Label(frame_y_values, text="Enter Y Min:", font=("Arial", 14)).pack(side=tk.LEFT, padx=10)
y_min_entry = tk.Entry(frame_y_values, font=("Arial", 14), width=10)
y_min_entry.pack(side=tk.LEFT, padx=10)

tk.Label(frame_y_values, text="Enter Y Max:", font=("Arial", 14)).pack(side=tk.LEFT, padx=10)
y_max_entry = tk.Entry(frame_y_values, font=("Arial", 14), width=10)
y_max_entry.pack(side=tk.LEFT)

# File Selection
frame_file = tk.Frame(root)
frame_file.pack(pady=20)

tk.Label(frame_file, text="Select File to Update:", font=("Arial", 14)).pack(side=tk.LEFT, padx=10)
file_entry = tk.Entry(frame_file, font=("Arial", 14), width=30)
file_entry.pack(side=tk.LEFT, padx=10)
file_button = tk.Button(frame_file, text="Browse", font=("Arial", 12), command=select_file)
file_button.pack(side=tk.LEFT)

# Save Button
save_button = tk.Button(root, text="Save", font=("Arial", 16, "bold"), command=update_file, bg="green", fg="white", width=15, height=2)
save_button.pack(pady=30)

# Run the GUI
root.mainloop()