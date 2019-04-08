import tkinter as tk
from model.Character import Character
from model.Ennemy import ennemies

class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Heros(Character, metaclass=Singleton):
    # Stats du Héros
    team = "ally"
    state = "idle"
    lv1 = {}

    def showHp(self):
        print(self.hp)
        self.canvas.after(50, self.showHp)

    def __init__(self, canvas, x, y, max_y, min_y):
        Character.__init__(self, canvas, x, y)
        self.spritesheet1 = tk.PhotoImage(file=self.lv1["spritesheet"])
        self.max_y = max_y
        self.min_y = min_y
        self.seek()
        # self.showHp()
    
    def getSprite(self):
        super().getSprite()
        if hasattr(self, 'lv1') and self.lv1 != []:
            self.spritesheet = tk.PhotoImage(file=self.lv1["spritesheet"])
            self.idle1 = [self.subimage(self.lv1["spriteSize"]*i, self.lv1["y_Anim"]["idle"], self.lv1["spriteSize"]*(i+1), self.lv1["y_Anim"]["idle"]+self.lv1["spriteSize"]).zoom(self.zoom)
                        for i in range(self.lv1["num_sprintes"]["idle"])]

            self.runRight1 = [self.subimage(self.lv1["spriteSize"]*i, self.lv1["y_Anim"]["runRight"], self.lv1["spriteSize"]*(i+1), self.lv1["y_Anim"]["runRight"]+self.lv1["spriteSize"]).zoom(self.zoom)
                            for i in range(self.lv1["num_sprintes"]["runRight"])]

            self.runLeft1 = [self.subimage(self.lv1["spriteSize"]*i, self.lv1["y_Anim"]["runLeft"], self.lv1["spriteSize"]*(i+1), self.lv1["y_Anim"]["runLeft"]+self.lv1["spriteSize"]).zoom(self.zoom)
                            for i in range(self.lv1["num_sprintes"]["runLeft"])]
            self.runLeft1.reverse()

            self.attackRight1 = [self.subimage(self.lv1["spriteSize"]*i, self.lv1["y_Anim"]["attackRight"], self.lv1["spriteSize"]*(i+1), self.lv1["y_Anim"]["attackRight"]+self.lv1["spriteSize"]).zoom(self.zoom)
                            for i in range(self.lv1["num_sprintes"]["attackRight"])]

            self.attackLeft1 = [self.subimage(self.lv1["spriteSize"]*i, self.lv1["y_Anim"]["attackLeft"], self.lv1["spriteSize"]*(i+1), self.lv1["y_Anim"]["attackLeft"]+self.lv1["spriteSize"]).zoom(self.zoom)
                            for i in range(self.lv1["num_sprintes"]["attackLeft"])]
            self.attackLeft1.reverse()

            self.death1 = [self.subimage(self.lv1["spriteSize"]*i, self.lv1["y_Anim"]["die"], self.lv1["spriteSize"]*(i+1), self.lv1["y_Anim"]["die"]+self.lv1["spriteSize"]).zoom(self.zoom)
                            for i in range(self.lv1["num_sprintes"]["die"])]

    def seek(self):
        if self.target:
            self.attack()
        else:
            for ennemy in ennemies:
                if (((ennemy.x-self.x)**2)+((ennemy.y-self.y)**2))**0.5 < self.range and ennemy.state != "die":
                    self.target = ennemy
                    self.canvas.after_cancel(self.seeking)
                    if self.move:
                        self.canvas.after_cancel(self.move)
                    self.sprite = 0
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
 
    def transformTo1(self, event):
        self.hp = self.lv1["hp"]
        self.damage = self.lv1["damage"]
        self.damagingSprite = self.lv1["damagingSprite"]
        self.speed = self.lv1["speed"]
        self.attackSpeed = self.lv1["attackSpeed"]
        self.num_sprintes = self.lv1["num_sprintes"]
        self.spritesheet = self.lv1["spritesheet"]
        self.spriteSize = self.lv1["spriteSize"]
        self.y_Anim = self.lv1["y_Anim"]
        self.idle = self.idle1
        self.runRight = self.runRight1
        self.runLeft = self.runLeft1
        self.attackLeft = self.attackLeft1
        self.attackRight = self.attackRight1
        self.death = self.death1

class Adventurer(Heros):
    # Stats du Héros
    name = "Aventurier"
    hp = 100
    damage = 4
    speed = 8
    attackSpeed = 1

    # Spritesheet du Heros
    num_sprintes = {"idle": 13, "runRight": 8,
                    "runLeft": 8, "attackRight": 10, "attackLeft": 10, "die": 7}
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
    attackSpeed = 1

    # Spritesheet du Heros
    num_sprintes = {"idle": 2, "runRight": 8,
                    "runLeft": 8, "attackRight": 16, "attackLeft": 16, "die": 2, "Transform": 3}
    spritesheet = "view/src/Ichigo1.png"
    spriteSize = 200
    y_Anim = {"idle": 0, "runRight": 400, "runLeft": 600,
              "attackRight": 800, "attackLeft": 1000, "die": 0, "Transform": 1200}


class Goku(Heros):
    name = "Son Goku"
    
    def __init__(self, canvas, x, y, max_y, min_y):
        self.hp = self.lv0["hp"]
        self.damage = self.lv0["damage"]
        self.damagingSprite = self.lv0["damagingSprite"]
        self.speed = self.lv0["speed"]
        self.attackSpeed = self.lv0["attackSpeed"]
        self.num_sprintes = self.lv0["num_sprintes"]
        self.spritesheet = self.lv0["spritesheet"]
        self.spriteSize = self.lv0["spriteSize"]
        self.y_Anim = self.lv0["y_Anim"]
        Heros.__init__(self, canvas, x, y, max_y, min_y)        

    lv0 = {
        "hp": 50,
        "damage": 2,
        "damagingSprite": [5, 10, 11, 12, 13, 18, 22, 23],
        "speed": 8,
        "attackSpeed": 3,
        "num_sprintes": {"idle": 8, "runRight": 4,
                         "runLeft": 4, "attackRight": 15, "attackLeft": 15, "die": 8, "Transform": 8},
        "spritesheet": "view/src/Goku0.png",
        "spriteSize": 200,
        "y_Anim": {"idle": 200, "runRight": 400, "runLeft": 600,
                   "attackRight": 1200, "attackLeft": 1400, "die": 200, "Transform": 2200}
    }

    lv1 = {
        "hp": 50,
        "damage": 4,
        "damagingSprite" : [2,3,4,5,6,7,12,13,14,15],
        "speed": 12,
        "attackSpeed": 3,
        "num_sprintes": {"idle": 4, "runRight": 4,
                         "runLeft": 4, "attackRight": 15, "attackLeft": 15, "die": 4, "Transform": 8},
        "spritesheet": "view/src/Goku1.png",
        "spriteSize": 200,
        "y_Anim": {"idle": 200, "runRight": 400, "runLeft": 600,
                   "attackRight": 1200, "attackLeft": 1400, "die": 200, "Transform": 2200}
    }

    lv2 = {
        "hp": 50,
        "damage": 4,
        "speed": 16,
        "attackSpeed": 5,
        "num_sprintes": {"idle": 4, "runRight": 4,
                         "runLeft": 4, "attackRight": 26, "attackLeft": 26, "die": 4, "Transform": 8},
        "spritesheet": "view/src/Goku2.png",
        "spriteSize": 200,
        "y_Anim": {"idle": 200, "runRight": 400, "runLeft": 600,
                   "attackRight": 1200, "attackLeft": 1400, "die": 200, "Transform": 2200}
    }

    lv3 = {
        "hp": 50,
        "damage": 4,
        "speed": 25,
        "attackSpeed": 5,
        "damagingSprite": [3, 7, 10, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24],
        "num_sprintes": {"idle": 4, "runRight": 4,
                         "runLeft": 4, "attackRight": 24, "attackLeft": 24, "die": 4},
        "spritesheet": "view/src/Goku3.png",
        "spriteSize": 200,
        "y_Anim": {"idle": 200, "runRight": 400, "runLeft": 600,
                   "attackRight": 800, "attackLeft": 1000, "die": 200}
    }

# class Goku(Heros):
#     name = "Son Goku"
#     lvl = 0
#     hp = 50
#     damage = 2
#     damagingSprite = [5,10,11,12,13,18,22,23]
#     speed = 8
#     attackSpeed = 3
#     num_sprintes = {"idle": 8, "runRight": 4,
#                     "runLeft": 4, "attackRight": 15, "attackLeft": 15, "die" : 8,"Transform" : 8}
#     spritesheet = "view/src/Goku0.png"
#     spriteSize = 200
#     y_Anim = {"idle": 200, "runRight": 400, "runLeft": 600,
#               "attackRight": 1200, "attackLeft": 1400, "die" : 200,"Transform": 2200}

# class Goku(Heros):
#     name = "Son Goku"

#     lvl = 1
    # hp = 50
    # damage = 4
    # speed = 12
    # attackSpeed = 1
    # num_sprintes = {"idle": 4, "runRight": 4,
    #                 "runLeft": 4, "attackRight": 15, "attackLeft": 15, "die" : 4,"Transform" : 8}
    # spritesheet = "view/src/Goku1.png"
    # spriteSize = 200
    # y_Anim = {"idle": 200, "runRight": 400, "runLeft": 600,
    #           "attackRight": 1200, "attackLeft": 1400, "die" : 200,"Transform": 2200}

# class Goku(Heros):
#     name = "Son Goku"

#     lvl = 2
    # hp = 50
    # damage = 4
    # speed = 16
    # attackSpeed = 5
    # num_sprintes = {"idle": 4, "runRight": 4,
    #                 "runLeft": 4, "attackRight": 26, "attackLeft": 26, "die" : 4,"Transform" : 8}
    # spritesheet = "view/src/Goku2.png"
    # spriteSize = 200
    # y_Anim = {"idle": 200, "runRight": 400, "runLeft": 600,
    #           "attackRight": 1200, "attackLeft": 1400, "die" : 200,"Transform": 2200}

# class Goku(Heros):
#     name = "Son Goku"

#     lvl = 3
    # hp = 50
    # damage = 4
    # speed = 25
    # attackSpeed = 5
    # damagingSprite = [3,7,10,12,13,14,16,17,18,19,20,21,22,23,24]
    # num_sprintes = {"idle": 4, "runRight": 4,
    #                 "runLeft": 4, "attackRight": 24, "attackLeft": 24, "die" : 4}
    # spritesheet = "view/src/Goku3.png"
    # spriteSize = 200
    # y_Anim = {"idle": 200, "runRight": 400, "runLeft": 600,
    #           "attackRight": 800, "attackLeft": 1000, "die" : 200}
