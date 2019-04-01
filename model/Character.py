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
    images = []
    num_sprintes = 0
    spritesheet = None

    canvas = None

    def move(self):
        self.position += self.speed

    def attack(self):
        if self.target:
            self.target.hp -= self.damage
        else :
            raise NameError("NoTargetError")

    @staticmethod # Méthode chargée de charger le spritesheet et de le rendre utilisable
    def getSprite(self):
        # Mise en place des découpages de l'image et zoom sur les images (sinon trop petites)
        self.images = [self.subimage(self, 32*i, 0, 32*(i+1), 32).zoom(2)
                       for i in range(self.num_sprintes)]

        # Lancement de l'animation
        self.updateImage(0)

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
    def updateImage(self, sprite):
        # On efface l'image précédemment affichée
        self.canvas.delete(self.last_img)

        # On place l'image d'après
        self.last_img = self.canvas.create_image(self.x, self.y, image=self.images[sprite])

        # On incrémente le sprite et/ou on reset puis on rappelle la fonction
        return self.canvas.after(250, self.updateImage, ((sprite+1) % self.num_sprintes))

    # Méthode chargée du changement de position de l'image
    def moveTo(self, x, y):
        if self.x!=x or self.y!=y:
            if self.x>x:
                self.x-=0.1
            else:
                self.x+=0.1
            if self.y>y:
                self.y-=0.1
            else:
                self.y+=0.1
            self.canvas.after(int(100/self.speed),self.moveTo,x,y)