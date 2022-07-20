# Librairies nécessaires au foncionnement du jeu
import tkinter as tk
from functools import lru_cache
from threading import Thread
import asyncio
import time

from model.State import State


class Character (Thread):
    # ---------------------Attributs------------------------------------------------
    # Statistiques du Character
    team = ""
    hp = 0
    name = ""
    speed = 0
    damage = 0
    attackSpeed = 0
    purse = 0

    #Coordonnées + Etats
    state = State.IdleLeft
    pathIndex = 0
    x = 0
    y = 0
    target = None
    range = 35

# ------------------- Partie utile aux animations et aux héros------------------
    lvl = 0
    barOffsetx = 0
    barOffsety = 0
    lv1 = {}
    lv2 = {}
    lv3 = {}
    zoom = 1

    crossCallback = None
    last_img = None
    idleRight = []
    idleLeft = []
    idleRight1 = []
    idleLeft1 = []
    runRight = []
    runLeft = []
    specialMoveRight = []
    specialMoveLeft = []
    damagingSprite = []
    attackRight = []
    attackLeft = []
    transformAnim = []
    transformAnim1 = []
    transformAnim2 = []
    instantMoveAnim = []
    death = []
    num_sprintes = {}
    y_Anim = {}

    spritesheet = None
    sprite = 0
    spriteSize = 0

    damageBar = None
    healthBar = None
    canvas = None
    v = 2
# ------------------------------------------------------------------------------

    # Partie contenant tous les afters_cancels
    move = None
    attacking = None
    afterIdle = None
    seeking = None
    incrementing = None
    dying = None

# ------------------------------------------------------------------------------

    # Fonction chargée de la destruction du personnage
    def __del__(self):
        for el in self.__dict__:
            del el

    # Fonction nulle car elle dépend de celui qui l'invoque
    def seek(self):
        pass

    # Fonction chargeée d'arriver à la destination nulle car le héros n'en a pas
    def goToObjective(self):
        pass

    # Initialisation de la classe
    def __init__(self, parent, x, y):
        """
        On crée un Thread par personnage ce qui permet de fluidifier le système
        Pour cela :
        1. On instancie le thread
        2. On le lance
        """
        Thread.__init__(self)  # 1.
        self.start()  # 2.

        # Initialisation de la position
        self.x = x
        self.y = y

        # Instanciation des liaisons entre les variables
        self.parent = parent
        self.canvas = parent.canvas

        # On ajoute les HP  de base
        self.baseHp = self.hp

        # On charge les Sprites
        self.getSprite()

    # Fonction générale chargée de l'attaque entre les personnages

    def attack(self):
        # On vérifie que l'on vise bien quelque chose
        if self.target:
            # On utilise le théorème de pythagore pour vérifier qu'il soit à portée
            if ((self.target.x-self.x)**2+(self.target.y-self.y)**2)**0.5 > self.range:
                # Si ce n'est pas le cas tout le monde reprends sa route
                if self.x > self.target.x:
                    self.state = State.IdleLeft
                else:
                    self.state = State.IdleRight

                self.target.goToObjective()
                self.goToObjective()
                self.target = None
                self.attacking = None
                self.seek()
                self.idleAnim()
                return
            else:
                # Si c'est le cas alors on arrêtes les tâches parrallèles et on attaque
                if self.target.move and self.target.__class__.__bases__[0].__name__ != "Heros":
                    self.canvas.after_cancel(self.target.move)
                    self.target.move = None
                if self.target.target == None:
                    self.target.target = self
                    if self.target.seeking:
                        self.canvas.after_cancel(self.target.seeking)
                    self.target.attack()
                if self.afterIdle:
                    self.canvas.after_cancel(self.afterIdle)
                if self.x > self.target.x:
                    self.state = State.AttackLeft
                else:
                    self.state = State.AttackRight
                self.show()

                # Si l'animation à laquelle on est doit faire des dégats alors seulement on en fait
                if self.sprite in self.damagingSprite:
                    self.target.hp -= self.damage
                    self.parent.interface.updateHp()

                # Si la cible a un nombre de point de vie négatif ou nul il meurt et on reprend sa route
                if self.target.hp <= 0:
                    self.target.die(False)
                    self.target = None
                    self.goToObjective()

        else:
            # Si on n'a pas de cible alors on reprends sa route
            if self.state == State.AttackRight:
                self.state = State.IdleRight
            else:
                self.state = State.IdleLeft
            self.attacking = None
            self.seek()
            self.idleAnim()
            return
        # Et on recommence autant de fois que nécessaire
        # plus ou moins rapidement en fonction de la vitesse d'attaque
        self.attacking = self.canvas.after(
            int(500/self.attackSpeed), self.attack)

    # Fonction générale chargée de tuer un personnage

    def die(self, delete):
        # Si l'on doit supprimer le personnage alors on supprime l'image
        # et on efface les références pour optimiser
        if delete:
            self.canvas.delete(self.last_img)
            self.canvas.after_cancel(self.dying)

            self.parent.winGame()

            del self
            return

        # Si le personnage est déjà en train de mourrir alorso continue
        elif self.state == State.Die:
            self.show()

            # Si l'animation de mort est déjà finie alors on supprime
            if self.sprite == self.num_sprintes[State.Die]-1:
                if self.afterIdle:
                    self.canvas.after_cancel(self.afterIdle)
                self.afterIdle = None
                self.canvas.after_cancel(self.incrementing)
                delete = True
                # Avec 5s de temps d'attente
                self.dying = self.canvas.after(5000, self.die, delete)
                return
            self.dying = self.canvas.after(150, self.die, delete)

        # Si c'est le début de la mort alors on ajoute l'argent de sa bourse
        else:
            self.parent.gold.set(self.parent.gold.get()+self.purse)
            self.parent.interface.preView()

            # On coupe toutes les autres tâches
            if self.move:
                self.canvas.after_cancel(self.move)
            if self.seeking:
                self.canvas.after_cancel(self.seeking)
            if self.attacking:
                self.canvas.after_cancel(self.attacking)

            # On mets son état en "mort"
            self.state = State.Die
            self.dying = self.canvas.after(150, self.die, delete)

    """
    # Méthode chargée de charger le spritesheet et de le rendre utilisable
    # On change le cache CPU de la fonction en utilisant le lru_cache
    # Ce qui permet d'accroître les performances
    """
    @lru_cache(128)
    def getSprite(self):
        # On charge le spritesheet du personnage
        self.spritesheet = tk.PhotoImage(file=self.spritesheet)

        # Ici, on utlise la librairie asyncio pour charger les animations de manières asynchrones et aller plus vite
        # On cherche l'événement dans le quel on est
        loop = asyncio.get_event_loop()

        # On utilise un tuple pour lui donner les animations à charger
        tasks = self.getIdleRightAnim(), self.getIdleLeftAnim(), self.getRunRightAnim(
        ), self.getRunLeftAnim(), self.getAttackRightAnim(), self.getAttackLeftAnim(), self.getDeathAnim()

        # On attends les résultats de chaque fonction
        (self.idleRight, self.idleLeft, self.runRight, self.runLeft, self.attackRight,
         self.attackLeft, self.death) = loop.run_until_complete(asyncio.gather(*tasks))
        # On lance l'animation
        self.idleAnim()
        self.incrementSprite()

# -----------------------Méthode chargée du découpage de l'image en fonction de l'animation désirée---------------------
    async def getIdleRightAnim(self):
        idleRight = [self.subimage(self.spriteSize*i, self.y_Anim[State.IdleRight], self.spriteSize*(i+1), self.y_Anim[State.IdleRight]+self.spriteSize).zoom(self.zoom)
                     for i in range(self.num_sprintes[State.IdleRight])]

        return idleRight

    async def getIdleLeftAnim(self):
        idleLeft = [self.subimage(self.spriteSize*i, self.y_Anim[State.IdleLeft], self.spriteSize*(i+1), self.y_Anim[State.IdleLeft]+self.spriteSize).zoom(self.zoom)
                    for i in range(self.num_sprintes[State.IdleLeft])]

        idleLeft.reverse()
        return idleLeft

    async def getRunRightAnim(self):

        runRight = [self.subimage(self.spriteSize*i, self.y_Anim[State.RunRight], self.spriteSize*(i+1), self.y_Anim[State.RunRight]+self.spriteSize).zoom(self.zoom)
                    for i in range(self.num_sprintes[State.RunRight])]

        return runRight

    async def getRunLeftAnim(self):

        runLeft = [self.subimage(self.spriteSize*i, self.y_Anim[State.RunLeft], self.spriteSize*(i+1), self.y_Anim[State.RunLeft]+self.spriteSize).zoom(self.zoom)
                   for i in range(self.num_sprintes[State.RunLeft])]

        runLeft.reverse()

        return runLeft

    async def getAttackRightAnim(self):

        attackRight = [self.subimage(self.spriteSize*i, self.y_Anim[State.AttackRight], self.spriteSize*(i+1), self.y_Anim[State.AttackRight]+self.spriteSize).zoom(self.zoom)
                       for i in range(self.num_sprintes[State.AttackRight])]

        return attackRight

    async def getAttackLeftAnim(self):

        attackLeft = [self.subimage(self.spriteSize*i, self.y_Anim[State.AttackLeft], self.spriteSize*(i+1), self.y_Anim[State.AttackLeft]+self.spriteSize).zoom(self.zoom)
                      for i in range(self.num_sprintes[State.AttackLeft])]

        # attackLeft.reverse()

        return attackLeft

    async def getDeathAnim(self):

        death = [self.subimage(self.spriteSize*i, self.y_Anim[State.Die], self.spriteSize*(i+1), self.y_Anim[State.Die]+self.spriteSize).zoom(self.zoom)
                 for i in range(self.num_sprintes[State.Die])]

        return death
# ----------------------------------------------------------------------------------------------------------------------

    # Méthode chargée du découpage du spritesheet
    # x1 = abscisse du point en haut à gauche
    # y1 = ordonnée du point en haut à gauche
    # x2 = abscisse du point en bas à droite
    # y2 = ordonnée du point en bas à droite
    def subimage(self, x1, y1, x2, y2):
        # Création de la variable à retourner
        sprite = tk.PhotoImage()
        self.parent.update()
        # Décupage de l'image en Tcl à partir de l'image du personnage et des coordonnées
        sprite.tk.call(sprite, 'copy', self.spritesheet,
                       '-from', int(x1), int(y1), int(x2), int(y2), '-to', 0, 0)
        return sprite

    # Méthode chargée du placement de l'image sans déplacement
    def idleAnim(self):
        # On modifie le temps que l'on mets pour rappeler la fonction selon l'état du personnage
        if self.state == State.Transform:
            time = 200
        elif self.state == State.SpecialMoveRight or self.state == State.SpecialMoveLeft:
            time = 300
        else:
            time = 250
        self.show()

        # On rappelle la fonction
        self.afterIdle = self.canvas.after(time, self.idleAnim)

    # Méthode d'incrémentation de l'image à afficher
    def incrementSprite(self, **kwargs):
        time = kwargs.get("time", 0)
        # On incrémente le sprite et/ou on reset (en fonction de l'état et du nombre d'animation)

        if time == 0:
            self.sprite = (self.sprite+1) % self.num_sprintes[self.state]

        # Selon l'état on modifie le temps d'incrémentation
            if self.state == State.IdleLeft or self.state == State.IdleRight:
                time = 250
            elif self.state == State.RunRight or self.state == State.RunLeft:
                time = 100
            elif self.state == State.AttackRight or self.state == State.AttackLeft:
                time = int(500/self.attackSpeed)
            elif self.state == State.Transform:
                time = 200
            elif self.state == State.SpecialMoveLeft or self.state == State.SpecialMoveRight:
                time = 300
            elif self.state == State.Die:
                time = 400
            else:
                time = 200

        # On rappelle la fonction
        self.incrementing = self.canvas.after(time, self.incrementSprite)

    def moveTo(self, x, y):
        self.n_coups = int((((self.x-x)**2+(self.y-y)**2)**0.5)/2)
        if self.n_coups == 0:
            self.n_coups = 1
        self.inc_abs = -(self.x-x)/self.n_coups
        self.inc_ord = -(self.y-y)/self.n_coups
        self.move = self.canvas.after(int(200/self.speed), self.Move, x, y)

    # Méthode chargée du déplacement de la position de base jusqu'à un point donné
    def Move(self, x, y):

        # On vérifie s'il on est déjà en train de courrir
        if (self.state == State.RunRight or self.state == State.RunLeft) or (self.x == x and self.y == y):
            # Dans ce cas on change sa position
            if self.n_coups == 1:
                self.x = x
                self.y = y

            # Si on est arrivé on arrete la fonction et on se remet en attente
            if self.x == x and self.y == y:
                self.move = None
                self.pathIndex += 1
                self.goToObjective()
                self.sprite = 0
                if self.state == State.RunRight:
                    self.state = State.IdleRight
                elif self.state == State.RunLeft:
                    self.state = State.IdleLeft
                if self.crossCallback:
                    self.canvas.delete(self.crossCallback)
                return

            # Sinon on se déplace
            self.x += self.inc_abs
            self.y += self.inc_ord
            self.n_coups -= 1

            self.show()

        # Sinon on vérifie que l'on est pas déjà arrivé
        elif self.x != x or self.y != y:
            # Si l'on est trop à droite de l'objectif on court à gauche sinon à droite
            if self.x > x:
                self.state = State.RunLeft
            else:
                self.state = State.RunRight

        else:
            self.move = None
            self.pathIndex += 1
            self.goToObjective()
            if self.crossCallback:
                self.canvas.delete(self.crossCallback)

        # On relance la fonction en fonction de la vitesse du personnage
        self.move = self.canvas.after(int(200/self.speed), self.Move, x, y)

    # Fonction chargée de l'affichage du personnage en fonction de son état
    def show(self):
        # On supprime l'ancienne image
        if self.last_img:
            self.canvas.delete(self.last_img)
        # Si on dépasse le tableau on recommence à la première image
        if self.sprite > self.num_sprintes[self.state] - 1:
            self.sprite = 0

        # On affiche la bonne image en fonction de l'état
        if self.state == State.RunRight:
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.runRight[self.sprite])
        elif self.state == State.RunLeft:
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.runLeft[self.sprite])
        elif self.state == State.AttackRight:
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.attackRight[self.sprite])
        elif self.state == State.AttackLeft:
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.attackLeft[self.sprite])

        elif self.state == State.Transform:
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.transformAnim[self.sprite])
        elif self.state == State.SpecialMoveRight:
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.specialMoveRight[self.sprite])
        elif self.state == State.SpecialMoveLeft:
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.specialMoveLeft[self.sprite])
        elif self.state == State.IdleRight:
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.idleRight[self.sprite])
        elif self.state == State.IdleLeft:
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.idleLeft[self.sprite])
        elif self.state == State.Die:
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.death[self.sprite])
        elif self.state == State.InstantMove:
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.instantMoveAnim[self.sprite])

        #  On supprime l'ancienne barre de vie
        if self.healthBar:
            self.canvas.delete(self.healthBar)
        if self.damageBar:
            self.canvas.delete(self.damageBar)

        # Si seulement on est pas mort alors on affiche une barre de vie
        if self.state != State.Die:
            # On calcule la vie manquante sur 40 pixel
            missingHealth = 40*self.hp/self.baseHp

            # Si on a assez de vie pour afficher une barre on le fait
            if self.hp > 0:
                # La barre de vie
                self.healthBar = self.canvas.create_line(self.x-15+self.barOffsetx, self.y+25+self.barOffsety,
                                                         self.x+missingHealth-15+self.barOffsetx, self.y+25+self.barOffsety, width=5, fill="green")

                # La barre de vie manquante
                self.damageBar = self.canvas.create_line(self.x+missingHealth-15+self.barOffsetx, self.y+25 +
                                                         self.barOffsety, self.x+25+self.barOffsetx, self.y+25+self.barOffsety, width=5, fill="red")

            else:
                self.damageBar = self.canvas.create_line(
                    self.x-15+self.barOffsetx, self.y+25+self.barOffsety, self.x+25+self.barOffsetx, self.y+25+self.barOffsety, width=5, fill="red")

        for spot in self.parent.spots:
            if spot.tower:
                try:
                    if spot.tower.last_img:
                        if spot.tower.y <= self.y:
                            self.canvas.tag_lower(
                                self.last_img, spot.tower.last_img)
                            self.canvas.tag_lower(
                                self.healthBar, spot.tower.last_img)
                            self.canvas.tag_lower(
                                self.damageBar, spot.tower.last_img)
                except:
                    None
