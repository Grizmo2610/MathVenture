import os
import tkinter as tk
from tkinter import messagebox, simpledialog

MAPS_DIR = "maps"
GRID_WIDTH = 16
GRID_HEIGHT = 20

# Ensure the map storage folder exists
os.makedirs(MAPS_DIR, exist_ok=True)

class MapManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Map Manager")

        self.map_data = []
        self.current_map = None

        # Top control frame
        control_frame = tk.Frame(root)
        control_frame.pack(pady=10)

        self.map_name_entry = tk.Entry(control_frame, width=20)
        self.map_name_entry.pack(side=tk.LEFT, padx=5)

        tk.Button(control_frame, text="Create Map", command=self.create_map).pack(side=tk.LEFT)
        tk.Button(control_frame, text="Delete Map", command=self.delete_map).pack(side=tk.LEFT)

        # Operator buttons
        operator_frame = tk.Frame(root)
        operator_frame.pack(pady=5)

        for op in ["W", "+", "-", "*", "/", "^", "@"]:
            tk.Button(operator_frame, text=op, width=5,
                      command=lambda o=op: self.insert_operator(o)).pack(side=tk.LEFT, padx=2)

        # Canvas for grid
        self.grid_frame = tk.Frame(root)
        self.grid_frame.pack(pady=10)

        self.cell_buttons = []

    def create_map(self):
        name = self.map_name_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Error", "Enter a map name.")
            return

        if not name.endswith(".txt"):
            name += ".txt"

        self.current_map = os.path.join(MAPS_DIR, name)

        if os.path.exists(self.current_map):
            overwrite = messagebox.askyesno("Map Exists", f"{name} exists. Overwrite?")
            if not overwrite:
                return

        # Ask for target value
        try:
            target = simpledialog.askinteger("Target", "Enter target value:")
            if target is None:
                return
        except ValueError:
            messagebox.showerror("Invalid Input", "Target must be an integer.")
            return

        # Initialize map data with empty cells
        self.map_data = [["" for _ in range(GRID_WIDTH)] for _ in range(GRID_HEIGHT)]
        self.map_data.insert(0, target)  # First line is the target
        self.save_map()
        self.render_grid()

    def delete_map(self):
        name = self.map_name_entry.get().strip()
        if not name:
            messagebox.showwarning("Input Error", "Enter a map name.")
            return

        if not name.endswith(".txt"):
            name += ".txt"

        path = os.path.join(MAPS_DIR, name)

        if os.path.exists(path):
            os.remove(path)
            messagebox.showinfo("Deleted", f"Deleted {name}")
        else:
            messagebox.showwarning("Not Found", f"{name} not found.")

    def save_map(self):
        if self.current_map:
            with open(self.current_map, "w") as f:
                f.write(str(self.map_data[0]) + "\n")  # Write target
                for row in self.map_data[1:]:
                    f.write(", ".join(cell if cell else " " for cell in row) + ",\n")

    def render_grid(self):
        for widget in self.grid_frame.winfo_children():
            widget.destroy()

        self.cell_buttons = []
        for r in range(GRID_HEIGHT):
            row_buttons = []
            for c in range(GRID_WIDTH):
                text = self.map_data[r + 1][c] if self.map_data[r + 1][c] else " "
                btn = tk.Button(self.grid_frame, text=text, width=4, height=2,
                                command=lambda x=r, y=c: self.select_cell(x, y))
                btn.grid(row=r, column=c)
                row_buttons.append(btn)
            self.cell_buttons.append(row_buttons)

        self.selected_cell = None

    def select_cell(self, row, col):
        self.selected_cell = (row, col)

    def insert_operator(self, operator):
        if operator == "@":
            return
        
        if not self.selected_cell:
            messagebox.showinfo("Select Cell", "Click a cell first.")
            return
        
        if operator != "W" and operator != "@":
            number = simpledialog.askinteger("Number", "Enter a number:")

        if number is None:
            return

        if operator != "W" and operator != "@":
            logic = messagebox.askyesno("Logic", "Is logic True?")

        if operator == "@":
            value = f"{operator}{number}"
        elif operator == "W":
            value = "W"
        else:
            value = f"{operator}{number}{operator}{logic}"

        r, c = self.selected_cell
        self.map_data[r + 1][c] = value
        self.save_map()
        self.render_grid()

# Run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = MapManager(root)
    root.mainloop()
    # root.destroy()