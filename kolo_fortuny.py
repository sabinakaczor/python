# *-* coding: utf-8 *-*

import random



class Game:
    def __init__(self):
        self.name = "Koło fortuny"

    def get_users_number(self):
        self.users = input("Ile osób gra?\n")
        return self.users

    def get_names(self):
        names = []
        for i in range (0,self.users):
            names[i] = raw_input("Imię " + str(i-1) + ". uczestnika: ")

    def available_pos(self):
        self.list_av = range(1,self.users+1)

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

class User:
    def __init__(self,name):
        self.score = 0
        self.name = name


    def get_pos(self):
        random.seed()
        self.pos = random.randint(1,Game.users)
        Game.list_av.remove(self.pos)
        return self.pos

    def twist(self):
        random.seed()
        self.rand_no = random.randint(-10,10)
        print "Wylosowałeś " + self.rand_no +"\n"
        if self.rand_no != 0:
            self.get_letter()
        else:
            self.score = 0

    def get_letter(self):
        letter = raw_input("Podaj literkę ")
        while (len(letter) != 1):
            letter = raw_input("Podaj pojedynczą literkę ")
        if letter in self.passwd:
            k = 0
            for i in range (0,len(self.passwd)):
                if self.passwd[i] == letter:
                    k += 1
            # cos zrobić z k
            if self.rand_no > 0:
                self.score += self.rand_no
        self.guess_passwd()

    def guess_passwd(self):
        guess = raw_input("Jakie hasło obstawiasz?\n")
        if guess==self.passwd:
            self.score *= len(self.passwd) - 1

    def get_score(self):
        if self.rand_no > 0 or self.rand_no < 0:
            self.score += self.rand_no
            self.get_letter()
        elif self.rand_no == 0:
            self.score = 0



g = Game()
n = g.get_users_number()
g.get_names()
g.available_pos()
g.get_category()
g.get_passwd()

users = []
for i in range(0,n):
    users[i] = User()

for j in range (0,n):
    users[i].
