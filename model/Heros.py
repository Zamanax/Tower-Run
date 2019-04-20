import tkinter as tk
from model.Character import Character
from model.Ennemy import ennemies
from functools import lru_cache


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
    lvl = 0
    lv0 = {}
    lv1 = {}
    lv2 = {}
    lv3 = {}

    def __init__(self, canvas, x, y, max_y, min_y):
        Character.__init__(self, canvas, x, y)
        if "spritesheet" in self.lv0:
            self.spritesheet1 = tk.PhotoImage(file=self.lv1["spritesheet"])
        self.max_y = max_y
        self.min_y = min_y
        self.seek()

    @lru_cache(512)
    def getSprite(self):
        super().getSprite()

        if "num_sprintes" in self.lv0:
            self.transformAnim = [self.subimage(self.lv0["spriteSize"]*i, self.lv0["y_Anim"]["transform"], self.lv0["spriteSize"]*(i+1), self.lv0["y_Anim"]["transform"]+self.lv0["spriteSize"]).zoom(self.zoom)
                                  for i in range(self.lv0["num_sprintes"]["transform"])]
            self.transformAnim.reverse()

        if hasattr(self, 'lv1') and self.lv1 != {}:
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

            self.transformAnim1 = [self.subimage(self.lv1["spriteSize"]*i, self.lv1["y_Anim"]["transform"], self.lv1["spriteSize"]*(i+1), self.lv1["y_Anim"]["transform"]+self.lv1["spriteSize"]).zoom(self.zoom)
                                   for i in range(self.lv1["num_sprintes"]["transform"])]
            self.transformAnim1.reverse()

            self.death1 = [self.subimage(self.lv1["spriteSize"]*i, self.lv1["y_Anim"]["die"], self.lv1["spriteSize"]*(i+1), self.lv1["y_Anim"]["die"]+self.lv1["spriteSize"]).zoom(self.zoom)
                           for i in range(self.lv1["num_sprintes"]["die"])]

        if hasattr(self, 'lv2') and self.lv2 != {}:
            self.spritesheet = tk.PhotoImage(file=self.lv2["spritesheet"])
            self.idle2 = [self.subimage(self.lv2["spriteSize"]*i, self.lv2["y_Anim"]["idle"], self.lv2["spriteSize"]*(i+1), self.lv2["y_Anim"]["idle"]+self.lv2["spriteSize"]).zoom(self.zoom)
                          for i in range(self.lv2["num_sprintes"]["idle"])]

            self.runRight2 = [self.subimage(self.lv2["spriteSize"]*i, self.lv2["y_Anim"]["runRight"], self.lv2["spriteSize"]*(i+1), self.lv2["y_Anim"]["runRight"]+self.lv2["spriteSize"]).zoom(self.zoom)
                              for i in range(self.lv2["num_sprintes"]["runRight"])]

            self.runLeft2 = [self.subimage(self.lv2["spriteSize"]*i, self.lv2["y_Anim"]["runLeft"], self.lv2["spriteSize"]*(i+1), self.lv2["y_Anim"]["runLeft"]+self.lv2["spriteSize"]).zoom(self.zoom)
                             for i in range(self.lv2["num_sprintes"]["runLeft"])]
            self.runLeft2.reverse()

            self.attackRight2 = [self.subimage(self.lv2["spriteSize"]*i, self.lv2["y_Anim"]["attackRight"], self.lv2["spriteSize"]*(i+1), self.lv2["y_Anim"]["attackRight"]+self.lv2["spriteSize"]).zoom(self.zoom)
                                 for i in range(self.lv2["num_sprintes"]["attackRight"])]

            self.attackLeft2 = [self.subimage(self.lv2["spriteSize"]*i, self.lv2["y_Anim"]["attackLeft"], self.lv2["spriteSize"]*(i+1), self.lv2["y_Anim"]["attackLeft"]+self.lv2["spriteSize"]).zoom(self.zoom)
                                for i in range(self.lv2["num_sprintes"]["attackLeft"])]
            self.attackLeft2.reverse()

            self.transformAnim2 = [self.subimage(self.lv2["spriteSize"]*i, self.lv2["y_Anim"]["transform"], self.lv2["spriteSize"]*(i+1), self.lv2["y_Anim"]["transform"]+self.lv2["spriteSize"]).zoom(self.zoom)
                                   for i in range(self.lv2["num_sprintes"]["transform"])]
            self.transformAnim2.reverse()

            self.death2 = [self.subimage(self.lv2["spriteSize"]*i, self.lv2["y_Anim"]["die"], self.lv2["spriteSize"]*(i+1), self.lv2["y_Anim"]["die"]+self.lv2["spriteSize"]).zoom(self.zoom)
                           for i in range(self.lv2["num_sprintes"]["die"])]

        if hasattr(self, 'lv3') and self.lv3 != {}:
            self.spritesheet = tk.PhotoImage(file=self.lv3["spritesheet"])
            self.idle3 = [self.subimage(self.lv3["spriteSize"]*i, self.lv3["y_Anim"]["idle"], self.lv3["spriteSize"]*(i+1), self.lv3["y_Anim"]["idle"]+self.lv3["spriteSize"]).zoom(self.zoom)
                          for i in range(self.lv3["num_sprintes"]["idle"])]

            self.runRight3 = [self.subimage(self.lv3["spriteSize"]*i, self.lv3["y_Anim"]["runRight"], self.lv3["spriteSize"]*(i+1), self.lv3["y_Anim"]["runRight"]+self.lv3["spriteSize"]).zoom(self.zoom)
                              for i in range(self.lv3["num_sprintes"]["runRight"])]

            self.runLeft3 = [self.subimage(self.lv3["spriteSize"]*i, self.lv3["y_Anim"]["runLeft"], self.lv3["spriteSize"]*(i+1), self.lv3["y_Anim"]["runLeft"]+self.lv3["spriteSize"]).zoom(self.zoom)
                             for i in range(self.lv3["num_sprintes"]["runLeft"])]
            self.runLeft3.reverse()

            self.attackRight3 = [self.subimage(self.lv3["spriteSize"]*i, self.lv3["y_Anim"]["attackRight"], self.lv3["spriteSize"]*(i+1), self.lv3["y_Anim"]["attackRight"]+self.lv3["spriteSize"]).zoom(self.zoom)
                                 for i in range(self.lv3["num_sprintes"]["attackRight"])]

            self.attackLeft3 = [self.subimage(self.lv3["spriteSize"]*i, self.lv3["y_Anim"]["attackLeft"], self.lv3["spriteSize"]*(i+1), self.lv3["y_Anim"]["attackLeft"]+self.lv3["spriteSize"]).zoom(self.zoom)
                                for i in range(self.lv3["num_sprintes"]["attackLeft"])]
            self.attackLeft3.reverse()

            self.death3 = [self.subimage(self.lv3["spriteSize"]*i, self.lv3["y_Anim"]["die"], self.lv3["spriteSize"]*(i+1), self.lv3["y_Anim"]["die"]+self.lv3["spriteSize"]).zoom(self.zoom)
                           for i in range(self.lv3["num_sprintes"]["die"])]

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
            # if self.hp < self.baseHp:
            #     self.hp += 1
        self.seeking = self.canvas.after(50, self.seek)

    def mouseMove(self, event):
        if self.state == "transform":
            return
        if self.move:
            self.state = "idle"
            self.canvas.after_cancel(self.move)

            if event.y > self.max_y:
                self.moveTo(event.x, self.max_y)
            elif event.y < self.min_y:
                self.moveTo(event.x, self.min_y)
            else:
                self.moveTo(event.x, event.y)

        elif self.attacking:
            self.state = "idle"
            self.canvas.after_cancel(self.attack)

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

    def transform(self):
        self.sprite = 0
        if self.lvl == 0:
            self.sprite = 0
            self.state = "transform"

            self.lvl = 1
            self.hp = self.lv1["hp"]
            self.baseHp = self.hp
            self.damage = self.lv1["damage"]
            self.damagingSprite = self.lv1["damagingSprite"]
            self.speed = self.lv1["speed"]
            self.attackSpeed = self.lv1["attackSpeed"]
            # self.num_sprintes = self.lv1["num_sprintes"]
            self.spritesheet = self.lv1["spritesheet"]
            self.spriteSize = self.lv1["spriteSize"]
            self.y_Anim = self.lv1["y_Anim"]
            self.idle = self.idle1
            self.runRight = self.runRight1
            self.runLeft = self.runLeft1
            self.attackLeft = self.attackLeft1
            self.attackRight = self.attackRight1
            # self.transformAnim = self.transformAnim1
            self.death = self.death1

        elif self.lvl == 1:
            self.lvl = 2
            self.sprite = 0
            self.state = "transform"

            self.hp = self.lv2["hp"]
            self.baseHp = self.hp
            self.damage = self.lv2["damage"]
            self.damagingSprite = self.lv2["damagingSprite"]
            self.speed = self.lv2["speed"]
            self.attackSpeed = self.lv2["attackSpeed"]
            # self.num_sprintes = self.lv2["num_sprintes"]
            self.spritesheet = self.lv2["spritesheet"]
            self.spriteSize = self.lv2["spriteSize"]
            self.y_Anim = self.lv2["y_Anim"]
            self.idle = self.idle2
            self.runRight = self.runRight2
            self.runLeft = self.runLeft2
            self.attackLeft = self.attackLeft2
            self.attackRight = self.attackRight2
            # self.transformAnim = self.transformAnim2
            self.death = self.death2

        elif self.lvl == 2:
            self.lvl = 3
            self.sprite = 0
            self.state = "transform"

            self.hp = self.lv3["hp"]
            self.baseHp = self.hp
            self.damage = self.lv3["damage"]
            self.damagingSprite = self.lv3["damagingSprite"]
            self.speed = self.lv3["speed"]
            self.attackSpeed = self.lv3["attackSpeed"]
            # self.num_sprintes = self.lv3["num_sprintes"]
            self.spritesheet = self.lv3["spritesheet"]
            self.spriteSize = self.lv3["spriteSize"]
            self.y_Anim = self.lv3["y_Anim"]
            # self.changeStats(self.lv3)
            self.idle = self.idle3
            self.runRight = self.runRight3
            self.runLeft = self.runLeft3
            self.attackLeft = self.attackLeft3
            self.attackRight = self.attackRight3
            self.death = self.death3

    def changeStats(self, dict):
        self.hp = dict["hp"]
        self.damage = dict["damage"]
        self.damagingSprite = dict["damagingSprite"]
        self.speed = dict["speed"]
        self.attackSpeed = dict["attackSpeed"]
        self.num_sprintes = dict["num_sprintes"]
        self.spritesheet = dict["spritesheet"]
        self.spriteSize = dict["spriteSize"]
        self.y_Anim = dict["y_Anim"]

    def incrementSprite(self):
        if "transform" in self.num_sprintes:
            if self.sprite == self.num_sprintes["transform"] - 1 and self.state == "transform":
                self.state = "idle"
                if self.lvl == 1:
                    self.transformAnim = self.transformAnim1
                    self.num_sprintes = self.lv1["num_sprintes"]

                elif self.lvl == 2:
                    self.transformAnim = self.transformAnim2
                    self.num_sprintes = self.lv2["num_sprintes"]

                elif self.lvl == 3:
                    self.num_sprintes = self.lv3["num_sprintes"]
        super().incrementSprite()

    # def show(self):
    #     super().show()
    #     for ennemy in ennemies:
    #         if ennemy.state == "die":
    #             if ennemy.y < self.y:
    #                 self.canvas.tag_raise(self.last_img, ennemy.last_img)
    #             else :
    #                 self.canvas.tag_lower(self.last_img, ennemy.last_img)


class Adventurer(Heros):
    # Stats du Héros
    name = "Aventurier"
    hp = 100
    damage = 4
    damagingSprite = [1, 2, 3, 4]
    speed = 8
    attackSpeed = 4

    # Spritesheet du Heros
    barOffsetx = -8.5
    barOffsety = 10
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

    def transform(self):
        pass


class Ichigo(Heros):
    # Stats du Héros
    name = "Ichigo"

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
        "speed": 8,
        "attackSpeed": 4,

        # Spritesheet du Heros
        "damagingSprite" : [2,3,5,12,13],
        "num_sprintes": {"idle": 2, "runRight": 8,
                         "runLeft": 8, "attackRight": 16, "attackLeft": 16, "die": 2, "transform": 20},
        "spritesheet": "view/src/Ichigo0.png",
        "spriteSize": 200,
        "y_Anim": {"idle": 0, "runRight": 400, "runLeft": 600,
                   "attackRight": 800, "attackLeft": 1000, "die": 0, "transform": 1800}
    }

    lv1 = {
        "hp": 50,
        "damage": 2,
        "speed": 8,
        "attackSpeed": 6,

        # Spritesheet du Heros
        "damagingSprite" : [2,3,7,8,9,13,14,17,18],
        "num_sprintes": {"idle": 2, "runRight": 8,
                         "runLeft": 8, "attackRight": 23, "attackLeft": 23, "die": 2, "transform": 7},
        "spritesheet": "view/src/Ichigo1.png",
        "spriteSize": 200,
        "y_Anim": {"idle": 0, "runRight": 400, "runLeft": 600,
                   "attackRight": 1200, "attackLeft": 1400, "die": 0, "transform": 2200}
    }

    lv2 = {
        "hp": 50,
        "damage": 2,
        "speed": 8,
        "attackSpeed": 6,

        # Spritesheet du Heros
        "damagingSprite" : [1,2,6,7,11,12,13,14],
        "num_sprintes": {"idle": 2, "runRight": 8,
                         "runLeft": 8, "attackRight": 18, "attackLeft": 18, "die": 2, "transform": 7},
        "spritesheet": "view/src/Ichigo2.png",
        "spriteSize": 200,
        "y_Anim": {"idle": 0, "runRight": 800, "runLeft": 1000,
                   "attackRight": 1200, "attackLeft": 1400, "die": 0, "transform": 1200}
    }

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
        "speed": 10,
        "attackSpeed": 3,
        "num_sprintes": {"idle": 8, "runRight": 4,
                         "runLeft": 4, "attackRight": 15, "attackLeft": 15, "die": 8, "transform": 9},
        "spritesheet": "view/src/Goku0.png",
        "spriteSize": 200,
        "y_Anim": {"idle": 200, "runRight": 400, "runLeft": 600,
                   "attackRight": 1200, "attackLeft": 1400, "die": 200, "transform": 2200}
    }

    lv1 = {
        "hp": 50,
        "damage": 4,
        "damagingSprite": [2, 3, 4, 5, 6, 7, 12, 13, 14, 15],
        "speed": 15,
        "attackSpeed": 3,
        "num_sprintes": {"idle": 4, "runRight": 4,
                         "runLeft": 4, "attackRight": 15, "attackLeft": 15, "die": 4, "transform": 8},
        "spritesheet": "view/src/Goku1.png",
        "spriteSize": 200,
        "y_Anim": {"idle": 200, "runRight": 400, "runLeft": 600,
                   "attackRight": 1200, "attackLeft": 1400, "die": 200, "transform": 2200}
    }

    lv2 = {
        "hp": 50,
        "damage": 4,
        "damagingSprite": [1, 2, 3, 5, 6, 7, 8, 12, 13, 16, 17, 21, 22, 23, 24, 25],
        "speed": 20,
        "attackSpeed": 5,
        "num_sprintes": {"idle": 4, "runRight": 4,
                         "runLeft": 4, "attackRight": 26, "attackLeft": 26, "die": 4, "transform": 8},
        "spritesheet": "view/src/Goku2.png",
        "spriteSize": 200,
        "y_Anim": {"idle": 200, "runRight": 400, "runLeft": 600,
                   "attackRight": 1200, "attackLeft": 1400, "die": 200, "transform": 2200}
    }

    lv3 = {
        "hp": 50,
        "damage": 4,
        "speed": 25,
        "attackSpeed": 5,
        "damagingSprite": [3, 7, 10, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24],
        "num_sprintes": {"idle": 4, "runRight": 4,
                         "runLeft": 4, "attackRight": 24, "attackLeft": 24, "die": 4, "transform": 8},
        "spritesheet": "view/src/Goku3.png",
        "spriteSize": 200,
        "y_Anim": {"idle": 200, "runRight": 400, "runLeft": 600,
                   "attackRight": 800, "attackLeft": 1000, "die": 200}
    }
