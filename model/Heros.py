import tkinter as tk
from model.Character import Character
import model.Ennemy as Enn
class Heros(Character):
    # Stats du Héros
    team = "ally"
    hp = 30
    damage = 5
    speed = 15
    attackSpeed = 2
    state = "idle"
    range = 50

    def __init__(self, canvas, x, y, max_y, min_y):
        Character.__init__(self, canvas, x, y)
        self.max_y = max_y
        self.min_y = min_y
        self.seek()

    def mouseMove(self, event):

        if self.move:
            self.state = "idle"
            self.canvas.after_cancel(self.move)

            if event.y > self.max_y:
                self.moveTo(event.x, self.max_y)
            elif event.y < self.min_y:
                self.moveTo(event.x, self.min_y)
            else:
                self.moveTo(event.x, event.y)
        else:
            self.sprite = 0
            if event.y > self.max_y:
                self.moveTo(event.x, self.max_y)
            elif event.y < self.min_y:
                self.moveTo(event.x, self.min_y)
            else:
                self.moveTo(event.x, event.y)

    def seek(self):
        for ennemy in Enn.loadedEnnemies:
            if (((ennemy.x-self.x)**2)+((ennemy.y-self.y)**2))**0.5 < self.range:
                self.target = ennemy
                self.attack()
                if self.target.hp <= 0:
                    self.target.die()
        self.canvas.after(50, self.seek)



class Adventurer(Heros):
    # Stats du Héros
    name = "Aventurier"

    # Spritesheet du Heros
    num_sprintes = {"idle": 13, "runRight": 8,
                    "runLeft": 8, "attackRight": 10, "attackLeft": 10}
    spritesheet = "view/src/Adventurer.png"
    spriteSize = 32
    zoom = 2
    y_Anim = {"idle": 0, "runRight": 32, "runLeft": 288,
              "attackRight": 64, "attackLeft": 324}

    def __init__(self, canvas, x, y, max_y, min_y):
        Heros.__init__(self, canvas, x, y, max_y, min_y)
        self.max_y -= 5
        self.min_y -= 5


class Ichigo(Heros):
    # Stats du Héros
    name = "Ichigo"

    # Spritesheet du Heros
    num_sprintes = {"idle": 2, "runRight": 8,
                    "runLeft": 8, "attackRight": 16, "attackLeft": 16, "Transform" : 3}
    spritesheet = "view/src/Ichigo1.png"
    spriteSize = 200
    y_Anim = {"idle": 0, "runRight": 400, "runLeft": 600,
              "attackRight": 800, "attackLeft": 1000, "Transform": 1200}
