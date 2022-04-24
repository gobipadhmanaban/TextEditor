from tkinter import *
from tkinter.filedialog import *
from tkinter.messagebox import *
import sys
import subprocess

file_path = ''
def set_file_path(path):
    global file_path
    file_path = path







class File():
    #clear output
    def clr_output(self):
        self.code_op.delete(0.0, END)
        self.code_op.insert(1.0, "OUTPUT: ")

    # run function
    def run(self):
        if file_path == '':
            save_prompt = Toplevel()
            text = Label(save_prompt, text='Please save your code')
            text.pack()
            return
        command = f'python {file_path}'
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        self.code_op.insert('9.0', output)
        self.code_op.insert('9.0', error)

    def newFile(self):
        self.filename = "Untitled"
        self.text.delete(0.0, END)



    def saveFile(self):
        if file_path != '':
            t = self.text.get(0.0, END)
            f = open(self.filename, 'w')
            f.write(t)
            f.close()
        else:
            self.saveAs()


    def saveAs(self):
        if file_path == '':
            path = asksaveasfilename(filetypes=[('Python Files', '*.py'),('Text file', '*.txt')])

        else:
            path = file_path
        self.filename = path
        with open(path, 'w') as file:
            code = self.text.get('1.0', END)
            file.write(code)
            set_file_path(path)
        t = self.text.get(0.0, END)
        try:
            file.write(t.rstrip())
        except:
            showerror(title="Oops!", message="Unable to save file...")

    def openFile(self):
        path = askopenfilename(filetypes=[('Python Files', '*.py'), ('Text file', '*.txt')])
        self.filename = path
        with open(path, 'r') as file:
            code = file.read()
            self.text.delete('1.0', END)
            self.text.insert('1.0', code)
            set_file_path(path)


    def quit(self):
        entry = askyesno(title="Quit", message="Are you sure you want to quit?")
        if entry == True:
            self.root.destroy()

    def __init__(self, text, code_op, root):
        self.filename = None
        self.text = text
        self.root = root
        self.code_op = code_op


def main(root, text, code_op, menubar):
    filemenu = Menu(menubar, tearoff=0)
    objFile = File(text, code_op, root)
    filemenu.add_command(label="New", command=objFile.newFile)
    filemenu.add_command(label="Open", command=objFile.openFile)
    filemenu.add_command(label="Save", command=objFile.saveFile)
    filemenu.add_command(label="Save As...", command=objFile.saveAs)
    # IDE FUNCTION
    filemenu.add_command(label='Run', command=objFile.run)
    filemenu.add_command(label='Clr Output', command=objFile.clr_output)
    filemenu.add_separator()
    filemenu.add_command(label="Quit", command=objFile.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    root.config(menu=menubar)


if __name__ == "__main__":
    print("Please run 'main.py'")
