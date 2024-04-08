from tkinter import *
from tkinter import filedialog
import tkinter as tk
from PIL import Image,ImageTk
import os

def showimage():
    filename=filedialog.askopenfilename(initialdir=os.getcwd(), title="Select image file", filetype=(("JPG File", "*.jpg"), ("PNG File", "*.png"), ("All File","How Are You .txt" )))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img)
    lbl.image=img
    
    
root = Tk()

frame=Frame(root)
frame.pack(side=BOTTOM, padx=15, pady=15)

lbl=Label(root)
lbl.pack()

btn1=Button(frame,text="Select Iamge", command=showimage)
btn1.pack()

btn2=Button(frame,text="Exit", command=lambda:exit())
btn2.pack(side=tk.LEFT, padx=12)

root.title("Image Viewer App")
root.geometry("400x450")
root.mainloop()
