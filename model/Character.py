import tkinter as tk

class Character (tk.Canvas):
    team = ""
    hp = 0
    name = ""
    speed = 0
    damage = 0
    attackSpeed = 0
    state = ""
    position = 0
    target = None

    last_img = None
    images = []
    num_sprintes = 0
    spritesheet = None

    def move(self):
        self.position += self.speed

    def attack(self):
        if self.target:
            self.target.hp -= self.damage
        else :
            raise NameError("NoTargetError")
