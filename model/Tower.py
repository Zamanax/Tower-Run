import tkinter as tk
from model.Heros import Heros
from model.Ennemy import ennemies

# Charge une image pour chaque point demandé

def load(coords, image):
    return subimage(image, coords[0], coords[1], coords[2], coords[3])  # , self.root)


def subimage(spritesheet, l, t, r, b):

        
    sprite = tk.PhotoImage()
    spritesheet = tk.PhotoImage(file=spritesheet)
    sprite.tk.call(sprite, 'copy', spritesheet,
                    '-from', l, t, r, b, '-to', 0, 0)
    
    return sprite


def test_subimage(spritesheet, l, t, r, b, root):

    # root=tk.Tk()
    canvas = tk.Canvas(root)
    sprite = tk.PhotoImage()
    spritesheet = tk.PhotoImage(file=spritesheet)
    sprite.tk.call(sprite, 'coy', spritesheet,
                    '-from', l, t, r, b, '-to', 0, 0)
    canvas.create_image(100, 100, image=sprite)
    canvas.pack()
    # root.mainloop()
    return sprite
#_____________________________________________________________________________________________________________________________________________



class Tower():
    # Coords de la tour
    x = 0
    y = 0
    # Image de la tour
    lv1 = None
    lv2 = None
    lv3 = None
    last_img=None

    # Point de l'image de chaque niveau de tour
    coordsLvl1=None
    coordsLvl2=None
    coordsLvl3=None

    # Chargement et attribution des différentes propriétés

    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.construction()
        self.damage=1
        # self.refresh()

    #Fonction chargée de l'apparition de la tour

    def construction(self):
        #On supprime l'ancienne image
        self.canvas.delete(self.last_img)
        #On place la nouvelle
        self.last_img = self.canvas.create_image(
            self.x, self.y, image=self.lv1, anchor="s")
        #On la place au dessus
        self.canvas.tag_raise(self.last_img)

        self.canvas.after(1000000, self.construction, self)

    #Attribution des variables pour chaque instance de la classe
    __slot__=("__dict__","lv1","lv2","lv3","coordsLvl1", "coordsLvl2","coordsLvl3", "construction")


    # def refresh(self):
    #     self.canvas.tag_raise(self.last_img)
    #     self.canvas.after(1,self.refresh)

 


    
# Classe projectile permattant de leur affecter des méthodes
class Projectile(Tower):
    target = None
    seeking = None
    # Méthode chargée de l'apparition du projectile

    def __init__(self, image,boom,):
            self.img=tk.PhotoImage(image)
            self.boom=tk.PhotoImage(boom)
    
            self.y+=10
            self.seek()
            # if type(self.target)!=None:
            #     self.tir(self.target)
    
    def seek(self):
        for ennemy in ennemies:
            if (((ennemy.x-self.x)**2)+((ennemy.y-self.y)**2))**0.5 < self.range and ennemy.state != "die":
                self.target = ennemy
                if self.seeking:
                    self.canvas.after_cancel(self.seeking)
                self.tir()
            else:
                self.seeking = self.canvas.after(250, self.seek)
                

    # Méthode chargée du déplacement des projectiles
    def tir(self):
        v=5 
        projectile=self.canvas.create_oval(self.x, self.y,self.x+10, self.y+10, fill="black")# image=self.img)
        if self.x==self.target.x and self.y==self.target.y:
            self.canvas.delete(projectile)
            projectile=self.canvas.create_image(self.x, self.y, image=self.boom)
            self.target.hp-=self.damage
            self.seek()
            self.canvas.after(500,self.canvas.delete, projectile)
            return

        elif self.x > self.target.x and self.y > self.target.y:
            self.x -= v
            self.y -= v
        elif self.x < self.target.x and self.y < self.target.y:
            self.y += v
            self.x += v
        elif self.x > self.target.x and self.y < self.target.y:
            self.x -= v
            self.y += v
        elif self.x < self.target.x and self.y > self.target.y:
            self.x += v
            self.y -= v
        elif self.x > self.target.x:
            self.x -= v
        elif self.x < self.target.x:
            self.x += v
        elif self.y > self.target.y:
            self.y -= v
        elif self.y < self.target.y:
            self.y += v
        self.canvas.delete(projectile)
        self.canvas.after(200,self.tir)


                
# Classe des mortiers basés sur le même template que les autres
class Mortier(Tower):
    
    coordsLvl1=[ 16, 54, 85, 142]
    coordsLvl2=[ 91, 30, 191, 142]
    coordsLvl3=[ 203, 3, 313, 142]
    image="view/src/Mortier.png"

    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        
        self.lv1=load(self.coordsLvl1, self.image)
        self.lv2=load(self.coordsLvl2, self.image)
        self.lv3=load(self.coordsLvl3, self.image)
        Tower.__init__(self, canvas, x, y)
       
        self.range=2000
        self.damage = 1
        self.speed = 1
        self.zone = 3
        self.damagetype = "fire"
        Projectile("cercle noir.png", "cercle noir.png", self.x, self.y+50, self.damage, self.range)
        # self.spritesheet=tk.PhotoImage(file="towers.png")
        # self.root.mainloop()

class Boulet(Mortier, Projectile):
    def __init__(self):
        Projectile.__init__(self)
    
    

class Mage(Tower):
    def __init__(self, canvas, x, y):
        Tower.__init__(self, canvas, x, y)
        self.damage = 4
        self.speed = 2
        self.zone = 1


class FireM(Mage):
    
    coordsLvl1 = [3, 72, 69, 129]
    coordsLvl2 = [91, 49, 191, 139]
    coordsLvl3 = [203, 3, 313, 141]
    image="view/src/Mage2.png"

    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        self.lv1=load(self.coordsLvl1, self.image)
        self.lv2=load(self.coordsLvl2, self.image)
        self.lv3=load(self.coordsLvl3, self.image)
        Mage.__init__(self, canvas, x, y)
        self.damagetype = "fire"
        # self.spritesheet=tk.PhotoImage(file="Mage2.png")

        # self.root.mainloop()

class WaterM(Mage):
    coordsLvl1=[3,72,82,139]
    coordsLvl2=[91,47,195,139]
    coordsLvl3=[203,0,323,139]
    image="view/src/Mage3.png"
    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        self.lv1=load(self.coordsLvl1, self.image)
        self.lv2=load(self.coordsLvl2, self.image)
        self.lv3=load(self.coordsLvl3, self.image)
        Mage.__init__(self, canvas, x, y)
        self.damagetype = "water"

        # self.root.mainloop()


class EarthM(Mage):
    image="view/src/Mage1.png"
    coordsLvl1 = [3, 62, 82, 132]
    coordsLvl2= [91, 47, 195, 132]
    coordsLvl3 = [203, 0, 323, 132]

    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        self.lv1=load(self.coordsLvl1, self.image)
        self.lv2=load(self.coordsLvl2, self.image)
        self.lv3=load(self.coordsLvl3, self.image)
        Mage.__init__(self, canvas, x, y)
        self.damagetype = "earth"
        
        # self.root.mainloop()

    

class Archer(Tower):
    image="view/src/Archer.png"
    coordsLvl1 = [3,51,82,138]
    coordsLvl2 = [91,35,195,144]
    coordsLvl3 = [203,0,295,144]
    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        self.lv1=load(self.coordsLvl1, self.image)
        self.lv2=load(self.coordsLvl2, self.image)
        self.lv3=load(self.coordsLvl3, self.image)
        Tower.__init__(self, canvas, x, y)
        self.damage = 4
        self.speed = 4
        self.zone = 1
        self.damagetype = "shot"
        # self.root.mainloop()

def distance(tower, ennemy):
    return ((ennemy.x-tower.x)**2+(ennemy.y-tower.y)**2)**0.5

