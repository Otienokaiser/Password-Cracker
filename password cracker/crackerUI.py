import tkinter as tk
from tkinter import messagebox

def crack_password():
    actual_password = entry_password.get()
    result = guess_password(actual_password)
    messagebox.showinfo("Password Cracker", result)

# Create the UI
root = tk.Tk()
root.title("Password Cracker")

label_username = tk.Label(root, text="Username:")
entry_username = tk.Entry(root)
label_password = tk.Label(root, text="Password:")
entry_password = tk.Entry(root, show="*")
button_crack = tk.Button(root, text="Crack Password", command=crack_password)

label_username.pack()
entry_username.pack()
label_password.pack()
entry_password.pack()
button_crack.pack()

root.mainloop()
