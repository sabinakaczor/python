'''
moduly - generator liczb pseudolosowych
'''

import random
#from random import *           #nazwy funkcji dostepne bez uzycia nazwy modulu
#from random import randint     #funkcja dostepna bez uzycia nazwy modulu

random.seed()
print random.randint(1,15) #losuje liczby calkowite z zakresu od 1 do 15
print random.randint(1,15)

l = range(1,10)
print random.choice(l)  #wybiera losowy element z sekwencji

random.shuffle(l) #wykopnuje losowe permutacje sekwencji
print l

print random.random()   #losowa liczba rzeczywista z zakresu 0.0 do 1.0

print random.uniform(10,30)   #losowa liczba rzeczywista z przedzialu [10,30)

print random.normalvariate(5,48) #zmienna losowa o rozkladzie normalnym o sredniej 5
                                    #i odchyleniu 48



'''
rekordy
'''

class Adres:
    pass


adr1 = Adres() #utowrzenie rekordu
adr1.ulica = 'Stonogi'
adr1.nr = 23
adr1.kod = '64-345'
adr1.miasto = 'Dno'

print adr1.ulica
print adr1.__dict__


