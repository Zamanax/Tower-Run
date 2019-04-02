import tkinter as tk
from model.Character import Character


class Heros(Character):

    def __init__(self, master, x, y, max_y, min_y):
        
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
        self.max_y = max_y
        self.min_y = min_y

        self.getSprite(self)

    def mouseMove(self, event):

        if self.move :
            self.canvas.after_cancel(self.move)
            
            if event.y > self.max_y:
                self.moveTo(event.x, self.max_y)
            elif event.y < self.min_y:
                self.moveTo(event.x, self.min_y)
            else:
                self.moveTo(event.x,event.y)
        else :
            if event.y > self.max_y:
                self.moveTo(event.x, self.max_y)
            elif event.y < self.min_y:
                self.moveTo(event.x, self.min_y)
            else:
                self.moveTo(event.x,event.y)