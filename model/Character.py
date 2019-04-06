import tkinter as tk

class Character ():
    team = ""
    hp = 0
    name = ""
    speed = 0
    damage = 0
    attackSpeed = 0
    state = ""
    position = 0
    target = None
    x = 0
    y = 0

    zoom = 1
    last_img = None
    idle = []
    runRight = []
    runLeft = []
    num_sprintes = {}
    spritesheet = None
    sprite = 0
    spriteSize = 0
    move = None
    y_Anim = {}

    canvas = None

    def __init__ (self, master, x, y) :
        #Stats
        self.x = x
        self.y = y
        self.canvas = master
        self.spritesheet = tk.PhotoImage(file=self.spritesheet)

        self.getSprite()
        
    def attack(self):
        if self.target:
            self.target.hp -= self.damage
            # self.state = "attack"
            # self.show()
            self.canvas.after(int(1000/self.attackSpeed), self.attack)
        else :
            self.state = "idle"

    def die(self):
        self.canvas.delete(self.last_img)
        self.
        self = None

    # Méthode chargée de charger le spritesheet et de le rendre utilisable
    def getSprite(self):
        # Mise en place des découpages de l'image et zoom sur les images (sinon trop petites)
        self.idle = [self.subimage(self.spriteSize*i, self.y_Anim["idle"], self.spriteSize*(i+1), self.y_Anim["idle"]+self.spriteSize).zoom(self.zoom)
                     for i in range(self.num_sprintes["idle"])]

        self.runRight = [self.subimage(self.spriteSize*i, self.y_Anim["runRight"], self.spriteSize*(i+1), self.y_Anim["runRight"]+self.spriteSize).zoom(self.zoom)
                         for i in range(self.num_sprintes["runRight"])]

        self.runLeft = [self.subimage(self.spriteSize*i, self.y_Anim["runLeft"], self.spriteSize*(i+1), self.y_Anim["runLeft"]+self.spriteSize).zoom(self.zoom)
                        for i in range(self.num_sprintes["runLeft"])]
        # Lancement de l'animation
        self.idleAnim()
        self.incrementSprite()

    # Méthode chargée du découpage du spritesheet
    # x1 = abscisse du point en haut à gauche
    # y1 = ordonnée du point en haut à gauche
    # x2 = abscisse du point en bas à droite
    # y2 = ordonnée du point en bas à droite
    def subimage(self, x1, y1, x2, y2):
        # Création de la variable à retourner
        sprite = tk.PhotoImage()

        # Décupage de l'image en Tcl
        sprite.tk.call(sprite, 'copy', self.spritesheet,
                       '-from', x1, y1, x2, y2, '-to', 0, 0)
        return sprite

    # Méthode chargée du placement de l'image d'attente
    def idleAnim(self):
        self.show()

        return self.canvas.after(250, self.idleAnim)

    # Méthode d'incrémentation de l'image à afficher
    def incrementSprite(self):

        # On incrémente le sprite et/ou on reset (en fonction de l'état)
        self.sprite = (self.sprite+1) % self.num_sprintes[self.state]
        # Si on est en attente on attends 200ms etc...
        if self.state == "idle":
            time = 250
        elif self.state == "runRight" or self.state == "runLeft":
            time = 100
        elif self.state == "attackRight" or self.state == "attackLeft":
            time = 50
        # On rappelle la fonction
        self.canvas.after(time, self.incrementSprite)

    # Méthode chargée du changement de position de l'image et du déplacement
    def moveTo(self, x, y):

        # On vérifie s'il on est déjà en train de courrir
        if self.state == "runRight" or self.state == "runLeft":

            # Si on est arrivé on arrete la fonction et on se remet en attente
            if self.x == x and self.y == y:
                self.sprite = 0
                self.state = "idle"
                self.move = None

                return
            # Sinon on se déplace
            elif self.x > x and self.y > y:
                self.x -= 1
                self.y -= 1
            elif self.x < x and self.y < y:
                self.x += 1
                self.y += 1
            elif self.x > x and self.y < y:
                self.x -= 1
                self.y += 1
            elif self.x < x and self.y > y:
                self.x += 1
                self.y -= 1
            elif self.x > x:
                self.x -= 1
            elif self.x < x:
                self.x += 1
            elif self.y > y:
                self.y -= 1
            elif self.y < y:
                self.y += 1
            self.show()
        # Sinon on vérifie que l'on est pas déjà arrivé
        elif self.x != x or self.y != y:
            # Si l'on est trop à droite de l'objectif on court à gauche sinon à droite
            if self.x > x:
                self.state = "runLeft"
            else:
                self.state = "runRight"

        self.move = self.canvas.after(int(100/self.speed), self.moveTo, x, y)
        return

    def show(self) :
        self.canvas.delete(self.last_img)

        if self.state == "runRight" :
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.runRight[self.sprite])
        elif self.state == "runLeft" :
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.runLeft[self.sprite])
        if self.state == "idle" :
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.idle[self.sprite])
    