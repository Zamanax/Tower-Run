import tkinter as tk
from functools import lru_cache
from threading import Thread
from model.fonctions_utiles import coeffdirecteur

class Character (Thread):
    team = ""
    hp = 0
    name = ""
    speed = 0
    damage = 0
    attackSpeed = 0
    state = ""
    
    x = 0
    y = 0
    target = None
    range = 35

    lvl = 0
    barOffsetx  = 0
    barOffsety  = 0
    lv1 = []
    lv2 = []
    zoom = 1
    last_img = None
    idle = []
    idle1 = []
    runRight = []
    runLeft = []

    damagingSprite = []
    attackRight = []
    attackLeft = []
    transformAnim = []
    transformAnim1 = []
    transformAnim2 = []
    death = []
    num_sprintes = {}
    y_Anim = {}

    spritesheet = None
    sprite = 0
    spriteSize = 0

    move = None
    attacking = None
    afterIdle = None
    seeking = None
    incrementing = None
    dying = None

    damageBar = None
    healthBar = None
    canvas = None
    v = 2

    def seek(self):
        pass

    def goToObjective(self):
        pass

    def __init__ (self, parent, x, y) :
        # Threading       
        Thread.__init__(self)
        self.start()
        # self.join()

        # Initialisation de la position
        self.x = x
        self.y = y
        self.parent = parent
        self.canvas = parent.canvas

        self.baseHp = self.hp
        self.getSprite()
        

        
    def attack(self):
        if self.target:
            if ((self.target.x-self.x)**2+(self.target.y-self.y)**2)**0.5>self.range:
                self.target.move = None
                self.target.goToObjective()
                self.goToObjective()
                self.target=None
                self.state ="idle"
                self.attacking = None
                self.seek()
                self.idleAnim()
                return 
            else:
                if self.target.move:
                    self.canvas.after_cancel(self.target.move)
                if self.target.target == None :
                    self.target.target = self
                    self.canvas.after_cancel(self.target.seeking)
                    self.target.attack()
                if self.afterIdle:
                    self.canvas.after_cancel(self.afterIdle)
                if self.x > self.target.x:
                    self.state = "attackLeft"
                else :
                    self.state = "attackRight"
                self.show()

                if self.sprite in self.damagingSprite:
                    self.target.hp -= self.damage

                if self.target.hp <= 0:
                    self.target.die(False)
                    self.target = None
                    self.goToObjective()
        
        else:
            self.state = "idle"
            self.attacking = None
            self.seek()
            self.idleAnim()
            return
        self.attacking = self.canvas.after(int(500/self.attackSpeed), self.attack)
            


    def die(self, delete):
        if delete:
            self.canvas.delete(self.last_img)
            self.canvas.after_cancel(self.dying)
            self = None
            del self
            return

        elif self.state == "die":
            self.show()
            self.canvas.delete(self.damageBar)
            self.canvas.delete(self.healthBar)
            if self.sprite == self.num_sprintes["die"]-1:
                if self.afterIdle:
                    self.canvas.after_cancel(self.afterIdle)
                self.afterIdle = None
                self.canvas.after_cancel(self.incrementing)
                delete = True
                self.dying = self.canvas.after(5000, self.die, delete)
                return 
            self.dying = self.canvas.after(150, self.die, delete)
            
        else :
            self.canvas.delete(self.healthBar)
            self.canvas.delete(self.damageBar)
            self.parent.gold.set(self.parent.gold.get()+self.purse)
            self.canvas.after_cancel(self.move)
            self.canvas.after_cancel(self.seeking)
            if self.attacking:
                self.canvas.after_cancel(self.attacking)
            self.state = "die"
            self.dying = self.canvas.after(150, self.die, delete)
        

    # Méthode chargée de charger le spritesheet et de le rendre utilisable
    @lru_cache(128)
    def getSprite(self):
        self.spritesheet = tk.PhotoImage(file=self.spritesheet)

        # Mise en place des découpages de l'image et zoom sur les images (sinon trop petites)
        self.idle = [self.subimage(self.spriteSize*i, self.y_Anim["idle"], self.spriteSize*(i+1), self.y_Anim["idle"]+self.spriteSize).zoom(self.zoom)
                     for i in range(self.num_sprintes["idle"])]

        self.runRight = [self.subimage(self.spriteSize*i, self.y_Anim["runRight"], self.spriteSize*(i+1), self.y_Anim["runRight"]+self.spriteSize).zoom(self.zoom)
                         for i in range(self.num_sprintes["runRight"])]

        self.runLeft = [self.subimage(self.spriteSize*i, self.y_Anim["runLeft"], self.spriteSize*(i+1), self.y_Anim["runLeft"]+self.spriteSize).zoom(self.zoom)
                        for i in range(self.num_sprintes["runLeft"])]
        self.runLeft.reverse()

        self.attackRight = [self.subimage(self.spriteSize*i, self.y_Anim["attackRight"], self.spriteSize*(i+1), self.y_Anim["attackRight"]+self.spriteSize).zoom(self.zoom)
                        for i in range(self.num_sprintes["attackRight"])]

        self.attackLeft = [self.subimage(self.spriteSize*i, self.y_Anim["attackLeft"], self.spriteSize*(i+1), self.y_Anim["attackLeft"]+self.spriteSize).zoom(self.zoom)
                        for i in range(self.num_sprintes["attackLeft"])]
        self.attackLeft.reverse()

        self.death = [self.subimage(self.spriteSize*i, self.y_Anim["die"], self.spriteSize*(i+1), self.y_Anim["die"]+self.spriteSize).zoom(self.zoom)
                        for i in range(self.num_sprintes["die"])]
        
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
        if self.state == "transform":
            time = 200
        else : 
            time = 250
        self.afterIdle = self.canvas.after(time, self.idleAnim)

    # Méthode d'incrémentation de l'image à afficher
    def incrementSprite(self):
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

                
                    


        # On incrémente le sprite et/ou on reset (en fonction de l'état)
        self.sprite = (self.sprite+1) % self.num_sprintes[self.state]
        # Si on est en attente on attends 200ms etc...
        if self.state == "idle":
            time = 250
        elif self.state == "runRight" or self.state == "runLeft":
            time = 100
        elif self.state == "attackRight" or self.state == "attackLeft":
            time = int(500/self.attackSpeed)
        elif self.state == "transform" :
            time = 200
        elif self.state == "die":
            time = 400
        else :
            time = 200
        # On rappelle la fonction
        self.incrementing = self.canvas.after(time, self.incrementSprite)

    # Méthode chargée du changement de position de l'image et du déplacement
    def moveTo(self, x, y):
        
        # On vérifie s'il on est déjà en train de courrir
        if self.state == "runRight" or self.state == "runLeft":

            if self.x == x+1:
                self.x += 1
            elif self.x == x-1:
                self.x -= 1
            if self.y-1 == y:
                self.y += 1
            elif self.y == y-1:
                self.y -= 1

            # Si on est arrivé on arrete la fonction et on se remet en attente
            if self.x == x and self.y == y:
                self.sprite = 0
                self.state = "idle"
                self.move = None
                return
                

            # Sinon on se déplace
            n_coups=int((((self.x-x)**2+(self.y-y)**2)**0.5)/2)
            self.inc_abs=-(self.x-x)/n_coups
            self.inc_ord=-(self.y-y)/n_coups
            self.x+=self.inc_abs
            self.y+=self.inc_ord

            
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
        if self.sprite >= self.num_sprintes[self.state]:
            self.sprite = 0

        if self.state == "runRight" :
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.runRight[self.sprite])
        elif self.state == "runLeft" :
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.runLeft[self.sprite])
        elif self.state == "attackRight" :
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.attackRight[self.sprite])
        elif self.state == "attackLeft" :
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.attackLeft[self.sprite])
        elif self.state == "transform":
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.transformAnim[self.sprite])
        elif self.state == "idle" :
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.idle[self.sprite])
        elif self.state == "die" :
            self.last_img = self.canvas.create_image(
                self.x, self.y, image=self.death[self.sprite])

        if self.healthBar:
            self.canvas.delete(self.healthBar)
        if self.damageBar :
            self.canvas.delete(self.damageBar)
        # print("base " + str(self.baseHp))
        # print("hp " + str(self.hp))
    
        missingHealth = 40*self.hp/self.baseHp
        
        self.healthBar = self.canvas.create_line(self.x-15+self.barOffsetx,self.y+25+self.barOffsety,self.x+missingHealth-15+self.barOffsetx,self.y+25+self.barOffsety, width= 5, fill="green")
        self.damageBar = self.canvas.create_line(self.x+missingHealth-15+self.barOffsetx,self.y+25+self.barOffsety,self.x+25+self.barOffsetx,self.y+25+self.barOffsety, width= 5, fill="red")
