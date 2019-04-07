import tkinter as tk
from model.Heros import Heros



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
    sprite.tk.call(sprite, 'copy', spritesheet,
                    '-from', l, t, r, b, '-to', 0, 0)
    canvas.create_image(100, 100, image=sprite)
    canvas.pack()
    # root.mainloop()
    return sprite
    
# Classe projectile permattant de leur affecter des méthodes
class projectile():
    # Méthode chargée de l'apparition du projectile
    def __init__(self, image,boom, canvas, x, y, damage):
            self.canvas=canvas
            self.img=tk.PhotoImage(image)
            self.boom=tk.PhotoImage(boom)
            self.px=x
            self.py=y
            self.target=Heros.seek(self)
            self.damage=damage
            self.tir(self.target)

    # Méthode chargée du déplacement des projectiles
    def tir(self, ennemy):
        v=5 
        projectile=self.canvas.create_image(self.px, self.py, image=self.img)
        if self.px==ennemy.x and self.py==ennemy.y:
            self.canvas.delete(projectile)
            projectile=self.canvas.create_image(self.px, self.py, image=self.boom)
            ennemy.hp-=self.damage
            self.canvas.after(500,self.canvas.delete, projectile)
            return

        elif self.px > ennemy.x and self.py > ennemy.y:
            self.px -= v
            self.py -= v
        elif self.px < ennemy.x and self.py < ennemy.y:
            self.py += v
            self.px += v
        elif self.px > ennemy.x and self.py < ennemy.y:
            self.px -= v
            self.py += v
        elif self.px < ennemy.x and self.py > ennemy.y:
            self.px += v
            self.py -= v
        elif self.px > ennemy.x:
            self.px -= v
        elif self.px < ennemy.x:
            self.px += v
        elif self.py > ennemy.y:
            self.py -= v
        elif self.py < ennemy.y:
            self.py += v
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
        self.damage = 5
        self.speed = 1
        self.zone = 3
        self.damagetype = "fire"
        # self.spritesheet=tk.PhotoImage(file="towers.png")
        # self.root.mainloop()
    
    

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
    coordsLvl2= [91,35,195,144]
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

