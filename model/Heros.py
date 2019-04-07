import tkinter as tk
from model.Character import Character
from model.Ennemy import ennemies

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Heros(Character, metaclass=Singleton):
    # Stats du Héros
    team = "ally"
    state = "idle"

    def showHp(self):
        print(self.hp)
        self.canvas.after(50, self.showHp)

    def __init__(self, canvas, x, y, max_y, min_y):
        Character.__init__(self, canvas, x, y)
        self.max_y = max_y
        self.min_y = min_y
        self.seek()
        # self.showHp()

    
    def seek(self):
        if self.target:
            self.attack()
        else:
            for ennemy in ennemies:
                if (((ennemy.x-self.x)**2)+((ennemy.y-self.y)**2))**0.5 < self.range:
                    self.target = ennemy
                    self.canvas.after_cancel(self.seeking)
                    self.attack()
                    return self.target
                
        self.seeking = self.canvas.after(50, self.seek)

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
                

class Adventurer(Heros):
    # Stats du Héros
    name = "Aventurier"
    hp = 100
    damage = 2
    speed = 8
    attackSpeed = 2

    # Spritesheet du Heros
    num_sprintes = {"idle": 13, "runRight": 8,
                    "runLeft": 8, "attackRight": 10, "attackLeft": 10, "die":7}
    spritesheet = "view/src/Adventurer.png"
    spriteSize = 32
    zoom = 2
    y_Anim = {"idle": 0, "runRight": 32, "runLeft": 288,
              "attackRight": 64, "attackLeft": 324, "die": 256}

    def __init__(self, canvas, x, y, max_y, min_y):
        Heros.__init__(self, canvas, x, y, max_y, min_y)
        self.max_y -= 5
        self.min_y -= 5


class Ichigo(Heros):
    # Stats du Héros
    name = "Ichigo"

    hp = 50
    damage = 2
    speed = 8
    attackSpeed = 2

    # Spritesheet du Heros
    num_sprintes = {"idle": 2, "runRight": 8,
                    "runLeft": 8, "attackRight": 16, "attackLeft": 16, "die" : 2,"Transform" : 3}
    spritesheet = "view/src/Ichigo1.png"
    spriteSize = 200
    y_Anim = {"idle": 0, "runRight": 400, "runLeft": 600,
              "attackRight": 800, "attackLeft": 1000, "die" : 0,"Transform": 1200}
