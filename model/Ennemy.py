import tkinter as tk
from model.Character import Character

class Ennemy (Character, Skeleton):
    def __init__ (self, master, x, y) :
        #Stats
        self.x = x
        self.y = y
        self.team = "ennemy"
        self.hp = 0
        self.name = ""
        self.speed = 0
        self.attackSpeed = 2
        self.state = "runRight"

        self.getSprite(self)
