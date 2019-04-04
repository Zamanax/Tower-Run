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
    speed = 15
    attackSpeed = 1
    spriteSize = 64
    y_Anim = {"idle" : 64, "runRight" : 64, "runLeft" : 0}

    def __init__(self, master, x, y):
    
        # Spritesheet du Heros
        self.spritesheet = tk.PhotoImage(file="view/src/Skeleton.png")
        self.num_sprintes = {"idle" : 4, "runRight" : 8, "runLeft" : 8}

        Ennemy.__init__(self, master, x, y)
