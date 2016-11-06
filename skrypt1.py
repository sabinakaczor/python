# coding=utf-8
'''
Witam w Pythonie
Pierwszy skrypt
'''


print 'Witaj w Pythonie'

a = 5
print a

'''
a += 2
print a
'''
#print a + 2

'''print a + '2' '''

#b = 4
#print a + b

'''
b = '4'
print a + b
'''

a, b, c = 9, 8, 7
print a, b, c

#del a
#print a

calkowita = 10
print calkowita

zmiennoprzecinkowa = 10.234
print zmiennoprzecinkowa

zespolona = 3+5j
print zespolona

osemkowa = 0o15
print osemkowa

szesnastkowa = 0xabc
print szesnastkowa

dwojkowa = 0b1011
print dwojkowa

napis = 'To jest \' String'
print napis

napis2 = 'Tekst z tabulatorem\ti znakiem\n nowego wiersza'
print napis2

napis3 = '''wiersz o
wielu
wierszach'''
print napis3

print("Zielone"+" jabłko")

#print("B"+"a"+5+"rdzo pyszne!")

print("Py" "thon")

napis = "Wiek: " + str(18)

print napis
print napis.replace("W","w")
print napis.lower()
print napis.upper()
napis = "Ta liczba %f to %s" % (3.23, "liczba")
print napis

print ('(0), (1), (2)'.format('a', 'b', 'c'))    #coś nie działa!!

l = [1,2,'element',3.14]
print l

k = (1,2,'element',3.14)
print k
print l[1]
print k[1]

print l[1:3]
print k[:-2]

print l in l

l[0] = 3
print l

#k[0] = 3
#print(k)

l[1:3] = ['a', 'b']
print l

macierz = [1,[1,2,3,4]]
print macierz

print macierz[1][3]

macierz[1][3] = 5
print macierz

lista = [1,2,3]
lista2 = lista + [4,5,6]
print(lista2)

lista = [4,6,2,4,8]
lista.sort()
print lista

lista.reverse()
print lista

lista.append(6)
print lista

lista.insert(2,10)
print lista

lista.pop()
print lista

lista.remove(4)
print lista

del lista[1:3]
print lista

slownik = {'a':'b','klucz':15,3:[1,3,4]}
print slownik

print slownik['a']
print len(slownik)

print list(slownik.keys())

d={}
print 'b' in d

d['b'] = 1
print d

a = True
b = False
print a,b

x = 4
y = 8

print x < y
print x == y
print x != y

print a or b
print a and b
print not a
print not b

licznik = 10
wartosc = 15
while licznik <= wartosc:
    licznik += 1
    print "Jestem w while."

for i in range(10):
    print i

print "Pętla 2:"
for i in range(3, 5):
    print i

print "Pętla 3:"
for i in range(10, 100, 10):
    print i

bar = {"imie": "tomasz", "nazwisko": "łobuz"}
print bar["imie"]

for i in bar:
    print i + " - " + bar[i]

if bar.has_key("imie"):
    print bar["imie"]

print bar.get("imie", "Brak klucza")
