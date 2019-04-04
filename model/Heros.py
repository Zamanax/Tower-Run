import tkinter as tk
from model.Character import Character


class Heros(Character):
    # Stats du Héros
    team = "ally"
    hp = 30
    name = "Heros"
    speed = 15
    attackSpeed = 2
    state = "idle"

    # Spritesheet du Heros
    num_sprintes = {"idle" : 13, "runRight" : 8, "runLeft" : 8}
    spriteSize = 32
    y_Anim = {"idle" : 0, "runRight" : 32, "runLeft" : 288}

    def __init__(self, master, x, y, max_y, min_y):
        
        # Stats du Heros
        self.x = x
        self.y = y

        # Spritesheet du Heros
        self.spritesheet = tk.PhotoImage(file="view/src/Adventurer.png")
        
        self.canvas = master
        self.max_y = max_y
        self.min_y = min_y

        self.getSprite(self)

    def mouseMove(self, event):

        if self.move :
            self.state = "idle"
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