#coding: utf-8

class Kontakt:
    def _init_(self, imie, nazwisko, nr, adres):
        self.n = imie
        self.ln = nazwisko
        self.nr = nr
        self.ad = adres

class Osoby:
    def _init_(self, ile):
        self.ile = ile

k1 = Kontakt()
k1.ad = "Lublin"
k1.n = "Sabina"
k1.ln = "Kaczor"
k1.nr = "123456789"

k2 = Kontakt()
k2.ad = "Warszawa"
k2.n = "Anna"
k2.ln = "Nowak"
k2.nr = "111222333"

k3 = Kontakt()
k3.ad = "Puławy"
k3.n = "Jan"
k3.ln = "Kowalski"
k3.nr = "123987645"

osoby = [k1, k2, k3]

'''
print "%3s" % ("LP") + " %10s" % ("IMIĘ") + " %10s" % ("NAZWISKO") + " %12s" % ("ADRES") + " %12s" % ("TELEFON\n")

for i in range (len(osoby)):
    print "%3s" % (str(i+1)) + " %10s" % (osoby[i].n) + " %10s" % (osoby[i].ln) + " %12s" % (osoby[i].ad) + " %12s" % (osoby[i].nr)
'''

def wyswietl(osoby):
    print "LP".center(3) + "IMIĘ".center(15) + "NAZWISKO".center(15) + "ADRES".center(20) + "TELEFON".center(13) + "\n"
    for i in range (len(osoby)):
        print str(i+1).center(3) + str(osoby[i].n).center(15) + str(osoby[i].ln).center(15) + str(osoby[i].ad).center(20) + str(osoby[i].nr).center(13)
    n = input("\nCo chcesz zrobiĆ?\n1 - dodaje nowy kontakt\n2 - usuwa kontakt\n3 - modyfikuje kontakt\n")

    while (n != 1 and n != 2 and n != 3):
        n = input("Niepoprawny format wyboru\n")
    return n




while (True):
    
    n = wyswietl(osoby)
    if (n==1):
        imie = raw_input("Podaj imię: ")
        nazw = raw_input("Podaj nazwisko: ")
        adr = raw_input("Podaj adres: ")
        tel = raw_input("Podaj numer telefonu: ")

        os = Kontakt()
        os.n = imie
        os.ln = nazw
        os.ad = adr
        os.nr = tel
        osoby.append(os)

    elif (n==2):
        k = input("Podaj numer kontaktu, który chcesz usunąć\n")
        while (k < 1 or k > len(osoby)):
            k = input("Złe dane, spróbuj ponownie!\n")
        dec = raw_input("Zostaną usunięte dane dla " + osoby[k-1].n + " " + osoby[k-1].ln + ", czy potwierdzasz? (T/N)\n")
        while (dec != "T" and dec != "N"):
            dec = raw_input("Wpisz T lub N\n")
        if (dec=="T"):
            osoby.remove(osoby[k-1])
        
    else:
        k = input("Podaj numer kontaktu, który chcesz zmodyfikować\n")
        while (k < 1 or k > len(osoby)):
            k = input("Złe dane, spróbuj ponownie!\n")
            
        imie = raw_input("Imię: " + osoby[k-1].n + "\nZachowaj [S] / Modyfikuj [M]\n")
        while (imie != "S" and imie != "M"):
            imie = raw_input("Wpisz S lub M\n")
        if (imie == "M"):
            imie = raw_input("Nowe imię: ")
            osoby[k-1].n = imie
        nazw = raw_input("Nazwisko: " + osoby[k-1].ln + "\nZachowaj [S] / Modyfikuj [M]\n")
        while (nazw != "S" and nazw != "M"):
            nazw = raw_input("Wpisz S lub M\n")
        if (nazw == "M"):
            nazw = raw_input("Nowe nazwisko: ")
            osoby[k-1].ln = nazw
        adr = raw_input("Adres: " + osoby[k-1].ad + "\nZachowaj [S] / Modyfikuj [M]\n")
        while (adr != "S" and adr != "M"):
            adr = raw_input("Wpisz S lub M\n")
        if (adr == "M"):
            adr = raw_input("Nowy adres: ")            
            osoby[k-1].ad = adr
        tel = raw_input("Numer telefonu: " + osoby[k-1].nr + "\nZachowaj [S] / Modyfikuj [M]\n")
        while (tel != "S" and tel != "M"):
            tel = raw_input("Wpisz S lub M\n")
        if (tel == "M"):
            tel = raw_input("Nowy numer telefonu: ")            
            osoby[k-1].nr = tel

        #~ os = Kontakt()
        #~ os.n = imie
        #~ os.ln = nazw
        #~ os.ad = adr
        #~ os.nr = tel
        
        #~ osoby[k-1] = os
        
        #~ temp = []
        #~ i = len(osoby)-1
        #~ while (osoby[i] != osoby[k-1]):
            #~ temp.append(osoby.pop())
            #~ i = len(osoby)-1
        #~ osoby.pop()
        #~ osoby.append(os)
        #~ while (len(temp) > 0):
            #~ osoby.append(temp.pop())