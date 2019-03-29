from Character import Character

class Slime (Character):
    def __init__(self):
        self.team = "ennemy"
        self.gold = 5
        self.hp = 30
        self.name = "Slime"
        self.speed = 1
        self.attackSpeed = 1
        self.state = "move"
