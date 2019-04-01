import tkinter as tk

class Character (tk.Canvas):
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

    last_img = None
    idle = []
    runRight = []
    runLeft = []
    num_sprintes = 0
    spritesheet = None
    sprite = 0

    canvas = None

    def attack(self):
        if self.target:
            self.target.hp -= self.damage
        else :
            raise NameError("NoTargetError")

    @staticmethod # Méthode chargée de charger le spritesheet et de le rendre utilisable
    def getSprite(self):
        # Mise en place des découpages de l'image et zoom sur les images (sinon trop petites)
        self.idle = [self.subimage(self, 32*i, 0, 32*(i+1), 0+32).zoom(2)
                       for i in range(self.num_sprintes)]

        self.runRight = [self.subimage(self, 32*i, 32, 32*(i+1), 32+32).zoom(2)
                       for i in range(self.num_sprintes)]

        self.runLeft = [self.subimage(self, 32*i, 288, 32*(i+1), 288+32).zoom(2)
                       for i in range(self.num_sprintes)]
        # Lancement de l'animation
        self.updateImage()

    @staticmethod # Méthode chargée du découpage du spritesheet
    # l = abscisse du point en haut à gauche
    # t = ordonnée du point en haut à gauche
    # r = abscisse du point en bas à droite
    # b = ordonnée du point en bas à droite
    def subimage(self, l, t, r, b):
        # Création de la variable à retourner
        sprite = tk.PhotoImage()

        # Décupage de l'image en Tcl
        sprite.tk.call(sprite, 'copy', self.spritesheet,
                    '-from', l, t, r, b, '-to', 0, 0)
        return sprite

    # Méthode chargée du placement de l'image
    def updateImage(self):
        # On efface l'image précédemment affichée
        self.canvas.delete(self.last_img)

        # On place l'image d'après
        self.last_img = self.canvas.create_image(self.x, self.y, image=self.idle[self.sprite])

        # On incrémente le sprite et/ou on reset puis on rappelle la fonction
        self.sprite = ((self.sprite+1) % self.num_sprintes)
        return self.canvas.after(250, self.updateImage)

    # Méthode chargée du changement de position de l'image
    def moveTo(self, x, y):
        if self.x!=x or self.y!=y:
            self.num_sprintes = 8

            if self.x>x:
                self.x-=0.25
                goRight = False
            else:
                self.x+=0.25
                goRight = True
            if self.y>y:
                self.y-=0.25
            else:
                self.y+=0.25

            self.canvas.delete(self.last_img)
            if goRight:
                self.last_img = self.canvas.create_image(self.x, self.y, image=self.runRight[self.sprite])
            else :
                self.last_img = self.canvas.create_image(self.x, self.y, image=self.runLeft[self.sprite])
                
            return self.canvas.after(int(100/self.speed),self.moveTo,x,y)
        else :
            self.num_sprintes = 13
    
    def mouseMove(self, event):
        self.moveTo(event.x, event.y)