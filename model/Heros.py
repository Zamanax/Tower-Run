import tkinter as tk
import asyncio
from functools import lru_cache
from threading import Thread
from model.fonctions_utiles import load
from model.Character import Character


class Heros(Character):
    # Variables propres au héros
    team = "ally"
    lv0 = {}
    compteur = 0
    reg = 1

    def defineStats(self):
        pass

    def __init__(self, parent, x, y, max_y, min_y, **kwargs):
        self.quality = int(kwargs.get("quality", 4))

        self.defineStats()

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
        if "coupSpe" in self.lv0:
            self.coupSpe = self.lv0["coupSpe"]
        if "barOffsetx" in self.lv0:
            self.barOffsetx = self.lv0["barOffsetx"]
        if "barOffsety" in self.lv0:
            self.barOffsety = self.lv0["barOffsety"]

        Character.__init__(self, parent, x, y)
        self.redCross = tk.PhotoImage(file="view/src/assets/Cross.png")
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

        if hasattr(self.parent.parent.currentFrame, "progressBar"):
            self.parent.parent.currentFrame.progressBar["value"] = self.compteur
            self.parent.update()
        # Décupage de l'image en Tcl
        sprite.tk.call(sprite, 'copy', image,
                       '-from', int(x1), int(y1), int(x2), int(y2), '-to', 0, 0)
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
        if self.crossCallback:
            self.canvas.delete(self.crossCallback)

        # Si on bouge déjà alors on annule l'ancien mouvement
        if self.move:
            self.canvas.after_cancel(self.move)
            self.move = None
            if self.state == "runRight":
                self.state = "idleRight"
            elif self.state == "runLeft":
                self.state = "idleLeft"
        else:
            self.sprite = 0

        # Si on attaque alors on annule
        if self.attacking:
            self.canvas.after_cancel(self.attack)
            self.attacking = None
            if self.state == "attackRight":
                self.state = "idleRight"
            elif self.state == "attackLeft":
                self.state = "idleLeft"

        # On effectue le mouvement en restant dans les bornes
        if event.y > self.max_y:
            y = self.max_y
        elif event.y < self.min_y:
            y = self.min_y
        else:
            y = event.y
        x = event.x
        
        self.crossCallback = self.canvas.create_image(x, y+25 , image=self.redCross)
        self.canvas.tag_lower(self.crossCallback)
        self.canvas.tag_raise(self.crossCallback, self.parent.background)

        self.moveTo(x, y)

    def reOrient(self, event):
        if self.state is "idleLeft" or self.state is "idleRight":
            if event.keysym == "Right":
                self.state = "idleRight"
            else :
                self.state = "idleLeft"

    def instantMove(self, event):
        if self.lvl != 0 and hasattr(self, "instantMoveAnim"):
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
    def specialAttack(self, *args):
        if hasattr(self, "coupSpe"):
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

            self.idleRight0 = self.idleRight
            self.idleLeft0 = self.idleLeft
            self.runRight0 = self.runRight
            self.runLeft0 = self.runLeft
            self.specialMoveRight0 = self.specialMoveRight
            self.specialMoveLeft0 = self.specialMoveLeft
            self.attackLeft0 = self.attackLeft
            self.attackRight0 = self.attackRight
            self.death0 = self.death
            self.instantMoveAnim0 = self.instantMoveAnim


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
        increment = True

        # Régénration du Héros
        if (self.sprite == self.num_sprintes["idleRight"] - 1 or self.sprite == self.num_sprintes["idleLeft"]-1) and (self.state == "idleRight"or self.state == "idleLeft") and self.hp + self.reg <= self.baseHp:
            self.hp += self.reg

        if self.state == "specialMoveRight" or self.state == "specialMoveLeft":
            if self.sprite == self.num_sprintes["specialMoveRight"] - 1:
                if self.name == "Goku":
                    self.coupSpe(self)
                    increment = False
                # self.state = "idleRight"
            elif self.sprite == self.num_sprintes["specialMoveLeft"] - 1:
                if self.name == "Goku":
                    self.coupSpe(self)
                    increment = False
                # self.state = "idleLeft"

            elif self.sprite == self.num_sprintes["specialMoveRight"] - 4 and self.name == "Ichigo":
                self.coupSpe(self)
                increment = False

        # Si on a fini de se transformer
        elif self.state == "transform":
            if self.sprite == self.num_sprintes["transform"] - 1:
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

        if increment:
            super().incrementSprite()
        else :
            self.incrementing = None

