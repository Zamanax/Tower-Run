# import tkinter as tk
from model.Character import Character
import model.Heros as He
from functools import lru_cache

ennemies=[]

class Ennemy (Character):
    team = "ennemy"
    state = "idle"
 
    def __init__ (self, master, x, y, heros) :
        global ennemies
        Character.__init__(self,master,x,y)
        self.heros = heros
        ennemies.append(self)
        self.index = len(ennemies)-1
        self.seek()
        self.moveTo(1200,self.y)

    @lru_cache(128)
    def seek(self):
        if self.target:
            self.attack()
        elif (((self.heros.x-self.x)**2)+((self.heros.y-self.y)**2))**0.5 < self.range:
            self.target = self.heros
            self.canvas.after_cancel(self.seeking)
            self.attack()
            return self.target
                
        self.seeking = self.canvas.after(100, self.seek)

    # def die(self, delete):
    #     global ennemies
    #     super().die(delete)
    #     ennemies.pop(self.index)


class Skeleton (Ennemy) :
    __slot__=("__dict__","idle","runRight","runLeft")

    hp = 10
    name = "Skeleton"
    attackSpeed = 1
    speed = 2
    damage = 1

    spriteSize = 32
    y_Anim = {"idle" : 32, "runRight" : 32, "runLeft" : 0, "attackRight": 32, "attackLeft": 0, "die" : 64}
    damagingSprite = [4,6,7,8]
    num_sprintes = {"idle" : 1, "runRight" : 4, "runLeft" : 4, "attackRight" : 8, "attackLeft": 8, "die": 4}
    spritesheet = "view/src/Skeleton.png"
    zoom = 2
