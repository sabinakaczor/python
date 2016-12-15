#coding: utf-8
"""Przykład widgetu Menu"""

from Tkinter import *
root = Tk()
root.title("Menu dla zbiorow")

menubar = Menu(root)
filemenu = Menu(menubar,tearoff=0)
filemenu.add_command(label="Nowy", command=None)
filemenu.add_command(label="Otworz", command=None)
filemenu.add_command(label="Nagraj", command=None)
filemenu.add_command(label="Nagraj jako...", command=None)
filemenu.add_command(label="Zamknij", command=None)

filemenu.add_separator()

filemenu.add_command(label=u"Wyj\u015bcie", command=root.quit)
filemenu.add_cascade(label="Zbior", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Cofnij", command=None)

editmenu.add_separator()

editmenu.add_command(label="Wytnij", command=None)
editmenu.add_command(label="Kopiuj", command=None)
editmenu.add_command(label="Wklej", command=None)
editmenu.add_command(label=u"Usu\u0144", command=None)
editmenu.add_command(label="Wybierz wszystko", command=None)

menubar.add_cascade(label="Edycja", menu=editmenu)
helpmenu = Menu(menubar, tearoff = 0)
helpmenu.add_command(label = "Indeks Pomocy", command=None)
helpmenu.add_command(label = "0...", command=None)
menubar.add_cascade(label="Pomoc", menu = helpmenu)

root.config(menu=menubar)
root.mainloop()