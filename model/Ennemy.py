import tkinter as tk
from model.Character import Character

class Ennemy (Character):
    team = "ennemy"
    state = "idle"

    def __init__ (self, master, x, y) :
        Character.__init__(self,master,x,y)
        self.moveTo(1200,self.y)

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
