import tkinter as tk
import asyncio
from functools import lru_cache
from threading import Thread
from model.fonctions_utiles import load
from model.Character import Character
# from subprocess import call
import os
from subprocess import call


class Kamehameha(Thread):
    gauche = [0, 0, 100, 100]
    milieu = [100, 0, 200, 100]
    droite = [200, 0, 300, 100]
    head = None
    img = "view/src/personnage/heros/Goku/kamehameha_1.png"
    v = 30
    longueurMax = 30

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

        elif self.hero.state == "specialMoveLeft":
            self.x = hero.x-100
            self.tete = self.g

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
            if ennemy.x-35 <= self.x <= ennemy.x+35 and ennemy.y-40 <= self.y <= ennemy.y+40:
                ennemy.hp -= self.damage
                if ennemy.hp <= 0:
                    ennemy.die(False)
        if self.hero.state == "specialMoveLeft":
            self.x -= self.v
        elif self.hero.state == "specialMoveRight":
            self.x += self.v

        self.head = self.canvas.create_image(self.x, self.y, image=self.tete)
        if not self.longueur == self.longueurMax:
            self.canvas.after(150, self.tir)
        else:
            for elt in trainee:
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
        self.y = hero.y-20
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
            self.x = hero.x-100
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
            if ennemy.x-35 <= self.x <= ennemy.x+35 and ennemy.y-40 <= self.y <= ennemy.y+40:
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
            for elt in trainee:
                self.canvas.delete(elt)


class Genkidamasupreme(Thread):
    boule1 = [0, 0, 200, 200]
    boule2 = [200, 0, 400, 200]
    head = None
    img = "view/src/personnage/heros/Goku/genkidamasupreme.png"
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
            if ennemy.x-35 <= self.x <= ennemy.x+35 and ennemy.y-40 <= self.y <= ennemy.y+40:
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
    mugetsu=[0,0,200,200]
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

        self.m=load(self.mugetsu, self.img)


        if self.hero.state == "specialMoveRight":
            self.x = hero.x+50
        elif self.hero.state == "specialMoveLeft":
            self.x = hero.x-50
            self.v=-self.v
        
        self.tir()

    def tir(self):
        ennemies = self.parent.ennemies
        self.longueur += 1

        for ennemy in ennemies:
            if ennemy.x-35 <= self.x <= ennemy.x+35 and ennemy.y-60 <= self.y <= ennemy.y+60:
                ennemy.hp -= self.damage
                if ennemy.hp <= 0:
                    ennemy.die(False)

        self.x += self.v

        self.corps = self.canvas.create_image(self.x, self.y, image=self.m)
        self.trainee.append(self.corps)

        if self.longueur == self.longueurMax:
            for elt in self.trainee:
                self.canvas.delete(elt)  
            del self
        elif self.longueur==self.longueurMax-1:
            self.canvas.after(350, self.tir)  
        else :
            self.canvas.after(200, self.tir)           

class Heros(Character):
    # Variables propres au héros
    team = "ally"
    lv0 = {}
    compteur = 0

    def __init__(self, parent, x, y, max_y, min_y):

        self.hp = self.lv0["hp"]
        self.damage = self.lv0["damage"]
        self.damagingSprite = self.lv0["damagingSprite"]
        self.speed = self.lv0["speed"]
        self.attackSpeed = self.lv0["attackSpeed"]
        self.num_sprintes = self.lv0["num_sprintes"]
        self.spritesheet = self.lv0["spritesheet"]
        self.spriteSize = self.lv0["spriteSize"]
        self.y_Anim = self.lv0["y_Anim"]
        self.zoom = self.lv0["zoom"]
        self.coupSpe = self.lv0["coupSpe"]
        if "barOffsetx" in self.lv0:
            self.barOffsetx = self.lv0["barOffsetx"]
        if "barOffsety" in self.lv0:
            self.barOffsety = self.lv0["barOffsety"]
        Character.__init__(self, parent, x, y)

        # On définit l'ordonnée minimale et maximale où on peut aller
        self.max_y = max_y
        self.min_y = min_y

        # on cherche les ennemis
        self.seek()

    # Même fonction que pour les personnages
    @lru_cache(128)
    def getSprite(self):
        super().getSprite()
        # Si le heros a un niveau supérieur alors on charge des animations suplémentaires
        if self.lv1 != {}:
            self.transformAnim = [self.subimage(self.lv0["spriteSize"]*i, self.lv0["y_Anim"]["transform"], self.lv0["spriteSize"]*(i+1), self.lv0["y_Anim"]["transform"]+self.lv0["spriteSize"]).zoom(self.zoom)
                                  for i in range(self.lv0["num_sprintes"]["transform"])]
            self.transformAnim.reverse()
            self.specialMoveLeft = [self.subimage(self.lv0["spriteSize"]*i, self.lv0["y_Anim"]["specialMoveLeft"], self.lv0["spriteSize"]*(i+1), self.lv0["y_Anim"]["specialMoveLeft"]+self.lv0["spriteSize"]).zoom(self.zoom)
                                    for i in range(self.lv0["num_sprintes"]["specialMoveLeft"])]

            self.specialMoveRight = [self.subimage(self.lv0["spriteSize"]*i, self.lv0["y_Anim"]["specialMoveRight"], self.lv0["spriteSize"]*(i+1), self.lv0["y_Anim"]["specialMoveRight"]+self.lv0["spriteSize"]).zoom(self.zoom)
                                     for i in range(self.lv0["num_sprintes"]["specialMoveRight"])]
            self.specialMoveLeft.reverse()

            self.getLvlSprite(self.lv1)

        if self.lv2 != {}:
            self.getLvlSprite(self.lv2)

        if self.lv3 != {}:
            self.getLvlSprite(self.lv3)

    # Fonction chargée de charger des animations en fonctions des niveaux
    def getLvlSprite(self, dict):
        loop = asyncio.get_event_loop()
        image = tk.PhotoImage(file=dict["spritesheet"])
        if dict != self.lv3:
            tasks = self.getIdleRightAnim1(dict, image), self.getIdleLeftAnim1(dict, image), self.getRunRightAnim1(dict, image), self.getRunLeftAnim1(dict, image), self.getAttackRightAnim1(dict, image), self.getAttackLeftAnim1(
                dict, image), self.getSpecialMoveRight(dict, image), self.getSpecialMoveLeft(dict, image), self.getDeathAnim1(dict, image), self.getTransformAnim1(dict, image), self.getinstantMoveAnim1(dict, image)
        else:
            tasks = self.getIdleRightAnim1(dict, image), self.getIdleLeftAnim1(dict, image), self.getRunRightAnim1(dict, image), self.getRunLeftAnim1(dict, image), self.getAttackRightAnim1(
                dict, image), self.getAttackLeftAnim1(dict, image), self.getSpecialMoveRight(dict, image), self.getSpecialMoveLeft(dict, image), self.getDeathAnim1(dict, image), self.getinstantMoveAnim1(dict, image)

        if dict == self.lv1:
            self.idleRight1, self.idleLeft1, self.runRight1, self.runLeft1, self.attackRight1, self.attackLeft1, self.specialMoveRight1, self.specialMoveLeft1, self.death1, self.transformAnim1, self.instantMoveAnim1 = loop.run_until_complete(
                asyncio.gather(*tasks))
        elif dict == self.lv2:
            self.idleRight2, self.idleLeft2, self.runRight2, self.runLeft2, self.attackRight2, self.attackLeft2, self.specialMoveRight2, self.specialMoveLeft2, self.death2, self.transformAnim2, self.instantMoveAnim2 = loop.run_until_complete(
                asyncio.gather(*tasks))
        elif dict == self.lv3:
            self.idleRight3, self.idleLeft3, self.runRight3, self.runLeft3, self.attackRight3, self.attackLeft3, self.specialMoveRight3, self.specialMoveLeft3, self.death3, self.instantMoveAnim3 = loop.run_until_complete(
                asyncio.gather(*tasks))

# ------------------------Fonction chargée de découper les images dans les images--------

    async def getSpecialMoveLeft(self, dict, image):
        specialMoveLeft = [self.subimage1(image, dict["spriteSize"]*i, dict["y_Anim"]["specialMoveLeft"], dict["spriteSize"]*(i+1), dict["y_Anim"]["specialMoveLeft"]+dict["spriteSize"]).zoom(self.zoom)
                           for i in range(dict["num_sprintes"]["specialMoveLeft"])]
        specialMoveLeft.reverse()

        return specialMoveLeft

    async def getSpecialMoveRight(self, dict, image):
        specialMoveRight = [self.subimage1(image, dict["spriteSize"]*i, dict["y_Anim"]["specialMoveRight"], dict["spriteSize"]*(i+1), dict["y_Anim"]["specialMoveRight"]+dict["spriteSize"]).zoom(self.zoom)
                            for i in range(dict["num_sprintes"]["specialMoveRight"])]

        return specialMoveRight

    async def getIdleRightAnim1(self, dict, image):
        idleRight1 = [self.subimage1(image, dict["spriteSize"]*i, dict["y_Anim"]["idleRight"], dict["spriteSize"]*(i+1), dict["y_Anim"]["idleRight"]+dict["spriteSize"]).zoom(self.zoom)
                      for i in range(dict["num_sprintes"]["idleRight"])]
        return idleRight1

    async def getIdleLeftAnim1(self, dict, image):
        idleLeft1 = [self.subimage1(image, dict["spriteSize"]*i, dict["y_Anim"]["idleLeft"], dict["spriteSize"]*(i+1), dict["y_Anim"]["idleLeft"]+dict["spriteSize"]).zoom(self.zoom)
                     for i in range(dict["num_sprintes"]["idleLeft"])]
        idleLeft1.reverse()

        return idleLeft1

    async def getRunRightAnim1(self, dict, image):

        runRight1 = [self.subimage1(image, dict["spriteSize"]*i, dict["y_Anim"]["runRight"], dict["spriteSize"]*(i+1), dict["y_Anim"]["runRight"]+dict["spriteSize"]).zoom(self.zoom)
                     for i in range(dict["num_sprintes"]["runRight"])]
        return runRight1

    async def getRunLeftAnim1(self, dict, image):

        runLeft1 = [self.subimage1(image, dict["spriteSize"]*i, dict["y_Anim"]["runLeft"], dict["spriteSize"]*(i+1), dict["y_Anim"]["runLeft"]+dict["spriteSize"]).zoom(self.zoom)
                    for i in range(dict["num_sprintes"]["runLeft"])]
        runLeft1.reverse()

        return runLeft1

    async def getAttackRightAnim1(self, dict, image):

        attackRight1 = [self.subimage1(image, dict["spriteSize"]*i, dict["y_Anim"]["attackRight"], dict["spriteSize"]*(i+1), dict["y_Anim"]["attackRight"]+self.lv1["spriteSize"]).zoom(self.zoom)
                        for i in range(dict["num_sprintes"]["attackRight"])]

        return attackRight1

    async def getAttackLeftAnim1(self, dict, image):

        attackLeft1 = [self.subimage1(image, dict["spriteSize"]*i, dict["y_Anim"]["attackLeft"], dict["spriteSize"]*(i+1), dict["y_Anim"]["attackLeft"]+self.lv1["spriteSize"]).zoom(self.zoom)
                       for i in range(dict["num_sprintes"]["attackLeft"])]
        attackLeft1.reverse()

        return attackLeft1

    async def getDeathAnim1(self, dict, image):

        death1 = [self.subimage1(image, dict["spriteSize"]*i, dict["y_Anim"]["die"], dict["spriteSize"]*(i+1), self.lv1["y_Anim"]["die"]+dict["spriteSize"]).zoom(self.zoom)
                  for i in range(dict["num_sprintes"]["die"])]

        return death1

    async def getTransformAnim1(self, dict, image):
        transform1 = [self.subimage1(image, dict["spriteSize"]*i, dict["y_Anim"]["transform"], dict["spriteSize"]*(i+1), self.lv1["y_Anim"]["transform"]+dict["spriteSize"]).zoom(self.zoom)
                      for i in range(dict["num_sprintes"]["transform"])]
        transform1.reverse()

        return transform1

    async def getinstantMoveAnim1(self, dict, image):
        instantMove = [self.subimage1(image, dict["spriteSize"]*i, dict["y_Anim"]["instantMove"], dict["spriteSize"]*(i+1), self.lv1["y_Anim"]["instantMove"]+dict["spriteSize"]).zoom(self.zoom)
                       for i in range(dict["num_sprintes"]["instantMove"])]

        return instantMove

    def subimage1(self, image, x1, y1, x2, y2):
        # Création de la variable à retourner
        self.compteur += 1
        sprite = tk.PhotoImage()
        # print(self.compteur)
        self.parent.parent.currentFrame.progressBar["value"] = self.compteur
        self.parent.update()
        # Décupage de l'image en Tcl
        sprite.tk.call(sprite, 'copy', image,
                       '-from', x1, y1, x2, y2, '-to', 0, 0)
        return sprite

# ----------------------------------------------------------------------------------------

    # Fonction de recherche des ennemis
    def seek(self):
        # Si on a déjà une cible on attaque
        if self.target:
            self.attack()
        else:
            if self.state == "idleRight" or self.state == "idleLeft":
                # Sinon on cherche une cible potentielle dans les ennemis du niveau
                for ennemy in self.parent.ennemies:
                    # On calcule la distance et l'état
                    if (((ennemy.x-self.x)**2)+((ennemy.y-self.y)**2))**0.5 < self.range and ennemy.state != "die":
                        # Il devient la cible
                        self.target = ennemy

                        # On annule tout
                        if self.seeking:
                            self.canvas.after_cancel(self.seeking)
                        if self.move:
                            self.canvas.after_cancel(self.move)

                        # On attaque
                        self.sprite = 0
                        self.attack()
                        return self.target

            self.seeking = self.canvas.after(150, self.seek)

    # Fonction chargée du déplacement à la souris du héros
    def mouseMove(self, event):

        # Si il se transforme on ne fait rien
        if self.state == "transform":
            return

        # Si on bouge déjà alors on annule l'ancien mouvement
        if self.move:
            if self.state == "runRight":
                self.state = "idleRight"
            elif self.state == "runLeft":
                self.state = "idleLeft"
            self.canvas.after_cancel(self.move)
            self.move = None

        # Si on attaque alors on annule
        if self.attacking:
            if self.state == "attackRight":
                self.state = "idleRight"
            elif self.state == "attackLeft":
                self.state = "idleLeft"
            self.canvas.after_cancel(self.attack)
            self.attacking = None

        # On effectue le mouvement en restant dans les bornes
        self.sprite = 0
        if event.y > self.max_y:
            self.moveTo(event.x, self.max_y)
        elif event.y < self.min_y:
            self.moveTo(event.x, self.min_y)
        else:
            self.moveTo(event.x, event.y)

    def instantMove(self, event):
        if hasattr(self, "instantMoveAnim"):
            if self.sprite == self.num_sprintes["instantMove"] - 1 and self.state == "instantMove":
                self.x = event.x
                self.y = event.y
                self.state = "idleRight"
                return
            elif self.state == "instantMove":
                self.show()
            else:
                self.state = "instantMove"
            self.canvas.after(200, self.instantMove, event)

    # On effectue l'attaque spéciale lorsque l'on presse la touche
    def specialAttack(self, event):
        if self.state == "idleRight" or self.state == "attackRight" or self.state == "runRight":
            self.state = "specialMoveRight"
        elif self.state == "idleLeft" or self.state == "attackLeft" or self.state == "runLeft":
            self.state = "specialMoveLeft"

    # Fonction chargée de la transformation du heros
    def transform(self):

        # On réinitialise l'image d'animation
        self.sprite = 0
        self.state = "transform"

        # On annule le mouvement
        if self.move:
            self.canvas.after_cancel(self.move)

        # On change les stats et les animations
        if self.lvl == 0:

            self.lvl = 1
            self.changeStats(self.lv1)

            self.idleRight = self.idleRight1
            self.idleLeft = self.idleLeft1
            self.runRight = self.runRight1
            self.runLeft = self.runLeft1
            self.specialMoveRight = self.specialMoveRight1
            self.specialMoveLeft = self.specialMoveLeft1
            self.attackLeft = self.attackLeft1
            self.attackRight = self.attackRight1
            self.death = self.death1
            self.instantMoveAnim = self.instantMoveAnim1

        elif self.lvl == 1:
            self.lvl = 2

            self.changeStats(self.lv2)

            self.idleRight = self.idleRight2
            self.idleLeft = self.idleLeft2
            self.runRight = self.runRight2
            self.runLeft = self.runLeft2
            self.specialMoveRight = self.specialMoveRight2
            self.specialMoveLeft = self.specialMoveLeft2
            self.attackLeft = self.attackLeft2
            self.attackRight = self.attackRight2
            self.death = self.death2
            self.instantMoveAnim = self.instantMoveAnim2

        elif self.lvl == 2:
            self.lvl = 3

            self.changeStats(self.lv3)

            self.idleRight = self.idleRight3
            self.idleLeft = self.idleLeft3
            self.runRight = self.runRight3
            self.runLeft = self.runLeft3
            self.specialMoveRight = self.specialMoveRight3
            self.specialMoveLeft = self.specialMoveLeft3
            self.attackLeft = self.attackLeft3
            self.attackRight = self.attackRight3
            self.death = self.death3
            self.instantMoveAnim = self.instantMoveAnim3

        # On change la vie de base
        self.baseHp = self.hp

    # Fonction chargé du changement de statistiques en fonction du dictionnaire donné
    def changeStats(self, dict):
        self.hp = dict["hp"]
        self.damage = dict["damage"]
        self.damagingSprite = dict["damagingSprite"]
        self.speed = dict["speed"]
        self.coupSpe = dict["coupSpe"]
        self.attackSpeed = dict["attackSpeed"]
        self.spritesheet = dict["spritesheet"]
        self.spriteSize = dict["spriteSize"]
        self.y_Anim = dict["y_Anim"]

    # Incrémentation du sprite en fonction de l'état
    def incrementSprite(self):
        reg = 1
        # Régénration du Héros
        if (self.sprite == self.num_sprintes["idleRight"] - 1 or self.sprite == self.num_sprintes["idleLeft"]-1) and (self.state == "idleRight"or self.state == "idleLeft") and self.hp + reg <= self.baseHp:
            self.hp += reg

        # Si on a fini de se transformer
        if "transform" in self.num_sprintes:
            if self.sprite == self.num_sprintes["transform"] - 1 and self.state == "transform":
                if self.lvl == 1:
                    self.transformAnim = self.transformAnim1
                    self.num_sprintes = self.lv1["num_sprintes"]

                elif self.lvl == 2:
                    self.transformAnim = self.transformAnim2
                    self.num_sprintes = self.lv2["num_sprintes"]

                elif self.lvl == 3:
                    self.num_sprintes = self.lv3["num_sprintes"]
                self.state = "idleLeft"
                self.sprite = 0
        if (self.sprite == self.num_sprintes["specialMoveRight"] - 1 and self.state == "specialMoveRight"):
            self.state = "idleRight"
        elif (self.sprite == self.num_sprintes["specialMoveLeft"] - 1 and self.state == "specialMoveLeft"):
            self.state = "idleLeft"
        super().incrementSprite()


class Adventurer(Heros):

    name = "Aventurier"

    lv0 = {
        "hp": 100,
        "damage": 4,
        "speed": 8,
        "attackSpeed": 4,

        # Spritesheet du Heros
        "barOffsety": 10,
        "damagingSprite": [1, 2, 3, 4],
        "num_sprintes": {"idleLeft": 13, "idleRight": 13, "runRight": 8,
                         "runLeft": 8, "attackRight": 10, "attackLeft": 10, "die": 7},
        "spritesheet": "view/src/personnage/heros/Aventurier/Adventurer.png",
        "spriteSize": 32,
        "zoom": 2,
        "y_Anim": {"idleLeft": 256, "idleRight": 0, "runRight": 32, "runLeft": 288,
                   "attackRight": 64, "attackLeft": 324, "die": 224}
    }

    def __init__(self, canvas, x, y, max_y, min_y):
        Heros.__init__(self, canvas, x, y, max_y, min_y)
        self.max_y -= 5
        self.min_y -= 5

    def transform(self):
        pass


class Ichigo(Heros):
    # Stats du Héros
    name = "Ichigo"

    lv0 = {
        "hp": 50,
        "damage": 2,
        "speed": 8,
        "coupSpe": GetsugaTenshou,
        "attackSpeed": 4,

        # Spritesheet du Heros
        "damagingSprite": [2, 3, 5, 12, 13],
        "num_sprintes": {"idleRight": 2, "idleLeft": 2, "runRight": 8,
                         "runLeft": 8, "attackRight": 16, "attackLeft": 16, "specialMoveRight": 19, "specialMoveLeft": 19, "die": 2, "transform": 20},
        "spritesheet": "view/src/personnage/heros/Ichigo/Ichigo0.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idleRight": 0, "idleLeft": 200, "runRight": 400, "runLeft": 600,
                   "attackRight": 800, "attackLeft": 1000, "die": 0, "specialMoveRight": 1200, "specialMoveLeft": 1400, "transform": 1800}
    }

    lv1 = {
        "hp": 50,
        "damage": 2,
        "speed": 8,
        "coupSpe": GetsugaTenshou2,
        "attackSpeed": 6,

        # Spritesheet du Heros
        "damagingSprite": [2, 3, 7, 8, 9, 13, 14, 17, 18],
        "num_sprintes": {"idleRight": 2, "idleLeft": 2, "runRight": 8, "instantMove":2,
                         "runLeft": 8, "attackRight": 23, "attackLeft": 23, "die": 2, "transform": 7, "specialMoveRight": 13, "specialMoveLeft": 13},
        "spritesheet": "view/src/personnage/heros/Ichigo/Ichigo1.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idleRight": 0, "idleLeft": 200, "runRight": 400, "runLeft": 600, "instantMove":800,
                   "attackRight": 1200, "attackLeft": 1400, "die": 0, "specialMoveRight": 1600, "specialMoveLeft": 1800, "transform": 2200}
    }

    lv2 = {
        "hp": 50,
        "damage": 2,
        "speed": 8,
        "coupSpe": GetsugaTenshou3,
        "attackSpeed": 6,

        # Spritesheet du Heros
        "damagingSprite": [1, 2, 6, 7, 11, 12, 13, 14],
        "num_sprintes": {"idleRight": 2, "idleLeft": 2, "runRight": 8, "instantMove":2,
                         "runLeft": 8, "attackRight": 18, "attackLeft": 18, "die": 2, "transform": 6, "specialMoveRight": 14, "specialMoveLeft": 14},
        "spritesheet": "view/src/personnage/heros/Ichigo/Ichigo2.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idleRight": 0, "idleLeft": 200, "runRight": 800, "runLeft": 1000, "instantMove":400,
                   "attackRight": 1200, "attackLeft": 1400, "specialMoveRight": 1600, "specialMoveLeft": 1800, "die": 0, "transform": 2200}
    }

    lv3 = {
        "hp": 50,
        "damage": 2,
        "speed": 8,
        "attackSpeed": 6,
        "coupSpe" : Mugetsu,
        # Spritesheet du Heros
        "damagingSprite": [1, 2, 6, 7, 11, 12, 13, 14],
        "num_sprintes": {"idleRight": 4, "idleLeft": 4, "runRight": 2, "instantMove":2,
                         "runLeft": 2, "attackRight": 6, "attackLeft": 6, "die": 2, "specialMoveRight": 14, "specialMoveLeft": 14},
        "spritesheet": "view/src/personnage/heros/Ichigo/Ichigo3.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idleRight": 0, "idleLeft": 200, "runRight": 800, "runLeft": 1000, "instantMove": 400,
                   "attackRight": 1200, "attackLeft": 1400, "specialMoveRight": 1600, "specialMoveLeft": 1800, "die": 0}
    }


class Goku(Heros):
    name = "Son Goku"
    lv0 = {
        "hp": 50,
        "damage": 2,
        "damagingSprite": [5, 10, 11, 12, 13, 18, 22, 23],
        "speed": 10,
        "coupSpe": Kamehameha,
        "attackSpeed": 3,
        "num_sprintes": {"idleRight": 8, "idleLeft": 8, "runRight": 4,
                         "runLeft": 4, "attackRight": 15, "attackLeft": 15, "die": 8, "transform": 9, "specialMoveRight": 16, "specialMoveLeft": 16},
        "spritesheet": "view/src/personnage/heros/Goku/Goku0.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idleRight": 0, "idleLeft": 200, "runRight": 400, "runLeft": 600,
                   "attackRight": 1200, "attackLeft": 1400, "die": 200, "transform": 2200, "specialMoveRight": 1600, "specialMoveLeft": 1800}
    }

    lv1 = {
        "hp": 50,
        "damage": 4,
        "damagingSprite": [2, 3, 4, 5, 6, 7, 12, 13, 14, 15],
        "speed": 15,
        "coupSpe": Kamehameha2,
        "attackSpeed": 3,
        "num_sprintes": {"idleRight": 4, "idleLeft": 4, "runRight": 4,
                         "runLeft": 4, "attackRight": 15, "attackLeft": 15, "die": 4, "transform": 8, "specialMoveRight": 17, "specialMoveLeft": 17, "instantMove":4},
        "spritesheet": "view/src/personnage/heros/Goku/Goku1.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idleRight": 0, "idleLeft": 200, "runRight": 400, "runLeft": 600, "instantMove":800,
                   "attackRight": 1200, "attackLeft": 1400, "die": 200, "transform": 2200, "specialMoveRight": 1600, "specialMoveLeft": 1800}
    }

    lv2 = {
        "hp": 50,
        "damage": 4,
        "damagingSprite": [1, 2, 3, 5, 6, 7, 8, 12, 13, 16, 17, 21, 22, 23, 24, 25],
        "speed": 20,
        "coupSpe": Kamehameha3,
        "attackSpeed": 5,
        "num_sprintes": {"idleRight": 4, "idleLeft": 4, "runRight": 4,
                         "runLeft": 4, "attackRight": 26, "attackLeft": 26, "die": 4, "transform": 8, "specialMoveRight": 17, "specialMoveLeft": 17, "instantMove":3},
        "spritesheet": "view/src/personnage/heros/Goku/Goku2.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idleRight": 0, "idleLeft": 200, "runRight": 400, "runLeft": 600, "instantMove":800,
                   "attackRight": 1200, "attackLeft": 1400, "die": 200, "transform": 2200, "specialMoveRight": 1600, "specialMoveLeft": 1800}
    }

    lv3 = {
        "hp": 50,
        "damage": 4,
        "speed": 25,
        "attackSpeed": 5,
        "coupSpe": Genkidamasupreme,
        "damagingSprite": [3, 7, 10, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24],
        "num_sprintes": {"idleRight": 4, "idleLeft": 4, "runRight": 4,
                         "runLeft": 4, "attackRight": 24, "attackLeft": 24, "die": 4, "transform": 8, "specialMoveRight": 8, "specialMoveLeft": 8, "instantMove":2},
        "spritesheet": "view/src/personnage/heros/Goku/Goku3.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idleRight": 0, "idleLeft": 200, "runRight": 400, "runLeft": 600, "instantMove":0,
                   "attackRight": 800, "attackLeft": 1000, "die": 200, "specialMoveRight": 1200, "specialMoveLeft": 1400}
    }
