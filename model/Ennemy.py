import tkinter as tk
from model.Character import Character

class Ennemy (Character):
    def __init__ (self, master, x, y) :
        #Stats
        self.x = x
        self.y = y
        self.team = "ennemy"
        self.name = ""
        self.state = "runRight"

        self.getSprite(self)

class Skeleton (Ennemy) :
    def __init__(self, master, x, y):
        self.hp = 10
        self.name = "Skeleton"
        self.speed = 15
        self.attackSpeed = 1

        # Spritesheet du Heros
        self.spritesheet = tk.PhotoImage(file="view/src/Skeleton.png")
        self.num_sprintes = {"idle" : 4, "runRight" : 8, "runLeft" : 8}
        self.canvas = master

        Ennemy.__init__(self, master, x, y)
