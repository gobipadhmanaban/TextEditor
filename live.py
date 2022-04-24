import webbrowser
from tkinter import *


class Live():
    def go_live(root):
        webbrowser.open('https://studio.youtube.com/video/QYwpE_clZtQ/livestreaming')



def main(root, text, menubar):

    live = Live()

    liveMenu = Menu(menubar, tearoff=0)
    liveMenu.add_command(label="Go Live", command=live.go_live)
    menubar.add_cascade(label="Live", menu=liveMenu)

    root.config(menu=menubar)

if __name__ == "__main__":
    print("Please run 'main.py'")
