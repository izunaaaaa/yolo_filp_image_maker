from re import X
import cv2
import matplotlib.pyplot as plt
from os import path
import numpy as np
import os
import sys
import shutil
import string
import tkinter

def reverse_jpg():
 file_path = "C:/Users/IITP/Desktop/vscode/Filp_image"
 file_list=os.listdir(file_path)
 file_list_jpg=[file for file in file_list if file.endswith(".jpg")]
 temp = ""
 length = len(file_list_jpg)
 n = 1
 for i in file_list_jpg:
    temp = i
    src = cv2.imread("image/"+i) 
    dst = cv2.flip(src, 1)
    cv2.imwrite("filp_image/f_" + i, dst)
    print(n , round(n/length*100,1) , "%")
    n+=1

def reverse_txt():
 file_path = "C:/Users/IITP/Desktop/vscode/Filp_image"
 file_list=os.listdir(file_path)
 file_list_txt=[file for file in file_list if file.endswith(".txt")]
 temp = ""
 k = 0
 length = len(file_list_txt)
 for j in file_list_txt:
  filp_txt = open("filp_image/f_" + j, "w")
  with open("image/" + j, "r") as f:
    example = f.readlines()
    for line in example:
        x = line[2:10]
        reverse_x = 1-float(x)
        reverse_x = format(reverse_x, '.6f')
        line = line[0:1] +" "+ reverse_x + line[10:]
        filp_txt = open("filp_image/f_" + j, "a")
        filp_txt.write(line)
    filp_txt.close()
    k+=1
    print (k,len(file_list_txt))

window=tkinter.Tk()
window.title("reverse")
window.geometry("400x300+100+100")
window.resizable(False, False)
label = tkinter.Label(window, text="0")
label.pack()
button = tkinter.Button(window, overrelief="solid", width=15, command=reverse_jpg, repeatdelay=1000, repeatinterval=100, text="사진 반전")
button.pack()
window.mainloop()

