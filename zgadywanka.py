#coding utf-8

import random


proby = 1

a = input("Podaj poczatek zakresu\n")
while (a < 0):
    a = input("Wybierz liczbe nieujemna\n")

b = input("Podaj koniec zakresu\n")
while (b <= a):
    b = input("Koniec zakresu musi byc wiekszy od poczatku!\n")

random.seed()
k = random.randint(a, b)
#print k

l = input("Zgadnij liczbe\n")
while (l != k and proby <= 4):
    if (l<k):
        l = input("Podana liczba jest za mala, sprobuj ponownie\n")
    else:
        l = input("Podana liczba jest za duza, sprobuj ponownie\n")
    proby += 1

if (l==k):
    print "Brawo!"
else:
    print "Niestety nie zgadles :< Przekroczono liczbe dostepnych prob"