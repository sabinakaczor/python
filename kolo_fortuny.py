# *-* coding: utf-8 *-*

import random

class Game:
    def __init__(self):
        self.name = "Koło fortuny"
        self.guessed = []
        self.done = False

    def get_players_number(self):
        self.players_no = input("Ile osób gra?\n")
        self.list_av = range(1, self.players_no + 1)
        return self.players_no

    def get_category(self):
        file_categories = open("kategorie.txt","r")
        categories =  file_categories.readlines()
        random.seed()
        i = random.randint(1,len(categories)-1)
        self.category = categories[i]

    def get_passwd(self):
        file_passwds = open("hasla.txt","r")
        passwds = file_passwds.readlines()
        for i in range(0,len(passwds)):
            if self.category[:-1] in passwds[i]:
                random.seed()
                j = random.randint(i+1, i+6)
                self.passwd = passwds[j][:-1]


    def start_writing(self):
        with open("scores.txt","w") as fw:
            fw.write("Uczestnik Wynik")

    def show_passwd(self):
        copy = list(self.passwd)
        for i in range (0,len(copy)):
            if copy[i] not in self.guessed:
                copy[i] = "*"
        copy1 = ""
        for i in range(0, len(copy)):
            copy1 += str(copy[i])
        return copy1

class Player:
    def __init__(self,g):
        self.score = 0

    def get_name(self,i):
            self.name = raw_input("Imię " + str(i) + ". uczestnika: ")

    def get_pos(self):
        random.seed()
        self.pos = random.choice(g.list_av)
        g.list_av.remove(self.pos)
        return self.pos

    def twist(self):
        random.seed()
        self.rand_no = random.randint(-10,10)
        print "\n" + self.name + ":\nWylosowałeś " + str(self.rand_no)
        if self.rand_no != 0:
            self.get_letter()
        else:
            self.score = 0

    def get_letter(self):
        letter = raw_input("Podaj literkę ")
        while (len(letter) != 1):
            letter = raw_input("Podaj pojedynczą literkę ")
        if letter in g.passwd:
            g.guessed.append(letter)
            print "\nHasło: " + g.show_passwd()
            k = 0
            for i in range (0,len(g.passwd)):
                if g.passwd[i] == letter:
                    k += 1
            if self.rand_no > 0:
                self.score += self.rand_no
            self.guess_passwd(k)
        else:
            print "\nHasło nie zawiera tej literki!"
            self.score += self.rand_no

    def guess_passwd(self,k):
        guess = raw_input("Jakie hasło obstawiasz?\n")
        if guess==g.passwd:
            self.score *= len(g.passwd) - k
            print "\nBrawo!"
            g.done = True
        else:
            print "\nNiestety, nie zgadłeś!"

    def write_score(self):
        with open("scores.txt", "a") as fw:
            fw.write("\n" + "%9s" % self.name + " %5s" % str(self.score))

def code_passwd(passwd,letter):
    for x in passwd:
        if x != letter:
            x = '*'


def byPos_key(player):
    return player.pos

g = Game()

print g.name + "\n"
n = g.get_players_number()
g.get_category()
g.get_passwd()
g.start_writing()




players = []
for i in range (0,g.players_no):
    players.append(Player(g))

for i in range (0,len(players)):
    players[i].get_name(i+1)
    players[i].get_pos()

print "\nKolejność grania:"
players = sorted(players, key= byPos_key)
for player in players:
    print str(player.pos) + " " + player.name

print "\nKategoria: " + g.category + "Hasło: " + g.show_passwd()

while(g.done == False):
    for i in range (0,len(players)):
        players[i].twist()
        if (g.done):
            break

for i in range (0,len(players)):
    players[i].write_score()

print "Wyniki zapisano do pliku scores.txt."
