
from tkinter import *
import threading
import cv2
import numpy as np
from win32api import GetSystemMetrics
import datetime
from PIL import ImageGrab

class record():
    def rec_video(root):
            width = GetSystemMetrics(0)
            height = GetSystemMetrics(1)
            time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
            file_name = f'{time_stamp}.mp4'
            fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
            captured_video = cv2.VideoWriter(file_name, fourcc, 30.0, (width, height))


            while True:
                img = ImageGrab.grab(bbox=(0, 0, width, height))
                img_np = np.array(img)
                img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
                cv2.imshow('screen Capture', img_final)

                captured_video.write(img_final)
                cv2.imshow('Screen Captur', img_final)

                captured_video.write(img_final)
                if cv2.waitKey(10) == ord('q'):
                    break


def main(root, text, menubar):

    rec = record()

    recMenu = Menu(menubar, tearoff=0)
    recMenu.add_command(label="Record screen", command=threading.Thread(target=rec.rec_video).start)
    menubar.add_cascade(label="Record", menu=recMenu)

    root.config(menu=menubar)
