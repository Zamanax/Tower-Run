import tkinter as tk
from threading import Thread
from model.Heros import Heros
from model.Ennemy import ennemies
#@UnusedWildImport 
from model.fonctions_utiles import * 



#____________________________________________________________________________________________________________



class Tower(Thread):
    # Coords de la tour
    # Image de la tour
    lvl = 1
    lv1 = None
    lv2 = None
    lv3 = None
    last_img=None
    seeking=None
    range=0
    d_up=50
    r_up=25
    damage=1

    # Chargement et attribution des différentes propriétés

    def __init__(self, canvas, x, y, projectile):
        Thread.__init__(self)
        self.start()
        self.projectile=projectile
        self.canvas = canvas
        self.x = x
        self.y = y
        self.construction()
        self.seek()
        # self.canvas.after(5000, self.upgrade1)
        
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
                self.tir_p()
                return
        self.canvas.after(250, self.seek)
    
    def upgrade(self):
        if self.lvl == 1:
            self.upgrade1()
        elif self.lvl == 2:
            self.upgrade2()

    def upgrade1(self):
        self.lvl = 2
        self.damage+=self.d_up
        self.range+=self.r_up
        self.canvas.delete(self.last_img)
        #On place la nouvelle
        self.last_img = self.canvas.create_image(
            self.x, self.y, image=self.lv2, anchor="s")
        #On la place au dessus
        self.canvas.tag_raise(self.last_img)

        self.canvas.after(1000000, self.construction, self)
    
    def upgrade2(self):
        self.lvl = 3
        self.damage*=1.25
        self.range+=self.r_up
        self.canvas.delete(self.last_img)
            #On place la nouvelle
        self.last_img = self.canvas.create_image(
            self.x, self.y, image=self.lv3, anchor="s")
        #On la place au dessus
        self.canvas.tag_raise(self.last_img)

        self.canvas.after(1000000, self.construction, self)

    
    def tir_p(self):
        if self.target :
            self.projectile(self.canvas, self.x, self.y, self.target, self.damage)
            if self.target.hp <= 0:
                self.target.die(False)
                self.target = None
                self.canvas.after(1000, self.seek)
                return
            elif ((self.x -self.target.x)**2+(self.y -self.target.y)**2)**0.5>=self.range:
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
            self.img=tk.PhotoImage(file=image)
            self.boom=tk.PhotoImage(file=boom)
            self.canvas=canvas
            self.tx=self.target.x
            self.ty=self.target.y
            self.v=1
            self.tir()   

    # def calctraj(self):  
        
    #     self.tir()
    # Méthode chargée du déplacement des projectiles
    def tir(self):
        
        if type(self.corps)!=None:
            self.canvas.delete(self.corps)

        if self.x==self.tx and self.y==self.ty:
            self.canvas.delete(self.corps)
            # self.corps=self.canvas.create_oval(self.x-5, self.y-5,self.x+5, self.y+5, fill="black")
            self.corps=self.canvas.create_image(self.x, self.y, image=self.img)
            self.target.hp-=self.damage
            self.seek()
            self.canvas.after(5, self.canvas.delete, self.corps)
            return
        

        n_coups=int((((self.x-self.tx)**2+(self.y-self.ty)**2)**0.5)/2)
        self.inc_abs=-(self.x-self.tx)/n_coups
        self.inc_ord=-(self.y-self.ty)/n_coups
        self.x+=self.inc_abs
        self.y+=self.inc_ord
    
        # self.corps=self.canvas.create_oval(self.x-5, self.y-5,self.x+5, self.y+5, fill="black")
        self.corps=self.canvas.create_image(self.x, self.y, image=self.img)
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
        Tower.__init__(self, canvas, x, y,0)
        self.projectile=Boulet
        self.range = 150
        self.damage = 1
        self.speed = 2
        self.zone = 3
        self.damagetype = "fire"

    

    def __str__(self):
        return "Mortier"

class Boulet(Projectile):
    def __init__(self,canvas, x, y, target, damage):
        self.x=x-5
        self.y=y-70
        self.target = target
        self.damage=damage
        Projectile.__init__(self,canvas, "view/src/bouletDeCanon.png", "view/src/bouletDeCanon.png")
    

class Mage(Tower):
    def __init__(self, canvas, x, y):
        self.damage = 4
        self.speed = 2
        self.zone = 1
        Tower.__init__(self, canvas, x, y,0)

class FireM(Tower):
    
    coordsLvl1 = [3, 72, 69, 129]
    coordsLvl2 = [91, 49, 191, 139]
    coordsLvl3 = [203, 3, 313, 141]
    image="view/src/Mage2.png"

    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        self.lv1=load(self.coordsLvl1, self.image)
        self.lv2=load(self.coordsLvl2, self.image)
        self.lv3=load(self.coordsLvl3, self.image)
        Tower.__init__(self, canvas, x, y,0)
        self.damage = 4
        self.speed = 2
        self.zone = 1
        self.range = 150
        self.damagetype = "fire"
        self.projectile=BouleDeFeu
        # self.spritesheet=tk.PhotoImage(file="Mage2.png")

        # self.root.mainloop()
    
    def __str__(self):
        return "FireM"

class WaterM(Tower):
    coordsLvl1=[3,72,82,139]
    coordsLvl2=[91,47,195,139]
    coordsLvl3=[203,0,323,139]
    image="view/src/Mage3.png"
    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        self.lv1=load(self.coordsLvl1, self.image)
        self.lv2=load(self.coordsLvl2, self.image)
        self.lv3=load(self.coordsLvl3, self.image)
        Tower.__init__(self, canvas, x, y,0)
        self.damage = 4
        self.speed = 2
        self.zone = 1
        self.range = 150
        self.damagetype = "water"
        self.projectile=LameDEau

        # self.root.mainloop()
    
    def __str__(self):
        return "WaterM"

class EarthM(Tower):
    image="view/src/Mage1.png"
    coordsLvl1 = [3, 62, 82, 132]
    coordsLvl2= [91, 47, 195, 132]
    coordsLvl3 = [203, 0, 323, 132]

    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        self.lv1=load(self.coordsLvl1, self.image)
        self.lv2=load(self.coordsLvl2, self.image)
        self.lv3=load(self.coordsLvl3, self.image)
        Tower.__init__(self, canvas, x, y,0)
        self.damage = 4
        self.speed = 2
        self.zone = 1
        self.range = 150
        self.damagetype = "earth"
        self.projectile=Caillou
        
        # self.root.mainloop()
    def __str__(self):
        return "EarthM"

class BouleDeFeu(Projectile):
    def __init__(self,canvas, x, y, target, damage):
        self.x=x-5
        self.y=y-70
        self.target = target
        self.damage=damage
        Projectile.__init__(self,canvas, "view/src/flamèche.png", "view/src/flamèche.png")

class LameDEau(Projectile):
    def __init__(self, canvas, x, y, target, damage):
        self.x=x-5
        self.y=y-70
        self.target= target
        self.damage=damage
        Projectile.__init__(self, canvas, "view/src/petit shuriken eau.png", "view/src/petit shuriken eau.png")

class Caillou(Projectile):
    def __init__(self, canvas, x,y, target, damage):
        self.x=x-5
        self.y=y-70
        self.target=target
        self.damage=damage
        Projectile.__init__(self, canvas, "view/src/caillou.png", "view/src/caillou.png")


class Archer(Tower):
    image="view/src/Archer.png"
    coordsLvl1 = [3,51,82,138]
    coordsLvl2 = [91,35,195,144]
    coordsLvl3 = [203,0,295,144]
    range=200
    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        self.lv1=load(self.coordsLvl1, self.image)
        self.lv2=load(self.coordsLvl2, self.image)
        self.lv3=load(self.coordsLvl3, self.image)
        Tower.__init__(self, canvas, x, y,0)
        self.projectile=Fleche
        self.damage = 4
        self.speed = 4
        self.zone = 1
        self.damagetype = "shot"
        # self.root.mainloop()

    def __str__(self):
        return "Archer"

class Fleche(Projectile):
    def __init__(self, canvas, x,y, target, damage):
        self.x=x-5
        self.y=y-70
        self.target=target
        self.damage=damage
        Projectile.__init__(self, canvas, "view/src/flèche.png", "")


class Forgeron(Tower):
    
    coordsLvl1 = [0,0,120,115]
    coordsLvl2 = [125,0,250,115]
    coordsLvl3 = [250,0,380,115]
    image= 'view/src/Forgeron.png'
    def __init__(self, canvas, x,y, heros):
        self.lv1=load(self.coordsLvl1, self.image)
        self.lv2=load(self.coordsLvl2, self.image)
        self.lv3=load(self.coordsLvl3, self.image)
        self.hero=heros
        Tower.__init__(self, canvas, x, y,0)
    

    def seek(self):
        pass

    def tir_p(self):
        pass
    
    def construction(self): 
        Tower.construction(self)
        self.hero.transform(self)

    def upgrade1(self):
        self.lvl = 2
        self.canvas.delete(self.last_img)
        self.last_img = self.canvas.create_image(
                    self.x, self.y, image=self.lv2, anchor="s")
        self.canvas.tag_raise(self.last_img)
        self.canvas.after(1000000, self.construction, self)
        self.hero.transform(self)
    
    def upgrade2(self):
        self.lvl=3
        self.canvas.delete(self.last_img)
        self.last_img = self.canvas.create_image(
                    self.x, self.y, image=self.lv3, anchor="s")
        self.canvas.tag_raise(self.last_img)
        self.canvas.after(1000000, self.construction, self)
        self.hero.transform(self)
    
    def __str__(self):
        return "Forgeron"


def distance(tower, ennemy):
    return ((ennemy.x-tower.x)**2+(ennemy.y-tower.y)**2)**0.5