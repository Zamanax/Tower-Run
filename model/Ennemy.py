import tkinter as tk
from model.Character import Character

class Ennemy (Character):
    team = "ennemy"
    state = "idle"
    def __init__ (self, master, x, y) :
        #Stats
        self.x = x
        self.y = y
        self.canvas = master

        self.getSprite(self)

class Skeleton (Ennemy) :
    hp = 10
    name = "Skeleton"
    speed = 5
    attackSpeed = 1
    spriteSize = 32
    y_Anim = {"idle" : 32, "runRight" : 32, "runLeft" : 0}

    def __init__(self, master, x, y):
    
        # Spritesheet du Heros
        self.spritesheet = tk.PhotoImage(file="view/src/Skeleton2.png")
        self.num_sprintes = {"idle" : 1, "runRight" : 4, "runLeft" : 4}

        Ennemy.__init__(self, master, x, y)
        self.moveTo(1200,self.y)