# import tkinter as tk
from model.Character import Character
import model.Heros as He

ennemies=[]

class Ennemy (Character):
    purse = 0
    team = "ennemy"
    state = "idle"
 
    def __init__ (self, parent, x, y, heros) :
        global ennemies
        ennemies.insert(0,self)
        self.heros = heros
        Character.__init__(self,parent,x,y)
        # self.index = len(ennemies)-1
        self.goToObjective()

    # def seek(self):
    #     if self.target:
    #         self.attack()
    #     elif (((self.heros.x-self.x)**2)+((self.heros.y-self.y)**2))**0.5 < self.range:
    #         self.target = self.heros
    #         self.canvas.after_cancel(self.seeking)
    #         self.attack()
    #         return self.target
                
    #     self.seeking = self.canvas.after(100, self.seek)

    def goToObjective(self):
        if self.move == None:
            self.moveTo(1200,self.y)


class Skeleton (Ennemy) :
    __slots__ = ("idle", "runRight", "runLeft", "attackRight", "attackLeft", "death")
    hp = 10
    name = "Skeleton"
    attackSpeed = 1
    speed = 1
    damage = 2
    purse = 10

    barOffsetx = -20

    spriteSize = 32
    y_Anim = {"idle" : 32, "runRight" : 32, "runLeft" : 0, "attackRight": 32, "attackLeft": 0, "die" : 64}
    damagingSprite = [4,6,7,8]
    num_sprintes = {"idle" : 1, "runRight" : 4, "runLeft" : 4, "attackRight" : 8, "attackLeft": 8, "die": 4}
    spritesheet = "view/src/Skeleton.png"
    zoom = 2

class miniSkeleton (Skeleton) :
    hp = 5
    attackSpeed = 2
    speed = 2
    damage = 1
    zoom = 1

class Totor (Ennemy):
    __slots__ = ("idle", "runRight",
                "runLeft", "attackRight", "attackLeft")

    hp = 200
    name = "Totor"
    attackSpeed = 0.5
    speed = 1
    damage = 10
    
    spritesheet = 'view/src/Totor.png'
    spriteSize = 96
    y_Anim = {"idle" : 0, "runRight" : 96, "runLeft" : 96*12, "attackRight": 96*3, "attackLeft": 96*13, "die" : 96*10}
    damagingSprite = [1,2,3]
    num_sprintes = {"idle" : 5, "runRight" : 8, "runLeft" : 8, "attackRight" : 9, "attackLeft": 9, "die": 6}
    zoom = 2

class Fat_Totor (Totor) :
    hp = 1000
    name = "Fat_Totor"
    damage = 20
    speed = 0.5
    zoom = 3

class Dwarf (Ennemy) :
    __slots__ = ('idle', 'runRight', 'runLeft', 'attackRight', 'attackLeft')

    hp = 50
    name = 'Dwarf'
    attackSpeed = 1
    speed = 1
    damage = 5

    spritesheet = 'view/src/Dwarf.png'
    spriteSize = 96 
    num_sprintes = {'idle' : 5, 'runRight' : 8, 'runLeft' : 8, 'attackRight' : 9, 'attackLeft' : 9, 'die' : 6}
    zoom = 1
    