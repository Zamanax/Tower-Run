from model.Ennemy import Ennemy
from model.Character import Character
import tkinter as tk

class Skeleton (Ennemy, Character):
    def __init__(self, master, x, y):
        self.x = x
        self.y = y
        self.team = "ennemy"
        self.hp = 0
        self.name = ""
        self.speed = 0
        self.attackSpeed = 2
        self.state = "runRight"

        self.getSprite(self)
        self.spritesheet = tk.PhotoImage(file= "view/src/Skeleton.png")
        self.num_sprintes  = {"runRight": 4, "attack": 3 }
