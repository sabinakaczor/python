 # -*- coding: utf-8 -*-
'''
wttworniki (list comprehensions)
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

#para każdy element z każdym tyl;ko jeżeli pierwszy
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

