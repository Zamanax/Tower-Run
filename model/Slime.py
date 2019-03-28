from Character import Character


class Slime (Character):
    target = None
    def __init__(self):
        self.hp = 30
        self.name = "Slime"
        self.speed = 1
        self.attackSpeed = 1
        self.state = "move"

    def move(self):
        self.position += self.speed

    def attack(self):
        if self.target:
            self.target.hp -= self.damage
