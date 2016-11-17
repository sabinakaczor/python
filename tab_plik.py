# *-* coding=utf-8 *-*


f1 = open("plik2.txt","wb")

for i in range (1,11):
    for j in range (1,11):
        f1.write( "%6i" % (i*j))
    f1.write("\n\n")