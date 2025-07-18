import tkinter as tk

# tk.TkVersion = 8.6  # Ensure compatibility with the latest version of Tkinter


class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple GUI")
        self.root.geometry("300x200")

        self.label = tk.Label(root, text="Hello, Tkinter!")
        self.label.pack(pady=20)

        self.button = tk.Button(root, text="Click Me", command=self.on_button_click)
        self.button.pack(pady=10)

    def on_button_click(self):
        self.label.config(text="Button Clicked!")


if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
#     app.run(debug=True, host="
