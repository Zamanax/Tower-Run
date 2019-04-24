import tkinter as tk
import asyncio
from functools import lru_cache
from threading import Thread

from model.Character import Character
import model.Tower as Tow

class Heros(Character):
    # Variables propres au héros
    team = "ally"
    lv0 = {}

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
            self.specialMove = [self.subimage(self.lv0["spriteSize"]*i, self.lv0["y_Anim"]["specialMove"], self.lv0["spriteSize"]*(i+1), self.lv0["y_Anim"]["specialMove"]+self.lv0["spriteSize"]).zoom(self.zoom)
                          for i in range(self.lv0["num_sprintes"]["specialMove"])]
            self.specialMove.reverse()

            self.getLvlSprite(self.lv1)
            self.getLvlSprite(self.lv2)
            self.getLvlSprite(self.lv3)
        
    # Fonction chargée de charger des animations en fonctions des niveaux
    def getLvlSprite(self, dict):
        loop = asyncio.get_event_loop()
        image = tk.PhotoImage(file=dict["spritesheet"])
        if dict != self.lv3:
            tasks = self.getIdleAnim1(dict, image), self.getRunRightAnim1(dict, image), self.getRunLeftAnim1(dict, image), self.getAttackRightAnim1(dict, image), self.getAttackLeftAnim1(dict, image), self.getSpecialMove(dict, image), self.getDeathAnim1(dict, image),self.getTransformAnim1(dict, image)
        else :
            tasks = self.getIdleAnim1(dict, image), self.getRunRightAnim1(dict, image), self.getRunLeftAnim1(dict, image), self.getAttackRightAnim1(dict, image), self.getAttackLeftAnim1(dict, image), self.getSpecialMove(dict, image), self.getDeathAnim1(dict, image)

        if dict == self.lv1:
            self.idle1, self.runRight1, self.runLeft1, self.attackRight1, self.attackLeft1, self.specialMove1, self.death1, self.transformAnim1 = loop.run_until_complete(asyncio.gather(*tasks))
        elif dict == self.lv2:
            self.idle2, self.runRight2, self.runLeft2, self.attackRight2, self.attackLeft2, self.specialMove2, self.death2, self.transformAnim2 = loop.run_until_complete(asyncio.gather(*tasks))
        elif dict == self.lv3:
            self.idle3, self.runRight3, self.runLeft3, self.attackRight3, self.attackLeft3, self.specialMove3, self.death3 = loop.run_until_complete(asyncio.gather(*tasks))
        
#------------------------Fonction chargée de découper les images dans les images--------

    async def getSpecialMove(self, dict, image):
        specialMove = [self.subimage1(image,dict["spriteSize"]*i, dict["y_Anim"]["specialMove"], dict["spriteSize"]*(i+1), dict["y_Anim"]["specialMove"]+dict["spriteSize"]).zoom(self.zoom)
                          for i in range(dict["num_sprintes"]["specialMove"])]
        specialMove.reverse()
        return specialMove

    async def getIdleAnim1(self, dict, image):
        idle1 = [self.subimage1(image,dict["spriteSize"]*i, dict["y_Anim"]["idle"], dict["spriteSize"]*(i+1), dict["y_Anim"]["idle"]+dict["spriteSize"]).zoom(self.zoom)
                          for i in range(self.lv1["num_sprintes"]["idle"])]
        return idle1

    async def getRunRightAnim1(self, dict, image):

        runRight1 = [self.subimage1(image,dict["spriteSize"]*i, dict["y_Anim"]["runRight"], dict["spriteSize"]*(i+1), dict["y_Anim"]["runRight"]+dict["spriteSize"]).zoom(self.zoom)
                              for i in range(self.lv1["num_sprintes"]["runRight"])]
        return runRight1

    async def getRunLeftAnim1(self, dict, image):

        runLeft1 = [self.subimage1(image,dict["spriteSize"]*i, dict["y_Anim"]["runLeft"], dict["spriteSize"]*(i+1), dict["y_Anim"]["runLeft"]+dict["spriteSize"]).zoom(self.zoom)
                             for i in range(dict["num_sprintes"]["runLeft"])]
        runLeft1.reverse()

        return runLeft1

    async def getAttackRightAnim1(self, dict, image):

        attackRight1 = [self.subimage1(image,dict["spriteSize"]*i, dict["y_Anim"]["attackRight"], dict["spriteSize"]*(i+1), dict["y_Anim"]["attackRight"]+self.lv1["spriteSize"]).zoom(self.zoom)
                                 for i in range(dict["num_sprintes"]["attackRight"])]

        return attackRight1

    async def getAttackLeftAnim1(self, dict, image):

        attackLeft1 = [self.subimage1(image,dict["spriteSize"]*i, dict["y_Anim"]["attackLeft"], dict["spriteSize"]*(i+1), dict["y_Anim"]["attackLeft"]+self.lv1["spriteSize"]).zoom(self.zoom)
                                for i in range(dict["num_sprintes"]["attackLeft"])]
        attackLeft1.reverse()

        return attackLeft1

    async def getDeathAnim1(self, dict, image):

        death1 = [self.subimage1(image,dict["spriteSize"]*i, dict["y_Anim"]["die"], dict["spriteSize"]*(i+1), self.lv1["y_Anim"]["die"]+dict["spriteSize"]).zoom(self.zoom)
                           for i in range(dict["num_sprintes"]["die"])]

        return death1

    async def getTransformAnim1(self, dict, image):
        transform1 = [self.subimage1(image,dict["spriteSize"]*i, dict["y_Anim"]["transform"], dict["spriteSize"]*(i+1), self.lv1["y_Anim"]["transform"]+dict["spriteSize"]).zoom(self.zoom)
                           for i in range(dict["num_sprintes"]["transform"])]
        transform1.reverse()
        return transform1
    
    def subimage1(self,image, x1, y1, x2, y2):
        # Création de la variable à retourner
        sprite = tk.PhotoImage()

        # Décupage de l'image en Tcl
        sprite.tk.call(sprite, 'copy', image,
                       '-from', x1, y1, x2, y2, '-to', 0, 0)
        return sprite

#----------------------------------------------------------------------------------------

    # Fonction de recherche des ennemis
    def seek(self):
        # Si on a déjà une cible on attaque
        if self.target:
            self.attack()
        else:
            if self.state == "idle":
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
            self.state = "idle"
            self.canvas.after_cancel(self.move)
            self.move = None
        
        # Si on attaque alors on annule
        if self.attacking:
            self.state = "idle"
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

    # On effectue l'attaque spéciale lorsque l'on presse la touche
    def specialAttack(self, event):
        self.state = "specialMove"
    
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

            self.idle = self.idle1
            self.runRight = self.runRight1
            self.runLeft = self.runLeft1
            self.attackLeft = self.attackLeft1
            self.attackRight = self.attackRight1
            self.death = self.death1

        elif self.lvl == 1:
            self.lvl = 2

            self.changeStats(self.lv2)

            self.idle = self.idle2
            self.runRight = self.runRight2
            self.runLeft = self.runLeft2
            self.attackLeft = self.attackLeft2
            self.attackRight = self.attackRight2
            self.death = self.death2

        elif self.lvl == 2:
            self.lvl = 3

            self.changeStats(self.lv3)

            self.idle = self.idle3
            self.runRight = self.runRight3
            self.runLeft = self.runLeft3
            self.attackLeft = self.attackLeft3
            self.attackRight = self.attackRight3
            self.death = self.death3
        
        # On change la vie de base
        self.baseHp = self.hp

    # Fonction chargé du changement de statistiques en fonction du dictionnaire donné
    def changeStats(self, dict):
        self.hp = dict["hp"]
        self.damage = dict["damage"]
        self.damagingSprite = dict["damagingSprite"]
        self.speed = dict["speed"]
        self.attackSpeed = dict["attackSpeed"]
        self.spritesheet = dict["spritesheet"]
        self.spriteSize = dict["spriteSize"]
        self.y_Anim = dict["y_Anim"]

    # Incrémentation du sprite en fonction de l'état 
    def incrementSprite(self):
        reg = 1
        # Régénration du Héros
        if self.sprite == self.num_sprintes["idle"] - 1 and self.state == "idle" and self.hp + reg <= self.baseHp:
            self.hp += reg

        # Si on a fini de se transformer
        if "transform" in self.num_sprintes:
            if self.sprite == self.num_sprintes["transform"] - 1 and self.state == "transform":
                self.state = "idle"
                if self.lvl == 1:
                    self.transformAnim = self.transformAnim1
                    self.num_sprintes = self.lv1["num_sprintes"]

                elif self.lvl == 2:
                    self.transformAnim = self.transformAnim2
                    self.num_sprintes = self.lv2["num_sprintes"]

                elif self.lvl == 3:
                    self.num_sprintes = self.lv3["num_sprintes"]

            elif self.sprite == self.num_sprintes["specialMove"] - 1 and self.state == "specialMove":
                self.state = "idle"
        super().incrementSprite()

class Adventurer(Heros):

    name = "Aventurier"

    lv0 = {
        "hp" : 100,
        "damage" : 4,
        "speed" : 8,
        "attackSpeed" : 4,

        # Spritesheet du Heros
        "barOffsetx" : -8.5,
        "barOffsety" : 10,
        "damagingSprite" : [1, 2, 3, 4],
        "num_sprintes" : {"idle": 13, "runRight": 8,
                        "runLeft": 8, "attackRight": 10, "attackLeft": 10, "die": 7},
        "spritesheet" : "view/src/Adventurer.png",
        "spriteSize" : 32,
        "zoom" : 2,
        "y_Anim" : {"idle": 0, "runRight": 32, "runLeft": 288,
                "attackRight": 64, "attackLeft": 324, "die": 256}
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
        "attackSpeed": 4,

        # Spritesheet du Heros
        "damagingSprite" : [2,3,5,12,13],
        "num_sprintes": {"idle": 2, "runRight": 8,
                         "runLeft": 8, "attackRight": 16, "attackLeft": 16, "die": 2, "transform": 20},
        "spritesheet": "view/src/Ichigo0.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idle": 0, "runRight": 400, "runLeft": 600,
                   "attackRight": 800, "attackLeft": 1000, "die": 0, "transform": 1800}
    }

    lv1 = {
        "hp": 50,
        "damage": 2,
        "speed": 8,
        "attackSpeed": 6,

        # Spritesheet du Heros
        "damagingSprite" : [2,3,7,8,9,13,14,17,18],
        "num_sprintes": {"idle": 2, "runRight": 8,
                         "runLeft": 8, "attackRight": 23, "attackLeft": 23, "die": 2, "transform": 7},
        "spritesheet": "view/src/Ichigo1.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idle": 0, "runRight": 400, "runLeft": 600,
                   "attackRight": 1200, "attackLeft": 1400, "die": 0, "transform": 2200}
    }

    lv2 = {
        "hp": 50,
        "damage": 2,
        "speed": 8,
        "attackSpeed": 6,

        # Spritesheet du Heros
        "damagingSprite" : [1,2,6,7,11,12,13,14],
        "num_sprintes": {"idle": 2, "runRight": 8,
                         "runLeft": 8, "attackRight": 18, "attackLeft": 18, "die": 2, "transform": 7},
        "spritesheet": "view/src/Ichigo2.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idle": 0, "runRight": 800, "runLeft": 1000,
                   "attackRight": 1200, "attackLeft": 1400, "die": 0, "transform": 1200}
    }

class Goku(Heros):
    name = "Son Goku"
    lv0 = {
        "hp": 50,
        "damage": 2,
        "damagingSprite": [5, 10, 11, 12, 13, 18, 22, 23],
        "speed": 10,
        "attackSpeed": 3,
        "num_sprintes": {"idle": 8, "runRight": 4,
                         "runLeft": 4, "attackRight": 15, "attackLeft": 15, "die": 8, "transform": 9, "specialMove": 16},
        "spritesheet": "view/src/Goku0.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idle": 200, "runRight": 400, "runLeft": 600,
                   "attackRight": 1200, "attackLeft": 1400, "die": 200, "transform": 2200, "specialMove" : 1800}
    }

    lv1 = {
        "hp": 50,
        "damage": 4,
        "damagingSprite": [2, 3, 4, 5, 6, 7, 12, 13, 14, 15],
        "speed": 15,
        "attackSpeed": 3,
        "num_sprintes": {"idle": 4, "runRight": 4,
                         "runLeft": 4, "attackRight": 15, "attackLeft": 15, "die": 4, "transform": 8, "specialMove": 17},
        "spritesheet": "view/src/Goku1.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idle": 200, "runRight": 400, "runLeft": 600,
                   "attackRight": 1200, "attackLeft": 1400, "die": 200, "transform": 2200, "specialMove": 1800}
    }

    lv2 = {
        "hp": 50,
        "damage": 4,
        "damagingSprite": [1, 2, 3, 5, 6, 7, 8, 12, 13, 16, 17, 21, 22, 23, 24, 25],
        "speed": 20,
        "attackSpeed": 5,
        "num_sprintes": {"idle": 4, "runRight": 4,
                         "runLeft": 4, "attackRight": 26, "attackLeft": 26, "die": 4, "transform": 8, "specialMove": 17},
        "spritesheet": "view/src/Goku2.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idle": 200, "runRight": 400, "runLeft": 600,
                   "attackRight": 1200, "attackLeft": 1400, "die": 200, "transform": 2200, "specialMove": 1800}
    }

    lv3 = {
        "hp": 50,
        "damage": 4,
        "speed": 25,
        "attackSpeed": 5,
        "damagingSprite": [3, 7, 10, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24],
        "num_sprintes": {"idle": 4, "runRight": 4,
                         "runLeft": 4, "attackRight": 24, "attackLeft": 24, "die": 4, "transform": 8, "specialMove":8},
        "spritesheet": "view/src/Goku3.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idle": 200, "runRight": 400, "runLeft": 600,
                   "attackRight": 800, "attackLeft": 1000, "die": 200, "specialMove":1400}
    }
