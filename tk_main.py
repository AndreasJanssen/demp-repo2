import time
import tkinter as tk
import os

path = "."  # current directory
qr_list = os.listdir(path + "/QR_Codes")  # read existing QR-Codes
print(f"QR-Liste: {qr_list}")

from tkinter import *

root = Tk()

sizex = 600
sizey = 400
posx = 0
posy = 0
root.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

labels = []


def myClick(qr_list):
    del labels[:]  # remove any previous labels from if the callback was called before
    myframe = Frame(root, width=400, height=300, bd=2, relief=GROOVE)
    myframe.place(x=10, y=10)
    # x = myvalue.get()
    # value = int(x)
    for i in range(len(qr_list)):
        labels.append(Label(myframe, text=qr_list[i]))  # + str(i)))
        labels[i].place(x=10, y=10 + (30 * i))
        Button(myframe, text="Select").place(x=270, y=10 + (30 * i))


def myClick2():
    if len(labels) > 0:
        labels[0].config(text="Click2!")
    if len(labels) > 1:
        labels[1].config(text="Click2!!")


mybutton = Button(root, text="OK", command=myClick(qr_list))
mybutton.place(x=420, y=10)

mybutton2 = Button(root, text="Change", command=myClick2)
mybutton2.place(x=420, y=80)

myvalue = Entry(root)
myvalue.place(x=450, y=10)

root.mainloop()
exit()
window = tk.Tk()
window.geometry("500x300")
greeting = tk.Label(
    text="Hello Tkinter",
    foreground="white",
    background="black")
another = tk.Label(
    text="Another Text",
    fg="yellow",
    bg="blue")
third = tk.Label(
    text="Another Text",
    fg="black",
    bg="#34A2FE",
    width=15,
    height=2)
button_1 = tk.Button(
    text="Button 1",
    width=10,
    height=3,
    bg="grey",
    fg="yellow",
    activebackground="blue",
    activeforeground="yellow")

# text_in = tk.StringVar()
entry = tk.Entry(
    window,
    fg="black",
    bg="white",
    width=30)
text_in = entry.get()
print(text_in)
text_out = tk.Label(
    text=text_in,
    fg="black",
    bg="#34A2FE",
    width=15,
    height=2)

# entry_2 = tk.Entry(window)
# entry_2.grid(row=0, column=1)

greeting.pack()
another.pack()
third.pack()
button_1.pack()
entry.pack()
text_out.pack()

window.update()
window.mainloop()
