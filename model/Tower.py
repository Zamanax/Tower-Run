import tkinter as tk
from model.Heros import Heros
from model.Ennemy import ennemies
#pour optimiser le chargement des tours, il faut importer le canvas de launchTk.py

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
#____________________________________________________________________________________________________________



class Tower():
    # Coords de la tour
    # Image de la tour
    lv1 = None
    lv2 = None
    lv3 = None
    last_img=None
    seeking=None
    range=0

    # Chargement et attribution des différentes propriétés

    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.construction()
        self.damage=1
        self.seek()
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

    def seek(self):
        for ennemy in ennemies:
            if (((ennemy.x-self.x)**2)+((ennemy.y-self.y)**2))**0.5 < self.range and ennemy.state != "die":
            
                self.target = ennemy
                if self.seeking:
                    self.canvas.after_cancel(self.seeking) 

                self.tir_p()
            else:
                self.seeking = self.canvas.after(250, self.seek)
    
    def tir_p(self):
        if self.target :
            Boulet(self.canvas, self.x, self.y, self.target)
            if self.target.hp <= 0:
                self.target.die(False)
                self.target = None
                self.seek()
                return
            else :
                self.canvas.after(1000, self.tir_p)
        else :
            self.seek()
        

    # def refresh(self):
    #     self.canvas.tag_raise(self.last_img)
    #     self.canvas.after(1,self.refresh)

 


    
# Classe projectile permattant de leur affecter des méthodes
class Projectile(Tower):
    __slot__=('__dict__', "boom", "img")
    
    damage = 0
    target = None
    seeking = None
    corps=None

    # Méthode chargée de l'apparition du projectile
    def __init__(self,canvas, image,boom):
            self.img=tk.PhotoImage(image)
            self.boom=tk.PhotoImage(boom)
            self.canvas=canvas
            self.tir()         
            
    
    
    # Méthode chargée du déplacement des projectiles
    def tir(self):
        
        v=1

        if type(self.corps)!=None:
            self.canvas.delete(self.corps)
            
        if self.x==self.target.x and self.y==self.target.y:
            print("arrivé")
            self.canvas.delete(self.corps)
            self.corps=self.canvas.create_oval(self.x-5, self.y-5,self.x+5, self.y+5, fill="black")
            self.target.hp-=self.damage
            self.seek()
            self.canvas.after(5,self.canvas.delete, self.corps)
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
        # elif self.x > self.target.x:
        #     self.x -= v
        # elif self.x < self.target.x:
        #     self.x += v
        elif self.y > self.target.y:
            self.y -= v
        elif self.y < self.target.y:
            self.y += v

        self.corps=self.canvas.create_oval(self.x, self.y, self.x+20, self.y+20, fill="black")
        self.canvas.after(20,self.tir)

#________________________________________________________________________________________________________________________
                
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
        self.range = 150
       
        self.damage = 1
        self.speed = 1
        self.zone = 3
        self.damagetype = "fire"
        # print("le dico des Tours mon seigneur Ragy contient: "+str(Tower.__dict__))
        # print("le dico des projectiles mon seigneur Ragy contient: "+str(Projectile.__dict__))
        # print("le dico des Mortiers mon seigneur Ragy contient: "+str(Mortier.__dict__))
        # print("le dico des boulets mon seigneur Ragy contient: "+str(Boulet.__dict__))
        
        # self.spritesheet=tk.PhotoImage(file="towers.png")
        # self.root.mainloop()
    
    # def tir_p(self):
    #     # print("TIR!")
    #     Boulet(self.canvas, self.x, self.y+30, self.target)

class Boulet(Projectile):
    damage = 3
    def __init__(self,canvas, x, y, target):
        self.x=x-5
        self.y=y-80
        self.target = target
        Projectile.__init__(self,canvas, "cercle noir.png", "cercle noir.png")
    

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

