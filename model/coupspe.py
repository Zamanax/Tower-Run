import tkinter as tk
from threading import Thread
from model.fonctions_utiles import load
from model.Character import Character


class Kamehameha(Thread):
    gauche = [0, 0, 100, 100]
    milieu = [100, 0, 200, 100]
    droite = [200, 0, 300, 100]
    head = None
    img = "view/src/personnage/heros/Goku/kamehameha_1.png"
    v = 30
    longueurMax = 15
    trainee = []
    isHeadingRight = False
    def __init__(self, hero):
        Thread.__init__(self)
        self.start()
        self.longueur = 0
        self.hero = hero
        self.y = hero.y-5
        self.parent = hero.parent
        self.target = hero.target
        self.damage = hero.damage
        self.canvas = hero.canvas

        self.d = load(self.droite, self.img)
        self.g = load(self.gauche, self.img)
        self.m = load(self.milieu, self.img)

        if self.hero.state == "specialMoveRight":
            self.x = hero.x+100
            self.tete = self.d
            self.isHeadingRight = True

        elif self.hero.state == "specialMoveLeft":
            self.x = hero.x-100
            self.tete = self.g

        self.tir()

    def tir(self):
        ennemies = self.parent.ennemies
        self.longueur += 1

        if self.longueur != self.longueurMax:

            if self.head:
                self.canvas.delete(self.head)
            self.trainee.append(self.canvas.create_image(
                self.x, self.y, image=self.m))

            for ennemy in ennemies:
                if self.x-35 <= ennemy.x <= self.x+35 and self.y-40 <= ennemy.y <= self.y+40 and ennemy.state != "die":
                    ennemy.hp -= self.damage
                    if ennemy.hp <= 0:
                        ennemy.die(False)

            if self.isHeadingRight:
                self.x += self.v
            else:
                self.x -= self.v


            self.head = self.canvas.create_image(self.x, self.y, image=self.tete)

            self.canvas.after(150, self.tir)

        else:
            if self.isHeadingRight:
                self.hero.state = "idleRight"
            else:
                self.hero.state = "idleLeft"
            self.hero.incrementSprite()
            for elt in self.trainee:
                self.canvas.delete(elt)


class Kamehameha2(Kamehameha):
    gauche = [0, 0, 100, 100]
    milieu = [100, 0, 200, 100]
    droite = [200, 0, 300, 100]
    head = None
    img = "view/src/personnage/heros/Goku/kamehameha_2.png"
    v = 30
    longueurMax = 25

    def __init__(self, hero):
        Thread.__init__(self)
        self.start()
        self.longueur = 0

        self.hero = hero
        self.y = hero.y-16
        self.parent = hero.parent
        self.target = hero.target
        self.damage = hero.damage
        self.canvas = hero.canvas

        self.d = load(self.droite, self.img)
        self.g = load(self.gauche, self.img)
        self.m = load(self.milieu, self.img)

        if self.hero.state == "specialMoveRight":
            self.x = hero.x+100
            self.tete = self.d

        elif self.hero.state == "specialMoveLeft":
            self.x = hero.x-100
            self.tete = self.g

        self.tir()


class Kamehameha3(Thread):
    milieu = [0, 0, 150, 150]
    gauche1 = [0, 150, 150, 300]
    gauche2 = [150, 150, 300, 300]
    droite1 = [150, 0, 300, 150]
    droite2 = [300, 0, 450, 150]

    head = None
    img = "view/src/personnage/heros/Goku/kamehagra.png"
    v = 30
    longueurMax = 30

    def __init__(self, hero):
        Thread.__init__(self)
        self.start()
        self.longueur = 0

        self.hero = hero
        self.y = hero.y-23
        self.parent = hero.parent
        self.target = hero.target
        self.damage = hero.damage
        self.canvas = hero.canvas

        self.d1 = load(self.droite1, self.img)
        self.d2 = load(self.droite2, self.img)
        self.g1 = load(self.gauche1, self.img)
        self.g2 = load(self.gauche2, self.img)
        self.m = load(self.milieu, self.img)

        if self.hero.state == "specialMoveRight":
            self.x = hero.x+100
            self.tete1 = self.d1
            self.tete2 = self.d2

        elif self.hero.state == "specialMoveLeft":
            self.x = hero.x-132
            self.tete1 = self.g1
            self.tete2 = self.g2

        self.pointe = self.tete1

        self.tir()

    def tir(self):
        ennemies = self.parent.ennemies
        self.longueur += 1
        trainee = []

        if type(self.head) != None and self.longueur != self.longueurMax:
            self.canvas.delete(self.head)
            trainee.append(self.canvas.create_image(
                self.x, self.y, image=self.m))

        for ennemy in ennemies:
            if ennemy.x-35 <= self.x <= ennemy.x+35 and ennemy.y-40 <= self.y <= ennemy.y+40 and ennemy.state != "die":
                ennemy.hp -= self.damage
                if ennemy.hp <= 0:
                    ennemy.die(False)
        if self.hero.state == "specialMoveLeft":
            self.x -= self.v
        elif self.hero.state == "specialMoveRight":
            self.x += self.v

        if self.pointe == self.tete1:
            self.pointe = self.tete2
        elif self.pointe == self.tete2:
            self.pointe = self.tete1

        self.head = self.canvas.create_image(self.x, self.y, image=self.pointe)
        if not self.longueur == self.longueurMax:
            self.canvas.after(150, self.tir)
        else:
            if self.hero.state == "specialMoveLeft":
                self.hero.state = "idleLeft"
            else:
                self.hero.state = "idleRight"
            self.hero.incrementSprite()
            for elt in trainee:
                self.canvas.delete(elt)


class Genkidamasupreme(Thread):
    boule1 = [0, 0, 200, 200]
    boule2 = [200, 0, 400, 200]
    head = None
    img = "view/src/personnage/heros/Goku/genkidamasupreme.png"
    v = 3
    longueurMax = 20

    def __init__(self, hero):
        Thread.__init__(self)
        self.start()
        self.longueur = 0
        self.hero = hero
        self.y = hero.y-5
        self.parent = hero.parent
        self.target = hero.target
        self.damage = hero.damage
        self.canvas = hero.canvas

        self.c1 = load(self.boule1, self.img)
        self.c2 = load(self.boule2, self.img)
        self.corps = self.c1

        if self.hero.state == "specialMoveRight":
            self.x = hero.x+50

        elif self.hero.state == "specialMoveLeft":
            self.x = hero.x-50
            self.v = -self.v

        self.tir()

    def tir(self):
        ennemies = self.parent.ennemies
        self.longueur += 1

        if type(self.head) != None and self.longueur != self.longueurMax:
            self.canvas.delete(self.head)

        for ennemy in ennemies:
            if ennemy.x-35 <= self.x <= ennemy.x+35 and ennemy.y-40 <= self.y <= ennemy.y+40 and ennemy.state != "die":
                ennemy.hp -= self.damage
                if ennemy.hp <= 0:
                    ennemy.die(False)

            self.x += self.v

        if self.corps == self.c1:
            self.corps = self.c2
        elif self.corps == self.c2:
            self.corps = self.c1

        self.head = self.canvas.create_image(self.x, self.y, image=self.corps)
        if not self.longueur == self.longueurMax:
            self.canvas.after(150, self.tir)
        else:
            if self.hero.state == "specialMoveRight":
                self.hero.state = "idleRight"
            else: 
                self.hero.state = "idleLeft"
            self.hero.incrementSprite()


class GetsugaTenshou(Genkidamasupreme):
    gauche1 = [0, 0, 200, 200]
    gauche2 = [200, 0, 400, 200]
    droite1 = [400, 0, 600, 200]
    droite2 = [600, 0, 800, 200]
    head = None
    img = "view/src/personnage/heros/Ichigo/getsugatensho.png"
    v = 5
    longueurMax = 20

    def __init__(self, hero):
        Thread.__init__(self)
        self.start()
        self.longueur = 0
        self.hero = hero
        self.y = hero.y-5
        self.parent = hero.parent
        self.target = hero.target
        self.damage = hero.damage
        self.canvas = hero.canvas

        self.g1 = load(self.gauche1, self.img)
        self.g2 = load(self.gauche2, self.img)
        self.d1 = load(self.droite1, self.img)
        self.d2 = load(self.droite2, self.img)

        if self.hero.state == "specialMoveRight":
            self.x = hero.x+50
            self.c1 = self.d1
            self.c2 = self.d2

        elif self.hero.state == "specialMoveLeft":
            self.x = hero.x-50
            self.v = -self.v
            self.c1 = self.g1
            self.c2 = self.g2

        self.corps = self.c1

        self.tir()


class GetsugaTenshou2(GetsugaTenshou):
    gauche1 = [0, 0, 200, 200]
    gauche2 = [200, 0, 400, 200]
    droite1 = [400, 0, 600, 200]
    droite2 = [600, 0, 800, 200]
    head = None
    img = "view/src/personnage/heros/Ichigo/getsugatensho2.png"
    v = 7
    longueurMax = 25


class GetsugaTenshou3(GetsugaTenshou2):
    gauche1 = [0, 0, 200, 200]
    gauche2 = [200, 0, 400, 200]
    droite1 = [400, 0, 600, 200]
    droite2 = [600, 0, 800, 200]
    head = None
    img = "view/src/personnage/heros/Ichigo/getsugatensho3.png"
    v = 8
    longueurMax = 30


class Mugetsu(Thread):
    mugetsu = [0, 0, 200, 200]
    corps = None
    img = "view/src/personnage/heros/Ichigo/mugetsu.png"
    v = 120
    longueurMax = 15
    trainee = []

    def __init__(self, hero):
        Thread.__init__(self)
        self.start()
        self.longueur = 0
        self.y = hero.y-5
        self.hero = hero
        self.y = hero.y-16
        self.parent = hero.parent
        self.target = hero.target
        self.damage = hero.damage
        self.canvas = hero.canvas

        self.m = load(self.mugetsu, self.img)

        if self.hero.state == "specialMoveRight":
            self.x = hero.x+50
        elif self.hero.state == "specialMoveLeft":
            self.x = hero.x-50
            self.v = -self.v

        self.tir()

    def tir(self):
        ennemies = self.parent.ennemies
        self.longueur += 1

        for ennemy in ennemies:
            if ennemy.x-35 <= self.x <= ennemy.x+35 and ennemy.y-60 <= self.y <= ennemy.y+60 and ennemy.state != "die":
                ennemy.hp -= self.damage
                if ennemy.hp <= 0:
                    ennemy.die(False)

        self.x += self.v

        self.corps = self.canvas.create_image(self.x, self.y, image=self.m)
        self.trainee.append(self.corps)

        if self.longueur == self.longueurMax:
            self.hero.state = "idleRight"
            self.hero.sprite = 0
            if self.hero.incrementing == None:
                self.hero.incrementSprite()
            for elt in self.trainee:
                self.canvas.delete(elt)
            del self
        elif self.longueur == self.longueurMax-1:
            self.canvas.after(350, self.tir)
            if self.hero.state== "specialMoveRight"
                self.hero.state="idleRight"
            else:
                self.hero.state="idleLeft"
        else:
            self.canvas.after(200, self.tir)
