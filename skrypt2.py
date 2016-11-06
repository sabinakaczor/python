# coding=utf-8

'''
a, b, c = 9, 8, 7
print a, b, c

a=5; b=8
print a, b

a=4
b='6'
c = `a` + b
print c

a,b=2,3

print a+b
print a-b
print a*b
print a/b
print a%b
print a**b  #potega
print "\n"

#długie liczby rzeczywiste
print 4*7L
print "\n"

#Liczby rzeczywiste
print 2.5
print 2e+4
print 4.0/3.0
print 4.0//3.0
print 3.5e+4+1000000L*2
print "\n"

#Liczby zespolone
print -2+3j
print 3j**2
print 3.2+400L/(2+3j)
print "\n"

a,b,c,d,e=1,3,7,4,6
a+=2
b-=2
c*=2
d/=2
print a,b,c,d,e
print "\n"

imie = raw_input("Jak masz na imię?\n")
print "Masz na imię " + imie

a=6
b=5

#Instrukcje warunkowe i pętle
if a<4:
    print a
elif a>4:
    print b


for x in range (-10,11):
    print "%+i" % x, #+ -znak przed liczbą


print "\n"
'''
for x in range (5,100,10):
    print "%3i%6o%5x" % (x,x,x) #wyrównanie od prawej

'''
for x in range (5,100,10):
    print "%-3i%#-6o%#-5x" % (x,x,x) #wyrównanie od lewej (# - właściwy prefix)

for x in range (5,100,10):
    print "%3i %04o %#04x" % (x,x,x) #0 - pole przeznaczone na liczby będzie wypełnione 0

a=[1,2,3,4,5,6]
while a:
    a=a[:len(a)-1]
    print a


def pierw(n):
    return n**0.5

print pierw(3)

def pierw2(n):
    if n>=0: return n**0.5

print pierw2(4)

def pierw3(n):
    if n>0: return n**0.5
    else: return (-n)**0.5*1j

print pierw3(-6)

def rs(a,b):
    return a-b, a+b

print rs(8,4)

def suma(*arg):
    s=0
    for x in arg:
        s+=x
    return s

print suma(*range(10))


h = raw_input("Podaj wysokość trójkąta\n")
a = raw_input("Podaj długość podstawy trójkąta\n")
def poleTrojkata(a,h):
    pole  = 0.5 * float(a) * float(h)
    return pole

print "\nPole trójkąta wynosi " + str(poleTrojkata(a,h))
'''
