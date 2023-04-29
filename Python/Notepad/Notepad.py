from tkinter import *
import os
from tkinter import filedialog
from pathlib import Path

filename = "*.txt"

root = Tk()
root.title(f"Jihun NOTEPAD - {filename}")
root.geometry("640x480")

def open_file():
    global filename
    filename = filedialog.askopenfilename(title = "Select Text File",
                                          filetypes=(("Text File","*.txt"), ("All Files", "*.*")),
                                          initialdir="C:\\Users\\visio\\OneDrive\\Desktop\\Python\\Notepad\\Text")
    if os.path.isfile(filename):
        with open(filename, "r", encoding="utf-8") as file:
            txt.delete("1.0",END)
            txt.insert(END, file.read())
        filename = Path(filename).stem
        root.title(f"JIHUN NOTEPAD - {filename}")

def browse_dest_path():
    filesave = filedialog.asksaveasfilename(title = "Save",
                                          defaultextension='.txt',
                                          filetypes=(("Text File","*.txt"), ("All Files", "*.*")),
                                          initialdir="C:\\Users\\visio\\OneDrive\\Desktop\\Python\\Notepad\\Text")
    if filesave == "":
        return
    return filesave

def save_file():
    global filename
    file_path = browse_dest_path()
    filename = Path(file_path).stem
    with open(file_path, "w", encoding="uft-8") as f:
        f .write(txt.get("1.0", END))
        root.title(f"JIHUN NOTEPAD - {filename}")

menu = Menu(root)

menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label="Open", command=open_file)
menu_file.add_command(label="Save", command=save_file)
menu_file.add_separator()
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)




#scroll bar
scrollbar = Scrollbar(root)
scrollbar.pack(side="right", fill="y")

# Text pad
txt = Text(root, yscrollcommand=scrollbar.set)
txt.pack(fill="both", expand=True)
scrollbar.config(command=txt.yview)


root.config(menu=menu)
root.mainloop()