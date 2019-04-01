import tkinter as tk
from model.Character import Character


class Heros(Character):

    def __init__(self, master, x, y):
        
        # Stats du Heros
        self.x = x
        self.y = y
        self.team = "ally"
        self.hp = 30
        self.name = "Heros"
        self.speed = 15
        self.attackSpeed = 2
        self.state = "idle"

        # Spritesheet du Heros
        self.spritesheet = tk.PhotoImage(file="view/src/Adventurer.png")
        self.num_sprintes = 13
        self.canvas = master

        self.getSprite(self)

    def mouseMove(self, event):
        self.moveTo(event.x, event.y)
