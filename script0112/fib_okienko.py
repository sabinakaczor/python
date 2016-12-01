#coding: utf-8

from Tkinter import *

class App(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Ciąg Fibonacciego")

        self.button = Button(self, text="Wyświetl", fg="blue",
                                 command = self.fib, width = 16, height = 1)
        self.button.pack(side=TOP)

    def fib(self):
        k = [0, 1]
        for l in range(2, 10):
            il = k[l - 2] + k[l - 1]
            k.append(il)
        self.label = Label(self, text=str(k))
        self.label.pack(side=BOTTOM)

def main():
    App().mainloop()

if __name__ == "__main__":
    main()