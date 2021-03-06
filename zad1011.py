# coding: utf-8

import random
from math import sqrt, floor

class Lista:

    def initList(self):
        """tworzenie nowej listy"""
        self.lista = []

    def fillList(self):
        """uzupelnienie listy losowymi wartosciami"""
        size = input("Podaj rozmiar listy\n")
        self.a = input("Podaj poczatek zakresu\n")
        self.b = input("Podaj koniec zakresu\n")
        while (self.b <= self.a):
            self.b = input("Koniec zakresu musi byc wiekszy od poczatku!\n")
        random.seed()
        for i in range(size):
            k = random.randint(self.a, self.b)
            self.lista.append(k)

    def printList(self):
        print self.lista

    def multiplies(self):
        """wyszukiwanie wielokrotnosci"""
        self.A = [x for x in self.lista if (x % 2) == 0]
        self.B = [x for x in self.lista if (x % 3) == 0]
        self.C = [x for x in self.lista if (x % 5) == 0]

    def duplicates(self):
        """wyszukiwanie duplikatów i ich zapis do nowej listy"""
        self.D = []
        self.D += [self.A[i] for i in range(0,len(self.A)) for j in range (0,len(self.A)) if (self.A[i]==self.A[j] and i != j)]
        self.D += [self.B[i] for i in range(0,len(self.B)) for j in range (0,len(self.B)) if (self.B[i]==self.B[j] and i != j)]
        self.D += [self.C[i] for i in range(0,len(self.C)) for j in range (0,len(self.C)) if (self.C[i]==self.C[j] and i != j)]
        self.D += [self.lista[i] for i in range (0,len(self.lista)) for j in range (0,len(self.lista))
                   if self.lista[i]==self.lista[j] and i != j and self.lista[i] not in self.D]
        s = set(self.D)
        self.D = list(s)
        print self.D

    def duplicatesToX(self):
        """zamiana duplikatów na X"""
        for i in range (0,len(self.D)):
            for j in range (0,len(self.lista)):
                if self.lista[j]==self.D[i] and j != self.lista.index(self.D[i]):
                    self.lista[j] = 'X'
            for j in range(0, len(self.A)):
                if self.A[j] == self.D[i] and j != self.A.index(self.D[i]):
                    self.A[j] = 'X'
            for j in range(0, len(self.B)):
                if self.B[j] == self.D[i] and j != self.B.index(self.D[i]):
                    self.B[j] = 'X'
            for j in range(0, len(self.C)):
                if self.C[j] == self.D[i] and j != self.C.index(self.D[i]):
                    self.C[j] = 'X'
        print self.lista
        print self.A
        print self.B
        print self.C

    def removeDuplicates(self):
        """usuwanie duplikatów z pierwotnej listy"""
        while ('X' in self.lista):
            self.lista.remove('X')
        print self.lista

    def average_n_cube(self):
        "liczenie średniej i podnoszenie elementów do potęgi 3"
        self.average = (1.0 * sum(self.lista)) / len(self.lista)
        print self.average
        self.lista = [x**3 for x in self.lista]
        print self.lista

    def replace_multiplies(self):
        """zastepowanie wielokrotności odpowiednimi literami"""
        self.multiplies()
        for i in range (0,len(self.lista)):
            if self.lista[i] in self.A:
                if self.lista[i] in self.B:
                    if self.lista[i] in self.C:
                        self.lista[i] = 'AEL'
                    else:
                        self.lista[i] = 'AE'
                else:
                    self.lista[i] = 'A'
            elif self.lista[i] in self.B:
                if self.lista[i] in self.C:
                    self.lista[i] = 'EL'
                else:
                    self.lista[i] = 'E'
            elif self.lista[i] in self.C:
                self.lista[i] = 'L'
        print self.lista

    def prime_numbers(self):
        """zastępowanie liczb pierwszych znakiem Z"""
        primes = sito(self.b)
        for i in range (0,len(self.lista)):
            if self.lista[i] in primes:
                self.lista[i] = 'Z'
        print self.lista

    def random_words(self):
        """układanie słów z liter o losowych długościach z przedziała [3;25]"""
        letters = []
        words = []
        for x in self.lista:
            if type(x)==str:
                if len(x)==1:
                    letters.append(x)
                else:
                    letters += list(x)
        word = ""
        random.seed()
        k = random.randint(3,25)
        while (len(letters)>0):
            i = random.randint(0,len(letters)-1)
            if len(word) == k:
                words.append(word)
                word = ""
                k = random.randint(3, 25)
            word += letters[i]
            del(letters[i])
        if (len(letters) == 0):
            words.append(word)
        print words


def sito(n):
    A = [True]
    for i in range(2, n + 1):
        A.append(True)

    for i in range(2, int(floor(sqrt(n)) + 1)):
        if (A[i] == True):
            j = i ** 2
            while (j < n):
                A[j] = False
                j += i

    B = []
    for k in range(2, len(A)):
        if A[k] == True:
            B.append(k)
    return B


l = Lista()
l.initList()
l.fillList()
l.printList()
l.multiplies()
l.duplicates()
l.duplicatesToX()
l.removeDuplicates()
#l.average_n_cube()
l.replace_multiplies()
l.prime_numbers()
l.random_words()