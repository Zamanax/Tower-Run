import tkinter as tk
from Heros import Heros
from Character import Character
from coupspe import *

class Adventurer(Heros):

    name = "Aventurier"

    lv0 = {
        "hp": 100,
        "damage": 4,
        "speed": 8,
        "attackSpeed": 4,

        # Spritesheet du Heros
        "barOffsety": 10,
        "damagingSprite": [1, 2, 3, 4],
        "num_sprintes": {"idleLeft": 13, "idleRight": 13, "runRight": 8,
                         "runLeft": 8, "attackRight": 10, "attackLeft": 10, "die": 7},
        "spritesheet": "view/src/personnage/heros/Aventurier/Adventurer.png",
        "spriteSize": 32,
        "zoom": 2,
        "y_Anim": {"idleLeft": 256, "idleRight": 0, "runRight": 32, "runLeft": 288,
                   "attackRight": 64, "attackLeft": 324, "die": 224}
    }

    def __init__(self, canvas, x, y, max_y, min_y):
        Heros.__init__(self, canvas, x, y, max_y, min_y)
        self.max_y -= 5
        self.min_y -= 5

    def transform(self):
        pass


class Ichigo(Heros):
    # Stats du Héros
    name = "Ichigo"

    lv0 = {
        "hp": 50,
        "damage": 2,
        "speed": 8,
        "coupSpe": GetsugaTenshou,
        "attackSpeed": 4,

        # Spritesheet du Heros
        "damagingSprite": [2, 3, 5, 12, 13],
        "num_sprintes": {"idleRight": 2, "idleLeft": 2, "runRight": 8,
                         "runLeft": 8, "attackRight": 16, "attackLeft": 16, "specialMoveRight": 19, "specialMoveLeft": 19, "die": 2, "transform": 20},
        "spritesheet": "view/src/personnage/heros/Ichigo/Ichigo0.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idleRight": 0, "idleLeft": 200, "runRight": 400, "runLeft": 600,
                   "attackRight": 800, "attackLeft": 1000, "die": 0, "specialMoveRight": 1200, "specialMoveLeft": 1400, "transform": 1800}
    }

    lv1 = {
        "hp": 50,
        "damage": 2,
        "speed": 8,
        "coupSpe": GetsugaTenshou2,
        "attackSpeed": 6,

        # Spritesheet du Heros
        "damagingSprite": [2, 3, 7, 8, 9, 13, 14, 17, 18],
        "num_sprintes": {"idleRight": 2, "idleLeft": 2, "runRight": 8, "instantMove": 2,
                         "runLeft": 8, "attackRight": 23, "attackLeft": 23, "die": 2, "transform": 7, "specialMoveRight": 13, "specialMoveLeft": 13},
        "spritesheet": "view/src/personnage/heros/Ichigo/Ichigo1.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idleRight": 0, "idleLeft": 200, "runRight": 400, "runLeft": 600, "instantMove": 800,
                   "attackRight": 1200, "attackLeft": 1400, "die": 0, "specialMoveRight": 1600, "specialMoveLeft": 1800, "transform": 2200}
    }

    lv2 = {
        "hp": 50,
        "damage": 2,
        "speed": 8,
        "coupSpe": GetsugaTenshou3,
        "attackSpeed": 6,

        # Spritesheet du Heros
        "damagingSprite": [1, 2, 6, 7, 11, 12, 13, 14],
        "num_sprintes": {"idleRight": 2, "idleLeft": 2, "runRight": 8, "instantMove": 2,
                         "runLeft": 8, "attackRight": 18, "attackLeft": 18, "die": 2, "transform": 6, "specialMoveRight": 14, "specialMoveLeft": 14},
        "spritesheet": "view/src/personnage/heros/Ichigo/Ichigo2.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idleRight": 0, "idleLeft": 200, "runRight": 800, "runLeft": 1000, "instantMove": 400,
                   "attackRight": 1200, "attackLeft": 1400, "specialMoveRight": 1600, "specialMoveLeft": 1800, "die": 0, "transform": 2200}
    }

    lv3 = {
        "hp": 50,
        "damage": 2,
        "speed": 8,
        "attackSpeed": 6,
        "coupSpe": Mugetsu,
        # Spritesheet du Heros
        "damagingSprite": [1, 2, 6, 7, 11, 12, 13, 14],
        "num_sprintes": {"idleRight": 4, "idleLeft": 4, "runRight": 2, "instantMove": 2,
                         "runLeft": 2, "attackRight": 6, "attackLeft": 6, "die": 2, "specialMoveRight": 14, "specialMoveLeft": 14},
        "spritesheet": "view/src/personnage/heros/Ichigo/Ichigo3.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idleRight": 0, "idleLeft": 200, "runRight": 800, "runLeft": 1000, "instantMove": 400,
                   "attackRight": 1200, "attackLeft": 1400, "specialMoveRight": 1600, "specialMoveLeft": 1800, "die": 0}
    }


class Goku(Heros):
    name = "Goku"
    lv0 = {
        "hp": 50,
        "damage": 2,
        "damagingSprite": [5, 10, 11, 12, 13, 18, 22, 23],
        "speed": 10,
        "coupSpe": Kamehameha,
        "attackSpeed": 3,
        "num_sprintes": {"idleRight": 8, "idleLeft": 8, "runRight": 4,
                         "runLeft": 4, "attackRight": 15, "attackLeft": 15, "die": 8, "transform": 9, "specialMoveRight": 16, "specialMoveLeft": 16},
        "spritesheet": "view/src/personnage/heros/Goku/Goku0.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idleRight": 0, "idleLeft": 200, "runRight": 400, "runLeft": 600,
                   "attackRight": 1200, "attackLeft": 1400, "die": 200, "transform": 2200, "specialMoveRight": 1600, "specialMoveLeft": 1800}
    }

    lv1 = {
        "hp": 50,
        "damage": 4,
        "damagingSprite": [2, 3, 4, 5, 6, 7, 12, 13, 14, 15],
        "speed": 15,
        "coupSpe": Kamehameha2,
        "attackSpeed": 3,
        "num_sprintes": {"idleRight": 4, "idleLeft": 4, "runRight": 4,
                         "runLeft": 4, "attackRight": 15, "attackLeft": 15, "die": 4, "transform": 8, "specialMoveRight": 17, "specialMoveLeft": 17, "instantMove": 4},
        "spritesheet": "view/src/personnage/heros/Goku/Goku1.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idleRight": 0, "idleLeft": 200, "runRight": 400, "runLeft": 600, "instantMove": 800,
                   "attackRight": 1200, "attackLeft": 1400, "die": 200, "transform": 2200, "specialMoveRight": 1600, "specialMoveLeft": 1800}
    }

    lv2 = {
        "hp": 50,
        "damage": 4,
        "damagingSprite": [1, 2, 3, 5, 6, 7, 8, 12, 13, 16, 17, 21, 22, 23, 24, 25],
        "speed": 20,
        "coupSpe": Kamehameha3,
        "attackSpeed": 5,
        "num_sprintes": {"idleRight": 4, "idleLeft": 4, "runRight": 4,
                         "runLeft": 4, "attackRight": 26, "attackLeft": 26, "die": 4, "transform": 8, "specialMoveRight": 17, "specialMoveLeft": 17, "instantMove": 3},
        "spritesheet": "view/src/personnage/heros/Goku/Goku2.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idleRight": 0, "idleLeft": 200, "runRight": 400, "runLeft": 600, "instantMove": 800,
                   "attackRight": 1200, "attackLeft": 1400, "die": 200, "transform": 2200, "specialMoveRight": 1600, "specialMoveLeft": 1800}
    }

    lv3 = {
        "hp": 50,
        "damage": 4,
        "speed": 25,
        "attackSpeed": 5,
        "coupSpe": Genkidamasupreme,
        "damagingSprite": [3, 7, 10, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24],
        "num_sprintes": {"idleRight": 4, "idleLeft": 4, "runRight": 4,
                         "runLeft": 4, "attackRight": 24, "attackLeft": 24, "die": 4, "transform": 8, "specialMoveRight": 8, "specialMoveLeft": 8, "instantMove": 2},
        "spritesheet": "view/src/personnage/heros/Goku/Goku3.png",
        "spriteSize": 200,
        "zoom": 1,
        "y_Anim": {"idleRight": 0, "idleLeft": 200, "runRight": 400, "runLeft": 600, "instantMove": 0,
                   "attackRight": 800, "attackLeft": 1000, "die": 200, "specialMoveRight": 1200, "specialMoveLeft": 1400}
    }
