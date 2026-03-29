import tkinter as tk
from tkinter import messagebox, filedialog
def info():
	messagebox.showinfo("Info", "Hello!")
def open_file():
	file = filedialog.askopenfilename()
	label.config(text=f"Opened: {file}" if file else "Cancelled")
root = tk.Tk()
root.title("Dialogs Demo")
tk.Button(root, text="Message Box", command=info).pack()
tk.Button(root, text="Open File", command=open_file).pack()
label = tk.Label(root, text="")
label.pack()
root.mainloop()

