import tkinter as tk
from model.Character import Character
import model.Heros as He

ennemies=[]

class Ennemy (Character):
    team = "ennemy"
    state = "idle"
    number=0
        
    def __init__ (self, master, x, y) :
        global ennemies
        Character.__init__(self,master,x,y)
        ennemies.append(self)
        self.seek()
        self.moveTo(1200,self.y)

    def seek(self):

        if (((He.Heros.x-self.x)**2)+((He.Heros.y-self.y)**2))**0.5 < self.range:
            self.target = He.Heros
            self.canvas.after_cancel(self.seeking)
            self.attack()
            return self.target
                
        self.seeking = self.canvas.after(50, self.seek)

    def __str__(self):
        return "Ennemy_"+str(Ennemy.number)

class Skeleton (Ennemy) :
    __slot__=("__dict__","idle","runRight","runLeft")

    hp = 10
    name = "Skeleton"
    attackSpeed = 1
    speed = 2

    spriteSize = 32
    y_Anim = {"idle" : 32, "runRight" : 32, "runLeft" : 0}
    num_sprintes = {"idle" : 1, "runRight" : 4, "runLeft" : 4}
    spritesheet = "view/src/Skeleton2.png"
    zoom = 2
