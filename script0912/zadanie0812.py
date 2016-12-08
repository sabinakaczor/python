#coding: utf-8

"""
gui
system 2, 8, 10 konwersja
radio button + checkbox
"""


from Tkinter import *
from tkMessageBox import *
root = Tk()
root.title(u"Wykszta\u0142cenie")
var = IntVar()

def toBin(number):
    number = int(number)
    bin = ""
    while (number > 0):
        bin += str(number % 2)
        number /= 2
    bin = bin[::-1]
    return bin


def toOct(number):
    number = int(number)
    oct = ""
    while (number > 0):
        oct += str(number % 8)
        number /= 8
    oct = oct[::-1]
    return oct

class Konwersja(Frame):
    "demonstruje cztery pola tekstowe"
    def __init__(self):


        "Tworzy, pakuje i binduje zdarzenia do pol tekstowych"
        Frame.__init__(self)
        self.pack(expand = YES, fill = BOTH)

        self.master.title("Konwersja na system dwójkowy i ósemkowy")
        self.master.geometry("325x100") #width and length

        self.frame1 = Frame(self)
        self.frame1.pack(pady = 5)


        for text, value in [("dwójkowy", 1), ('ósemkowy', 2)]:
            Radiobutton(root, text=text, value=value, variable=var).pack(anchor=W)

        self.text = Entry(self.frame1, name = "tekst")
        self.text.insert(INSERT, "Wpisz liczbe tutaj")
        self.text.bind("<Return>", self.showContents)
        self.text.pack(side = LEFT, padx = 5)

        '''self.text1 = Entry(self.frame1, name = "tekst 1")
        self.text1.bind("<Return>", self.showContents)
        self.text1.pack(side = LEFT, padx = 5)

        self.text2 = Entry(self.frame1, name = "tekst 2")
        self.text2.insert(INSERT, "Wpisz tekst tutaj")
        self.text2.bind("<Return>", self.showContents)
        self.text2.pack(side = LEFT, padx = 5)

        self.frame2 = Frame(self)
        self.frame2.pack(pady = 5)

        self.text3 = Entry(self.frame2, name = "tekst 3")
        self.text3.insert(INSERT, "Pole nieedytowalne")
        self.text3.config(state = DISABLED)
        self.text3.bind("<Return>", self.showContents)
        self.text3.pack(side = LEFT, padx  =5)

        #tekst in polu text4 pojawia się jako
        self.text4 = Entry(self.frame2, name = "tekst 4", show = "*")
        self.text4.insert(INSERT, "Tekst ukryty")
        self.text4.bind("<Return>", self.showContents)
        self.text4.pack(side = LEFT, padx = 5)'''

    def showContents(self, event):
        """Wyswietl zawartosc pola"""
        theName = event.widget.winfo_name()
        theContents =  event.widget.get()
        choice = var.get()
        print choice
        if choice == 1:
            showinfo("Wynik konwersji:", toBin(theContents))
        else:
            showinfo("Wynik konwersji:", toOct(theContents))





def main():
    Konwersja().mainloop()

if __name__ == "__main__":
    main()