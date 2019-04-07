# import tkinter as tk
from model.Character import Character
import model.Heros as He
ennemies=[]

class Ennemy (Character):
    team = "ennemy"
    state = "idle"
        
    def __init__ (self, master, x, y, heros) :
        global ennemies
        Character.__init__(self,master,x,y)
        self.heros = heros
        ennemies.append(self)
        self.seek()
        self.moveTo(1200,self.y)

    def seek(self):
        if (((self.heros.x-self.x)**2)+((self.heros.y-self.y)**2))**0.5 < self.range:
            self.target = self.heros
            self.canvas.after_cancel(self.seeking)
            self.attack()
            return self.target
                
        self.seeking = self.canvas.after(50, self.seek)

class Skeleton (Ennemy) :
    __slot__=("__dict__","idle","runRight","runLeft")

    hp = 10
    name = "Skeleton"
    attackSpeed = 1
    speed = 2
    damage = 2

    spriteSize = 32
    y_Anim = {"idle" : 32, "runRight" : 32, "runLeft" : 0, "attackRight": 32, "attackLeft": 0, "die" : 64}
    num_sprintes = {"idle" : 1, "runRight" : 4, "runLeft" : 4, "attackRight" : 8, "attackLeft": 8, "die": 4}
    spritesheet = "view/src/Skeleton.png"
    zoom = 2
