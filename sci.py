#coding:utf-8


"""
Fonction Vue: print(), input(), type()
int(), float(), str(), bool()

"""

import tkinter
# from tkinter import*

mainapp = tkinter.Tk()
mainapp.title("Fallout Shelter")
size_x = int(mainapp.winfo_screenwidth())
size_y = int(mainapp.winfo_screenheight())
window_x = 800
window_y = 600 
geo = "{} x {} + {} + {}".format(window_x, window_y, posX, posY)
#mainapp.minsize(600, 400)
#mainapp.maxsize(1280, 720)

#mainapp.geometry("800x600")
#mainapp.resizable(width=False, height=False)
#mainapp.positionfrom("user")

#position_x = (largeur // 2) - (largeur fenetre)
#position_y = (hauteur // 3) - (hauteur fenetre)

mainapp.mainloop()
