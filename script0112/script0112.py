#coding: utf-8

"""Przykład PY62. Najprostsza etykieta Label."""

from Tkinter import *

'''
root = Tk()
w = Label(root, text="Witajcie!")
w.pack()
root.mainloop()
'''

"""Przykład PY63. Etykiety i przyciski"""

class LabelDemo(Frame):
    def __init__(self):
        """Tworzy trzy etykiety i dwa przyciski oraz pakuje je"""
        #tworzy obiekt ramka w którym umieszczono widgety
        #ramka jest upakowana w glownym oknie i ma tytul - Przyklad
        Frame.__init__(self)
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Przykład")

        #Tworzymy dwa przyciski o nazwach QUIT i Hej których wcisniecie
        #powoduje wywolanie metod quit1 i say_hi odpowiednio
        #nazwy obiektow to button i hi_there
        self.button = Button(self, text="QUIT", fg="red",
                             command = self.quit1, width = 16, height = 1)

        self.hi_there = Button(self, text= "Hej", command = self.say_hi,
                               width = 16, height = 1)

        #tworzymy trzy pola etykiet - dwa tekstowe i ikone
        self.Label1 = Label(self, text = "Etykieta tekstowa")
        self.Label2 = Label(self, text = "Etykieta tekstowa z ikona")
        self.Label3 = Label(self, bitmap = "warning")

        #teraz pakujemy wsztstko w ramce
        self.button.pack(side=BOTTOM)
        self.hi_there.pack(side=BOTTOM)
        self.Label1.pack()
        self.Label2.pack(side=LEFT)
        self.Label3.pack(side=LEFT)

    #metoda wywolana przezz wcisniecie QUIT
    def quit1(self):
        print "Koniec"
        quit()

    #metoda wywolana przez wcisniecioe Hej
    def say_hi(self):
        print "Hej - witajcie!"

 # (A) Program glowny - utworzenie okna LabelDemo i obsluga wszytskich zdarzen
def main():
    LabelDemo().mainloop()

#jesli nazwa uruchomionego programu to __main__ wywolaj procedure main()
if __name__ == "__main__":
    main()

