from Tkinter import *
class Kalkulator (Frame):
    'dalsza instrukcja etykiet i przyciski'
    def __init__(self, ):
        'Tworzy trzy etykiety i dwa przyciski oraz pakujeje '
        # tworzy obiekt ramka w ktorym umieszczamy widgety
        # ramka jest upakowana w glownym oknie i ma tytyl - Przyklad

        Frame.__init__(self)
        self.pack(expand = YES, fill = BOTH)
        self.master.title("Kalkulator")
        self.master.geometry("200x200")

        # Tworzymy dwa przyciski o nazwach QUIT i Hej ktorych wcisniecie powoduje wywolanie metody quitl i say_hi odpowiednio
        # Nazwy obiektow to button i hi_there
        self.button = Button(self, text="QUIT", fg="red", command=self.quit1, width=16, height=1)
        self.hi_there = Button(self, text="Hej", command=self.fib, width=16, height=1)

        self.jeden = Button(self, text="1", command=self.przypisz, width=1, height=1)
        self.dwa = Button(self, text="2", command=self, width=1, height=1)
        self.trzy = Button(self, text="3", command=self, width=1, height=1)
        self.cztery = Button(self, text="4", command=self, width=1, height=1)
        self.piec = Button(self, text="5", command=self, width=1, height=1)
        self.szczesc = Button(self, text="6", command=self, width=1, height=1)
        self.siedem = Button(self, text="7", command=self, width=1, height=1)
        self.osiem = Button(self, text="8", command=self, width=1, height=1)
        self.dziewiec = Button(self, text="9", command=self, width=1, height=1)
        self.zero = Button(self, text="0", command=self, width=1, height=1)
        self.dzialanie = Label(self, text = "Etykieta tekstowa")
        self.dzialanie.pack()



        self.jeden.pack     (side=LEFT)
        self.dwa.pack       (side=LEFT)
        self.trzy.pack      (side=LEFT)
        self.cztery.pack    (side=LEFT)
        self.piec.pack      (side=LEFT)
        self.szczesc.pack   (side=LEFT)
        self.siedem.pack    (side=LEFT)
        self.osiem.pack     (side=LEFT)
        self.dziewiec.pack  (side=LEFT)
        self.zero.pack      (side=LEFT)
        self.button.pack(side=BOTTOM)
        self.hi_there.pack(side=BOTTOM)
        self.pack(fill=BOTH, expand=NO)

    def przypisz(self):
        self.Label4 = Label(self, text="1")
        self.Label4.pack()
    #metoda wywolywana przez wcisniecie przycisku Quit
    def quit1(self):
        print "Koniec"
        quit()
    #metoda wywolywana przez wcisniecie Hej
    def say_hi(self):
        print "Hej - witajcie !"

    def fib(self):
        k = [0, 1]
        for l in range(2, 10):
            il = k[l - 2] + k[l - 1]
            k.append(il)
        print k
        # self.Label4 = Label(self, text=k)
        # self.Label4.pack()


# (A) Program glowny - utworzenie okna laveldemo i obsluga wszystkich zdzarzen
def main():
    Kalkulator().mainloop()
# jesli nazwa uruchomionego programu to __main__ wywolaj procedure main()
if  __name__ == "__main__":
    main()

# coding=utf-8


