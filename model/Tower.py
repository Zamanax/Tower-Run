import tkinter as tk
from threading import Thread
from model.Heros import Heros
from model.Ennemy import ennemies
from model.fonctions_utiles import * #@UnusedWildImport 

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
    speed=3
    damage_evo=[damage, damage+d_up, (damage+d_up)*1.25]
    range_evo=[range, range+r_up, range+r_up*2] 
    speed_evo=[speed, speed+2, speed+6]
    price_evo=[0,0,0]
    # Chargement et attribution des différentes propriétés

    def __init__(self, canvas, x, y, projectile):
        Thread.__init__(self)
        self.start()
        self.price=self.price_evo[1]
        self.projectile=projectile
        self.canvas = canvas
        self.x = x
        self.y = y
        self.ndamage=self.damage_evo[1]
        self.nrange=self.range_evo[1]
        self.nspeed=self.speed_evo[1]
        self.construction()
        self.seek()
        # self.canvas.after(5000, self.upgrade1)
        
        # self.refresh()

    #Fonction chargée de l'apparition de la tour

    def construction(self):
        #On supprime l'ancienne image
        self.canvas.delete(self.last_img)

        # self.ndamage = self.damage + self.d_up       
        #On place la nouvelle
        self.last_img = self.canvas.create_image(
            self.x, self.y, image=self.lv1, anchor="s")
        #On la place au dessus
        self.canvas.tag_raise(self.last_img)

        # self.canvas.after(1000000, self.construction, self)

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
        self.damage=self.damage_evo[1]
        self.ndamage=self.damage_evo[2]
        self.range=self.range_evo[1]
        self.nrange=self.range_evo[2]
        self.speed=self.speed_evo[1]
        self.nspeed=self.speed_evo[2]
        self.price=self.price_evo[2]
        self.canvas.delete(self.last_img)
        #On place la nouvelle
        self.last_img = self.canvas.create_image(
            self.x, self.y, image=self.lv2, anchor="s")
        #On la place au dessus
        self.canvas.tag_raise(self.last_img)

        # self.canvas.after(1000000, self.construction, self)
    
    def upgrade2(self):
        self.lvl = 3
        self.damage=self.damage_evo[2]
        self.ndamage="Max"
        self.range=self.range_evo[2]
        self.nrange="Max"
        self.speed=self.speed_evo[2]
        self.nspeed="Max"
        self.price=""
        self.canvas.delete(self.last_img)
            #On place la nouvelle
        self.last_img = self.canvas.create_image(
            self.x, self.y, image=self.lv3, anchor="s")
        #On la place au dessus
        self.canvas.tag_raise(self.last_img)
       

        # self.canvas.after(1000000, self.construction, self)

    
    def tir_p(self):
        if self.target :
            self.projectile(self.canvas, self.x, self.y, self.target, self.damage)
            if self.target.hp <= 0:
                self.target.die(False)
                self.target = None
                self.canvas.after(int(6000/self.speed), self.seek)
                return
            elif ((self.x -self.target.x)**2+(self.y -self.target.y)**2)**0.5>=self.range:
                self.seek()
                return
            else :
                self.canvas.after(int(6000/self.speed), self.tir_p)
        else :
            self.seek()
    


    # def refresh(self):
    #     self.canvas.tag_raise(self.last_img)
    #     self.canvas.after(1,self.refresh)

# Classe projectile permattant de leur affecter des méthodes
class Projectile(Thread):
    __slot__=('__dict__', "boom", "img")
    x=0
    y=0
    damage = 0
    target = None
    seeking = None
    corps=None

    # Méthode chargée de l'apparition du projectile
    def __init__(self,canvas, image,boom):
        Thread.__init__(self)
        self.start()

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

        if self.tx-10<=self.x<=self.tx+10 and self.ty-5<=self.y<=self.ty+5:
            self.canvas.delete(self.corps)
            # self.corps=self.canvas.create_oval(self.x-5, self.y-5,self.x+5, self.y+5, fill="black")
            self.corps=self.canvas.create_image(self.x, self.y, image=self.img)
            self.target.hp-=self.damage
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
    range = 120
    damage = 1
    speed = 2
    zone = 3
    r_up=25
    damagetype = "explosion"
    d_up=50
    damage_evo=[damage, damage+d_up, (damage+d_up)*1.25]
    range_evo=[range, range+r_up, range+r_up*2]
    speed_evo=[speed, speed+1, speed+2]
    price_evo=[50, 125, 250]
    price=price_evo[0]   

    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        
        self.lv1=load(self.coordsLvl1, self.image)
        self.lv2=load(self.coordsLvl2, self.image)
        self.lv3=load(self.coordsLvl3, self.image)
        Tower.__init__(self, canvas, x, y,Boulet)
      
    def __str__(self):
        return "Mortier"

class FireM(Tower):
    
    coordsLvl1 = [3, 72, 69, 129]
    coordsLvl2 = [91, 49, 191, 139]
    coordsLvl3 = [203, 3, 313, 141]
    image="view/src/Mage2.png"
    damage = 4
    speed = 3
    zone = 1
    range = 150
    r_up=25
    d_up=25
    damagetype = "fire"
    damage_evo=[damage, damage+d_up, (damage+d_up)*1.25]
    range_evo=[range, range+r_up, range+r_up*2]
    price_evo=[50, 125, 250]
    price=price_evo[0]

    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        self.lv1=load(self.coordsLvl1, self.image)
        self.lv2=load(self.coordsLvl2, self.image)
        self.lv3=load(self.coordsLvl3, self.image)
        Tower.__init__(self, canvas, x, y,BouleDeFeu)

        # self.spritesheet=tk.PhotoImage(file="Mage2.png")

        # self.root.mainloop()
    
    def __str__(self):
        return "Mage de Feu"

class WaterM(Tower):
    coordsLvl1=[3,72,82,139]
    coordsLvl2=[91,47,195,139]
    coordsLvl3=[203,0,323,139]
    image="view/src/Mage3.png"
    damage = 4
    speed = 3
    zone = 1
    range = 150
    damagetype = "water"
    d_up=50
    r_up=25
    damage_evo=[damage, damage+d_up, (damage+d_up)*1.25]
    range_evo=[range, range+r_up, range+r_up*2]
    price_evo=[50, 125, 250]
    price=price_evo[0]

    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        self.lv1=load(self.coordsLvl1, self.image)
        self.lv2=load(self.coordsLvl2, self.image)
        self.lv3=load(self.coordsLvl3, self.image)
        Tower.__init__(self, canvas, x, y,LameDEau)

        
        # self.root.mainloop()
    
    def __str__(self):
        return "Mage d'Eau"

class EarthM(Tower):
    image="view/src/Mage1.png"
    coordsLvl1 = [3, 62, 82, 132]
    coordsLvl2= [91, 47, 195, 132]
    coordsLvl3 = [203, 0, 323, 132]
    damage = 4
    speed = 3
    zone = 1
    range = 150
    damagetype = "earth"
    d_up=50
    d_up=50
    r_up=25
    damage_evo=[damage, damage+d_up, (damage+d_up)*1.25]
    range_evo=[range, range+r_up, range+r_up*2]
    price_evo=[50, 125, 250]
    price=price_evo[0]

    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        self.lv1=load(self.coordsLvl1, self.image)
        self.lv2=load(self.coordsLvl2, self.image)
        self.lv3=load(self.coordsLvl3, self.image)
        Tower.__init__(self, canvas, x, y,Caillou)
        # self.root.mainloop()
    def __str__(self):
        return "Mage de Terre"

class Archer(Tower):
    image="view/src/Archer.png"
    coordsLvl1 = [3,51,82,138]
    coordsLvl2 = [91,35,195,144]
    coordsLvl3 = [203,0,295,144]
    range=200
    damage = 4
    speed = 5
    zone = 1
    damagetype = "shot"
    d_up=50
    r_up=25
    damage_evo=[damage, damage+d_up, (damage+d_up)*1.25]
    range_evo=[range, range+r_up, range+r_up*2]
    speed_evo=[speed, speed+4, speed+8]
    price_evo=[50, 125, 250]
    price=price_evo[0]

    def __init__(self, canvas, x, y):
        #self.root=tk.Tk()
        #test_subimage(self.image, 3, 51, 82, 138, self.root)
        self.lv1=load(self.coordsLvl1, self.image)
        self.lv2=load(self.coordsLvl2, self.image)
        self.lv3=load(self.coordsLvl3, self.image)
        Tower.__init__(self, canvas, x, y,Fleche)
        
        #self.root.mainloop()
        
class Forgeron(Tower):
    
    coordsLvl1 = [0,0,120,115]
    coordsLvl2 = [125,0,250,115]
    coordsLvl3 = [250,0,380,115]
    image= 'view/src/Forgeron.png'
    price_evo=[200, 500, 750]
    price=price_evo[0]
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
        self.price=self.price_evo[1]
        self.canvas.delete(self.last_img)
        self.last_img = self.canvas.create_image(
                    self.x, self.y, image=self.lv2, anchor="s")
        self.canvas.tag_raise(self.last_img)
        self.canvas.after(1000000, self.construction, self)
        self.hero.transform(self)
    
    def upgrade2(self):
        self.lvl=3
        self.price=self.price_evo[2]
        self.canvas.delete(self.last_img)
        self.last_img = self.canvas.create_image(
                    self.x, self.y, image=self.lv3, anchor="s")
        self.canvas.tag_raise(self.last_img)
        self.canvas.after(1000000, self.construction, self)
        self.hero.transform(self)
    
    def __str__(self):
        return "Forgeron"

class Mine(Tower):
    coordsLvl1 = [0,0,140,135]
    coordsLvl2 = [150,0,300,135]
    image= 'view/src/Mine.png'
    price_evo=[200, 500, 750]
    production=30
    def __init__(self, canvas, x, y, parent):
        #self.root=tk.Tk()
        #test_subimage(self.image, 3, 51, 82, 138, self.root)
        self.lv1=load(self.coordsLvl1, self.image)
        self.lv2=load(self.coordsLvl2, self.image)
        Tower.__init__(self, canvas, x, y,0)
        self.parent=parent
    
    def produce(self): 
        self.parent.gold.set(self.parent.gold.get()+self.production)
        self.canvas.after(100, self.produce)
    
    def seek(self):
        pass

    def tir_p(self):
        pass

    def upgrade2(self):
        pass
    
    def upgrade1(self):
        pass 

    def upgrade(self):
        self.production=60
        self.canvas.delete(self.last_img)
        #On place la nouvelle
        self.last_img = self.canvas.create_image(
            self.x, self.y, image=self.lv2, anchor="s")
        #On la place au dessus
        self.canvas.tag_raise(self.last_img)



class Boulet(Projectile):
    def __init__(self,canvas, x, y, target, damage):
        self.x=x-5
        self.y=y-70
        self.target = target
        self.damage=damage
        Projectile.__init__(self,canvas, "view/src/bouletDeCanon.png", "view/src/bouletDeCanon.png")

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



    def __str__(self):
        return "Archer"

class Fleche(Projectile):
    def __init__(self, canvas, x,y, target, damage):
        self.x=x-5
        self.y=y-70
        self.target=target
        self.damage=damage
        
        self.canvas=canvas
        self.tx=self.target.x
        self.ty=self.target.y
        if self.tx<=self.x and self.ty<= self.y:
            self.img=tk.PhotoImage(file = "view/src/flèche gh.png")
        elif self.tx>=self.x and self.ty>=self.y:
            self.img=tk.PhotoImage(file= "view/src/flèche db.png")
        elif target.x>=self.x and self.ty<= self.y:
            self.img=tk.PhotoImage(file = "view/src/flèche dh.png")
        elif self.tx<=self.x and self.ty>=self.y:
            self.img=tk.PhotoImage(file ="view/src/flèche gb.png")
        self.boom=self.img
        self.v=1
        self.tir()



def distance(tower, ennemy):
    return ((ennemy.x-tower.x)**2+(ennemy.y-tower.y)**2)**0.5