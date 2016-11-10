# coding: utf-8
#utworzyć klasę - podpunkty mają być jej uniwersalnymi metodami
# c - bez metody

import random

class Lista:
    def __init__(self,A):
        self.A = A

    def uzupelnijListe(self):
        A=[]
        size = input("Podaj rozmiar listy\n")
        a = input("Podaj poczatek zakresu\n")
        b = input("Podaj koniec zakresu\n")
        while (b <= a):
            b = input("Koniec zakresu musi byc wiekszy od poczatku!\n")

        random.seed()
        for i in range(size):
            k = random.randint(a, b)
            A.append(k)
        return A

    def wielokrotnosci(self, A):
        B = [x for x in A if not (x % 2)]
        C = [x for x in A if not (x % 3)]
        C = [x for x in A if not (x % 5)]

    def duplikaty(self,L):
        B = []
        for i in range(0,len(L)):
            for j in range (0,len(L)):
                if L[i]==L[j] and i!=j:
                    B.append(L[i])



def nwd(l1, l2):
    a = min(l1, l2)
    b = max(l1, l2) % a
    while a != 0 and b != 0:
        temp = min(a, b)
        temp2 = max(a, b) % temp
        a = temp
        b = temp2
    if a == 0:
        return b
    else:
        return a

def nww(a, b):
    return a * b / nwd(a, b)\





A=[]
l = Lista(A)
#A =  l.uzupelnijListe()
#B = wielokrotnosci([1,2,10,6])
#print B