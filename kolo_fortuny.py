# *-* coding: utf-8 *-*

import random

class Game:
    def __init__(self):
        self.name = "Koło fortuny"

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
        random.seed()
        i = random.randint(1,len(passwds)-1)
        self.passwd = passwds[i]

    def start_writing(self):
        with open("scores.txt","w") as fw:
            fw.write("Uczestnik Wynik")

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
            k = 0
            for i in range (0,len(g.passwd)):
                if g.passwd[i] == letter:
                    k += 1
            if self.rand_no > 0:
                self.score += self.rand_no
            self.guess_passwd(k)
        else:
            print "\nHasło nie zawiera tej literki!"

    def guess_passwd(self,k):
        guess = raw_input("Jakie hasło obstawiasz?\n")
        if guess==g.passwd:
            self.score *= len(g.passwd) - k
            print "Brawo!"
        else:
            print "Niestety, nie zgadłeś!"

    def write_score(self):
        with open("scores.txt", "a") as fw:
            fw.write("\n" + self.name + " " + self.score)

def byPos_key(player):
    return player.pos

g = Game()

n = g.get_players_number()
g.get_category()
g.get_passwd()
g.start_writing()

print "Hasło: " + g.passwd
#h = ['*' for x ]


players = []
for i in range (0,g.players_no):
    players.append(Player(g))

for i in range (0,len(players)):
    players[i].get_name(i+1)
    players[i].get_pos()

players = sorted(players, key= byPos_key)
for player in players:
    print str(player.pos) + " " + player.name

for i in range (0,len(players)):
    players[i].twist()

for i in range (9,len(players)):
    players[i].write_score()

#print players

