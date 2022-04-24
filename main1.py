from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter.font import Font
from tkinter.scrolledtext import *
import file_menu
import rec


import subprocess

import live

root = Tk()

root.title("Text Editor WITH IDE")
root.geometry("300x250+300+300")
root.minsize(width=400, height=400)

file_path = ''


def set_file_path(path):
    global file_path
    file_path = path





menubar = Menu(root)



#text Frame Creation
editor = Text(root)
editor.pack(expand=True, fill=BOTH)
code_op = Text(height=5, width=500)
code_op.pack(expand=True, fill=Y)


code_op.insert(1.0, "OUTPUT: ")
#Call all function
file_menu.main(root, editor, code_op, menubar)

live.main(root, editor, menubar)
rec.main(root, editor, menubar)





root.mainloop()
