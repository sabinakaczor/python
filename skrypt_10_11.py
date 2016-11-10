 # -*- coding: utf-8 -*-
'''
wytworniki (list comprehensions)
'''

l=range(1,21,2)
print l

#postać prosta

#podwojenie wartości
print [2*x for x in l]

#para (x, kwadrat x)
print [(x, x*x) for x in range (1,5)]

#tabela kodowa ASCII
print [(x, ord(x)) for x in "ABCDEF"]

#lista zawierająca 10 pustych list
print [ [] for x in range(10)]

#postać prosta warunkowa

#liczby (większe od 10)
print [x for x in l if x>10]

#liczby podzielne przez 3 lub 5
print [x for x in range(1,20) if not (x%3) or not (x%5)]

#tabela kodowa ASCII dla samogłosek
print [(x, ord(x)) for x in "ABCDEF" if x in "AEIOUY"]

#postać rozszerzona

#pary każdy element z każdym
print [(x,y) for x in range (1,5)
       for y in range (4,0,-1)]

#różnica między wartością z pierwszej i drugiej listy
print [x-y for x in range (1,5)
       for y in range (4,0,-1)]

#sklejanie napisu z wartości pochodzących z 3 list
print [`x` + y + `z` for x in [1,2]
       for y in ['A','B']
       for z in [0,3]]

#postac rozszerzona z jednym warunkiem

#para każdy element z każdym tylko jeżeli pierwszy
# element jest mniejszy od drugiego
print [(x,y) for x in range (1,5)
       for y in range (6,3,-1)
       if x<y]

#para każdy element z każdym tylko jeżeli
# suma elementów jest mniejsza od 7
print [(x,y) for x in range (1,5)
       for y in range (6,3,-1)
       if x+y<7]

#para każdy element z każdym pod warunkiem że
# pierwszy element jest parzysty lub drugi jest
# nieparzysty
print [(x,y) for x in range (1,5)
       for y in range (6,2,-1)
       if not (x%2) or (y%2)]

#postać rozszerzona z wieloma warunkami

#para każdy element z każdym pod warunkiem że pierwszy
# element jest parzysty a drugi nieparzysty
print [(x,y) for x in range (1,5) if not (x%2)
       for y in range (6,2,-1) if y%2]

'''
funkcje ułatwiające przetwarzanie sekwencji
'''

#funkcja apply  -  wywołannie funkcji z parametrami
# uzyskanymi z rozpakowania sekwencji
dziel = lambda x,y,z: (x+y)/z
print dziel(7,4,6)

xyz = (7,4,6)
print apply(dziel,xyz)

#funkcja map - wywołuje określoną funkcję dla każdego
# elementu sekwencji z osobna
print map(lambda x: x*x*x, range(10))
print map(dziel, range(10), range(10), [2]*10)

#funkcja zip - służy do konsolidacji danych
#wartość pojedynczego elementu listy wynikowej
# zależy od wartości pojedynczych
# elementów list źródłowych

print zip("abcdef",[1,2,3,4,5,6])
print zip(range(1,10),range(9,0,-1))
print zip("zip", range(0,9), zip(range(0,9)))

#funkcja filter - służy do filtrowania danych

#filtrowanie samogłosek
samogloska = lambda x: x.lower() in 'aeiou'
print samogloska('A')
print filter(samogloska,"ala ma kota")

#filtrowanie innych znaków2
print filter(lambda x: not samogloska(x), "Ala ma kota")

#funkcja reduce - agregowanie danych operacja obliczania
# pojedynczego wyrażenia zależnego od wszystkich elementów
# listy źródłowej

#suma elementów
print reduce(lambda x,y: x+y, [1,2,3])

#suma kwadratów elementów
print reduce(lambda x,y: x+y, map(lambda x: x*x, range(1,3)))