#coding:utf-8

import tkinter

def update_label(*args):
	var_label.set(var_entry.get())


app = tkinter.Tk()
app.geometry("1920x1080")
app.title("Variable")

var_entry = tkinter.StringVar()
var_entry.trace("w", update_label)
entry = tkinter.Entry(app, textvariable=var_entry)

check = tkinter.Checkbutton()

var_label = tkinter.StringVar()
label = tkinter.Label(app, width=200, textvariable=var_label)


var_label.set("Aime tu les films de diglateur et les monsieurs tout nue ?")
var_label.set("Es-tu gay ? ")
var_label.set("Whouah t'en une énorme !!")
check = tkinter.Checkbutton()

check = tkinter.Checkbutton()


#entry.pack()
label.pack()
check.pack()
app.mainloop()
