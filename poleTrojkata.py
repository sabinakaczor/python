# coding=utf-8



h = raw_input("Podaj wysokość trójkąta\n")
a = raw_input("Podaj długość podstawy trójkąta\n")
def poleTrojkata(a,h):
    pole  = 0.5 * float(a) * float(h)
    return pole

print "\nPole trójkąta wynosi " + str(poleTrojkata(a,h)) + "."
