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

    last_img = None
    idle = []
    runRight = []
    runLeft = []
    num_sprintes = {}
    spritesheet = None
    sprite = 0
    move = None

    canvas = None

    def attack(self):
        if self.target:
            self.target.hp -= self.damage
        else :
            raise NameError("NoTargetError")

    @staticmethod # Méthode chargée de charger le spritesheet et de le rendre utilisable
    def getSprite(self):
        # Mise en place des découpages de l'image et zoom sur les images (sinon trop petites)
        self.idle = [self.subimage(32*i, 0, 32*(i+1), 0+32).zoom(2)
                       for i in range(self.num_sprintes["idle"])]

        self.runRight = [self.subimage(32*i, 32, 32*(i+1), 32+32).zoom(2)
                       for i in range(self.num_sprintes["runRight"])]

        self.runLeft = [self.subimage(32*i, 288, 32*(i+1), 288+32).zoom(2)
                       for i in range(self.num_sprintes["runLeft"])]
        # Lancement de l'animation
        self.updateImage()
        self.incrementSprite()

    # Méthode chargée du découpage du spritesheet
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
        # On place l'image d'après
        if self.state == "idle" :
            self.canvas.delete(self.last_img)
            self.last_img = self.canvas.create_image(self.x, self.y, image=self.idle[self.sprite], anchor="s")

        return self.canvas.after(250, self.updateImage)

    # On incrémente le sprite et/ou on reset puis on rappelle la fonction
    def incrementSprite(self):
        self.sprite = (self.sprite+1) % self.num_sprintes[self.state]
        if self.state == "idle":
            time = 250
        elif self.state == "runRight" or self.state == "runLeft":
            time = 100
        self.canvas.after(time, self.incrementSprite)


    # Méthode chargée du changement de position de l'image et du déplacement
    def moveTo(self, x, y):
        if self.state == "runRight" or self.state == "runLeft":

            if self.state == "runRight":
                self.canvas.delete(self.last_img)
                self.last_img = self.canvas.create_image(self.x, self.y, image=self.runRight[self.sprite], anchor="s")
            else :
                self.canvas.delete(self.last_img)
                self.last_img = self.canvas.create_image(self.x, self.y, image=self.runLeft[self.sprite], anchor="s")

            
            if self.x==x and self.y==y:
                self.state = "idle"
                self.move = None

                return
            elif self.x>x and self.y>y:
                self.x-=1
                self.y-=1
            elif self.x<x and self.y<y:
                self.x+=1
                self.y+=1
            elif self.x>x and self.y<y:
                self.x-=1
                self.y+=1
            elif self.x<x and self.y>y:
                self.x+=1
                self.y-=1
            elif self.x>x:
                self.x-=1
            elif self.x<x:
                self.x+=1
            elif self.y>y:
                self.y-=1
            elif self.y<y:
                self.y+=1
            
            

            self.move = self.canvas.after(int(100/self.speed),self.moveTo,x,y)
            return

        elif self.x!=x or self.y!=y:
            self.sprite = 0

            if self.x>x:
                self.state = "runLeft"
            else:
                self.state = "runRight"

            if self.state == "runRight":
                self.canvas.delete(self.last_img)
                self.last_img = self.canvas.create_image(self.x, self.y, image=self.runRight[self.sprite], anchor="s")
            else :
                self.canvas.delete(self.last_img)
                self.last_img = self.canvas.create_image(self.x, self.y, image=self.runLeft[self.sprite], anchor="s")
            
           

            self.move = self.canvas.after(int(100/self.speed),self.moveTo,x,y)
            return
            