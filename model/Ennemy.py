import tkinter as tk
from model.Character import Character
loadedEnnemies = []

class Ennemy (Character):
    team = "ennemy"
    state = "idle"

    def showHp(self):
        print(self.hp)
        self.canvas.after(50, self.showHp)
        
    def __init__ (self, master, x, y) :
        global loadedEnnemies
        loadedEnnemies.append(self)
        Character.__init__(self,master,x,y)
        self.moveTo(1200,self.y)
        self.showHp()

class Skeleton (Ennemy) :
    hp = 10
    name = "Skeleton"
    attackSpeed = 1
    speed = 5

    spriteSize = 32
    y_Anim = {"idle" : 32, "runRight" : 32, "runLeft" : 0}
    num_sprintes = {"idle" : 1, "runRight" : 4, "runLeft" : 4}
    spritesheet = "view/src/Skeleton2.png"
    zoom = 2
