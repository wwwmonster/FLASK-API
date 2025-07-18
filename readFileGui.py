import tkinter as tk
from tkinter import BOTTOM, filedialog
from tkinter import ttk
from tkinter import messagebox
import os


class FileSelectorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Selector with Checkboxes")

        window_width = 800
        window_height = 600
        self.center_window(window_width, window_height)
        self.root.attributes("-topmost", True)

        # Main horizontal layout: left (table), right (button)
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Left: Scrollable file table
        self.table_frame = ttk.Frame(self.main_frame)
        self.table_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas = tk.Canvas(self.table_frame)
        self.scrollbar = ttk.Scrollbar(
            self.table_frame, orient="vertical", command=self.canvas.yview
        )
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")),
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Right: Select button
        self.right_panel = ttk.Frame(self.main_frame, width=100)
        self.right_panel.pack(side=tk.RIGHT, fill=tk.Y, padx=(10, 0))

        self.select_button = ttk.Button(
            self.right_panel, text="Select Files", command=self.select_files, width=10
        )
        self.select_button.pack(pady=10, anchor="n")

        self.excute_button = ttk.Button(
            self.right_panel, text="Excute", command=self.execute_action, width=10
        )
        self.excute_button.pack(pady=10, anchor="n")

        self.exit_button = ttk.Button(
            self.right_panel, text="Exit", command=self.root.destroy, width=10
        )
        self.exit_button.pack(pady=10, side=tk.BOTTOM, anchor="n")

        # Store checkbutton variables
        self.check_vars = []

    def center_window(self, width, height):
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def select_files(self):
        self.file_vars = []
        file_paths = filedialog.askopenfilenames(title="Select Files")
        self.clear_table()
        self.check_vars = []
        self.root.attributes("-topmost", False)

        for index, path in enumerate(file_paths):
            filename = os.path.basename(path)
            var = tk.BooleanVar()
            self.check_vars.append(var)
            self.file_vars.append((filename, var))
            checkbox = ttk.Checkbutton(self.scrollable_frame, variable=var)
            checkbox.grid(row=index, column=0, sticky="w", padx=5, pady=2)

            label = ttk.Label(self.scrollable_frame, text=filename, anchor="w")
            label.grid(row=index, column=1, sticky="w", padx=5, pady=2)

    def clear_table(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

    def execute_action(self):
        if not hasattr(self, "file_vars") or not self.file_vars:
            messagebox.showinfo("No files", "No files selected.")
            return

        selected_files = [fname for fname, var in self.file_vars if var.get()]
        if selected_files:
            messagebox.showinfo("Selected Files", "\n".join(selected_files))
        else:
            messagebox.showinfo("Selected Files", "No files are checked.")


# Run the app
root = tk.Tk()
app = FileSelectorApp(root)
root.mainloop()
