import tkinter as tk
from model.Character import Character

class Heros(Character):
    # Stats du Héros
    team = "ally"
    hp = 30
    speed = 15
    attackSpeed = 2
    state = "idle"

    def __init__(self, canvas, x, y, max_y, min_y):
        Character.__init__(self,canvas,x,y)
        self.max_y = max_y
        self.min_y = min_y

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
            self.sprite = 0
            if event.y > self.max_y:
                self.moveTo(event.x, self.max_y)
            elif event.y < self.min_y:
                self.moveTo(event.x, self.min_y)
            else:
                self.moveTo(event.x,event.y)

class Adventurer(Heros):
    # Stats du Héros
    name = "Aventurier"

    # Spritesheet du Heros
    num_sprintes = {"idle" : 13, "runRight" : 8, "runLeft" : 8}
    spritesheet = "view/src/Adventurer.png"
    spriteSize = 32
    zoom = 2
    y_Anim = {"idle" : 0, "runRight" : 32, "runLeft" : 288}

class Ichigo(Heros) :
    # Stats du Héros
    name = "Ichigo"

    # Spritesheet du Heros
    num_sprintes = {"idle" : 4, "runRight" : 8, "runLeft" : 8}
    spritesheet = "view/src/Ichigo.png"
    spriteSize = 200
    y_Anim = {"idle" : 0, "runRight" : 400, "runLeft" : 600}
    