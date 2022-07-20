from model.Heros import Heros
from model.coupspe import *
from model.State import State

class Adventurer(Heros):

    name = "Aventurier"

    lv0 = {
        "hp": 200,
        "damage": 17,
        "speed": 8,
        "attackSpeed": 4,

        # Spritesheet du Heros
        "barOffsety": 10,
        "damagingSprite": [1, 2, 3, 4],
        "num_sprintes": {State.IdleLeft: 13, State.IdleRight: 13, State.RunRight: 8,
                         State.RunLeft: 8, State.AttackRight: 10, State.AttackLeft: 10, State.Die: 7},
        "spritesheet": "view/src/personnage/heros/Aventurier/Adventurer.png",
        "spriteSize": 32,
        "zoom": 2,
        "y_Anim": {State.IdleLeft: 256, State.IdleRight: 0, State.RunRight: 32, State.RunLeft: 288,
                   State.AttackRight: 64, State.AttackLeft: 324, State.Die: 224}
    }

    def transform(self):
        pass


class Ichigo(Heros):
    # Stats du Héros
    name = "Ichigo"

    def defineStats(self):
        self.lv0 = {
            "hp": 150,
            "damage": 10,
            "speed": 8,
            "coupSpe": GetsugaTenshou,
            "attackSpeed": 3,

            # Spritesheet du Heros
            "damagingSprite": [2, 3, 5, 12, 13],
            "num_sprintes": {State.IdleRight: 2, State.IdleLeft: 2, State.RunRight: 8,
                             State.RunLeft: 8, State.AttackRight: 16, State.AttackLeft: 16, State.SpecialMoveRight: 19, State.SpecialMoveLeft: 19, State.Die: 8, State.Transform: 20},
            "spritesheet": "view/src/personnage/heros/Ichigo/Ichigo0 (" + str(self.quality) + ").png",
            "spriteSize": 200/self.quality,
            "zoom": self.quality,
            "y_Anim": {State.IdleRight: 0/self.quality, State.IdleLeft: 200/self.quality, State.RunRight: 400/self.quality, State.RunLeft: 600/self.quality,
                       State.AttackRight: 800/self.quality, State.AttackLeft: 1000/self.quality, State.Die: 0/self.quality, State.SpecialMoveRight: 1200/self.quality, State.SpecialMoveLeft: 1400/self.quality, State.Transform: 1800/self.quality, State.Die: 2000/self.quality}
        }

        self.lv1 = {
            "hp": 300,
            "damage": 15,
            "speed": 8,
            "coupSpe": GetsugaTenshou2,
            "attackSpeed": 3,

            # Spritesheet du Heros
            "damagingSprite": [2, 3, 7, 8, 9, 13, 14, 17, 18],
            "num_sprintes": {State.IdleRight: 2, State.IdleLeft: 2, State.RunRight: 8, State.InstantMove: 2,
                             State.RunLeft: 8, State.AttackRight: 23, State.AttackLeft: 23, State.Die: 8, State.Transform: 7, State.SpecialMoveRight: 13, State.SpecialMoveLeft: 13},
            "spritesheet": "view/src/personnage/heros/Ichigo/Ichigo1 (" + str(self.quality) + ").png",
            "spriteSize": 200/self.quality,
            "zoom": self.quality,
            "y_Anim": {State.IdleRight: 0/self.quality, State.IdleLeft: 200/self.quality, State.RunRight: 400/self.quality, State.RunLeft: 600/self.quality, State.InstantMove: 800/self.quality,
                       State.AttackRight: 1200/self.quality, State.AttackLeft: 1400/self.quality, State.Die: 0/self.quality, State.SpecialMoveRight: 1600/self.quality, State.SpecialMoveLeft: 1800/self.quality, State.Transform: 2200/self.quality, State.Die: 2400/self.quality}
        }

        self.lv2 = {
            "hp": 450,
            "damage": 20,
            "speed": 7,
            "coupSpe": GetsugaTenshou3,
            "attackSpeed": 4,

            # Spritesheet du Heros
            "damagingSprite": [1, 2, 6, 7, 11, 12, 13, 14],
            "num_sprintes": {State.IdleRight: 2, State.IdleLeft: 2, State.RunRight: 8, State.InstantMove: 2,
                             State.RunLeft: 8, State.AttackRight: 18, State.AttackLeft: 18, State.Die: 5, State.Transform: 6, State.SpecialMoveRight: 14, State.SpecialMoveLeft: 14},
            "spritesheet": "view/src/personnage/heros/Ichigo/Ichigo2 (" + str(self.quality) + ").png",
            "spriteSize": 200/self.quality,
            "zoom": self.quality,
            "y_Anim": {State.IdleRight: 0/self.quality, State.IdleLeft: 200/self.quality, State.RunRight: 800/self.quality, State.RunLeft: 1000/self.quality, State.InstantMove: 400/self.quality,
                       State.AttackRight: 1200/self.quality, State.AttackLeft: 1400/self.quality, State.SpecialMoveRight: 1600/self.quality, State.SpecialMoveLeft: 1800/self.quality, State.Die: 0/self.quality, State.Transform: 2200/self.quality, State.Die: 2400/self.quality}
        }

        self.lv3 = {
            "hp": 600,
            "damage": 25,
            "speed": 8,
            "attackSpeed": 5,
            "coupSpe": Mugetsu,
            # Spritesheet du Heros
            "damagingSprite": [1, 2, 3, 4, 5],
            "num_sprintes": {State.IdleRight: 4, State.IdleLeft: 4, State.RunRight: 2, State.InstantMove: 2,
                             State.RunLeft: 2, State.AttackRight: 6, State.AttackLeft: 6, State.Transform: 6, State.Die: 5, State.SpecialMoveRight: 14, State.SpecialMoveLeft: 14},
            "spritesheet": "view/src/personnage/heros/Ichigo/Ichigo3 (" + str(self.quality) + ").png",
            "spriteSize": 200/self.quality,
            "zoom": self.quality,
            "y_Anim": {State.IdleRight: 0/self.quality, State.IdleLeft: 200/self.quality, State.RunRight: 800/self.quality, State.RunLeft: 1000/self.quality, State.InstantMove: 400/self.quality,
                       State.AttackRight: 1200/self.quality, State.AttackLeft: 1400/self.quality, State.SpecialMoveRight: 1600/self.quality, State.SpecialMoveLeft: 1800/self.quality, State.Die: 0/self.quality, State.Die: 2000/self.quality}
        }


class Goku(Heros):
    name = "Goku"

    def defineStats(self):
        self.lv0 = {
            "hp": 150,
            "damage": 10,
            "damagingSprite": [5, 10, 11, 12, 13, 18, 22, 23],
            "speed": 10,
            "coupSpe": Kamehameha,
            "attackSpeed": 3,
            "num_sprintes": {State.IdleRight: 8, State.IdleLeft: 8, State.RunRight: 4,
                             State.RunLeft: 4, State.AttackRight: 15, State.AttackLeft: 15, State.Die: 5, State.Transform: 9, State.SpecialMoveRight: 16, State.SpecialMoveLeft: 16},
            "spritesheet": "view/src/personnage/heros/Goku/Goku0 (" + str(self.quality) + ").png",
            "spriteSize": 200/self.quality,
            "zoom": self.quality,
            "y_Anim": {State.IdleRight: 0/self.quality, State.IdleLeft: 200/self.quality, State.RunRight: 400/self.quality, State.RunLeft: 600/self.quality,
                       State.AttackRight: 1200/self.quality, State.AttackLeft: 1400/self.quality, State.Die: 200/self.quality, State.Transform: 2200/self.quality,
                       State.SpecialMoveRight: 1600/self.quality, State.SpecialMoveLeft: 1800/self.quality, State.Die: 2400/self.quality}
        }

        self.lv1 = {
            "hp": 300,
            "damage": 15,
            "damagingSprite": [2, 3, 4, 5, 6, 7, 12, 13, 14, 15],
            "speed": 15,
            "coupSpe": Kamehameha2,
            "attackSpeed": 4,
            "num_sprintes": {State.IdleRight: 4, State.IdleLeft: 4, State.RunRight: 4,
                             State.RunLeft: 4, State.AttackRight: 15, State.AttackLeft: 15, State.Die: 5, State.Transform: 8, State.SpecialMoveRight: 17, State.SpecialMoveLeft: 17, State.InstantMove: 4},
            "spritesheet": "view/src/personnage/heros/Goku/Goku1 (" + str(self.quality) + ").png",
            "spriteSize": 200/self.quality,
            "zoom": self.quality,
            "y_Anim": {State.IdleRight: 0/self.quality, State.IdleLeft: 200/self.quality, State.RunRight: 400/self.quality, State.RunLeft: 600/self.quality,
                       State.InstantMove: 800/self.quality, State.AttackRight: 1200/self.quality, State.AttackLeft: 1400/self.quality, State.Die: 200/self.quality,
                       State.Transform: 2200/self.quality, State.SpecialMoveRight: 1600/self.quality, State.SpecialMoveLeft: 1800/self.quality, State.Die: 2400/self.quality}
        }

        self.lv2 = {
            "hp": 450,
            "damage": 20,
            "damagingSprite": [1, 2, 3, 5, 6, 7, 8, 12, 13, 16, 17, 21, 22, 23, 24, 25],
            "speed": 20,
            "coupSpe": Kamehameha3,
            "attackSpeed": 5,
            "num_sprintes": {State.IdleRight: 4, State.IdleLeft: 4, State.RunRight: 4,
                             State.RunLeft: 4, State.AttackRight: 26, State.AttackLeft: 26, State.Die: 3, State.Transform: 8, State.SpecialMoveRight: 17, State.SpecialMoveLeft: 17, State.InstantMove: 3},
            "spritesheet": "view/src/personnage/heros/Goku/Goku2 (" + str(self.quality) + ").png",
            "spriteSize": 200/self.quality,
            "zoom": self.quality,
            "y_Anim": {State.IdleRight: 0/self.quality, State.IdleLeft: 200/self.quality, State.RunRight: 400/self.quality, State.RunLeft: 600/self.quality, State.InstantMove: 800/self.quality,
                       State.AttackRight: 1200/self.quality, State.AttackLeft: 1400/self.quality, State.Die: 200/self.quality, State.Transform: 2200/self.quality, State.SpecialMoveRight: 1600/self.quality, State.SpecialMoveLeft: 1800/self.quality, State.Die: 2400/self.quality}
        }

        self.lv3 = {
            "hp": 600,
            "damage": 25,
            "speed": 25,
            "attackSpeed": 6,
            "coupSpe": Genkidamasupreme,
            "damagingSprite": [3, 7, 10, 12, 13, 14, 16, 17, 18, 19, 20, 21, 22, 23, 24],
            "num_sprintes": {State.IdleRight: 4, State.IdleLeft: 4, State.RunRight: 4,
                             State.RunLeft: 4, State.AttackRight: 24, State.AttackLeft: 24, State.Die: 6, State.Transform: 8, State.SpecialMoveRight: 8, State.SpecialMoveLeft: 8, State.InstantMove: 2},
            "spritesheet": "view/src/personnage/heros/Goku/Goku3 (" + str(self.quality) + ").png",
            "spriteSize": 200/self.quality,
            "zoom": self.quality,
            "y_Anim": {State.IdleRight: 0/self.quality, State.IdleLeft: 200/self.quality, State.RunRight: 400/self.quality, State.RunLeft: 600/self.quality, State.InstantMove: 0/self.quality,
                       State.AttackRight: 800/self.quality, State.AttackLeft: 1000/self.quality, State.Die: 200/self.quality, State.SpecialMoveRight: 1200/self.quality, State.SpecialMoveLeft: 1400/self.quality, State.Die: 1600/self.quality}
        }
