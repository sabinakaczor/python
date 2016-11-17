# *-* coding: utf-8 *-*
'''
pliki
'''

#utworzenie i otwarcie do zapisu pliku "plik1.txt"
f1 = open("plik1.txt","wb")

# 3 podstawowe atrybuty obiektów plikowych

#name - nazwa pliku
print f1.name

# mode - określa tryb w jakim otwarto plik
print f1.mode

#closed - określa czy plik jest zamknięty
print f1.closed

#metody do obsługi pliku

#write - zapisuje do pliku napis
f1.write("Pierwszy plik")

#flush - zapisuje dane z bufora do pliku
# przydatne w przypadku systemu Windows
f1.flush()

#\n - nowa linia w pliku
f1.write("\nnowa linia")

#close - zapisuje dane z bufora do pliku i zamyka plik
f1.close()

#otwarcie pliku do modyfikacji
f1 = open("plik1.txt", "r+b")

#read - odczytuje z pliku napis
print f1.read()

#tell - podaje aktualną pozycję w pliku
print f1.tell()

#seek - ustawia pozycję w pliku na podaną
f1.seek(0)

#nadpisanie zawartości pliku
f1.write("Nowy początek")

#przesunięcie na względną pozycję pliku (od aktualnej pozycji)
f1.seek(-14,1)

#wczytanie fragmentu zawartości pliku o określonej długości
print f1.read(14)

#writelines - zapisuje do pliku sekwencję napisów
# (bez dodawania automatycznie separatorów)
f1.writelines(["\n3 linia","\n4 linia","\n5 linia"])

#readlines - wczytuje z pliku sekwencję napisów
f1.seek(0)
print f1.readlines()

#truncate - skraca plik na podanej pozycji
f1.truncate(30)
f1.seek(0)
print f1.read()

#isatty - zwraca True jeżeli plik jest dołączony do
# urządzenia terminalowego

print f1.isatty()

#przykład strumienie sys, stdout i sys.stdin
import sys
print sys.stdout.isatty()

#przykład przekierowania wewnątrz programu
import sys
ekran = sys.stdout

#przykład przekierowania wewnątrz programu
import sys
ekran = sys.stdout
sys.stdout = open("wyjscie.txt","w")
print "Jestem tutaj"
print "Gdzie Ty poszedłeś?"
sys.stdout = ekran
print open("wyjscie.txt","r").read()
