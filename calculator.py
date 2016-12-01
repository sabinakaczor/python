# coding: utf-8

from Tkinter import *


class Calculator(Frame):

    def __init__(self):
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Kalkulator")

        # przyciski
        self.button1 = Button(self, text="1", fg="black", width=2, height=2)
        self.button2 = Button(self, text="2", fg="black", width=2, height=2)
        self.button3 = Button(self, text="3", fg="black", width=2, height=2)
        self.button4 = Button(self, text="4", fg="black", width=2, height=2)
        self.button5 = Button(self, text="5", fg="black", width=2, height=2)
        self.button6 = Button(self, text="6", fg="black", width=2, height=2)
        self.button7 = Button(self, text="7", fg="black", width=2, height=2)
        self.button8 = Button(self, text="8", fg="black", width=2, height=2)
        self.button9 = Button(self, text="9", fg="black", width=2, height=2)
        self.button0 = Button(self, text="0", fg="black", width=2, height=2)
        self.buttonplus = Button(self, text="+", fg="black", width=2, height=2)
        self.buttonminus = Button(self, text="-", fg="black", width=2, height=2)
        self.buttonmultiply = Button(self, text="*", fg="black", width=2, height=2)
        self.buttondivide = Button(self, text="/", fg="black", width=2, height=2)
        self.buttonequal = Button(self, text="=", fg="black", width=2, height=2)

        # wyswietlacz
        self.label = Label(self, text="")

        self.label.pack()
        self.button1.pack()
        self.button2.pack()
        self.button3.pack()
        self.button4.pack()
        self.button5.pack()
        self.button6.pack()
        self.button7.pack()
        self.button8.pack()
        self.button9.pack()
        self.button0.pack()
        self.buttonplus.pack()
        self.buttonminus.pack()
        self.buttonmultiply.pack()
        self.buttondivide.pack()




def main():
    Calculator().mainloop()

if __name__ == "__main__":
    main()
