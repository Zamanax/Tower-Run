from Character import Character

class Heros(Character) : 
    def __init__(self):
        self.team = "ally"
        self.hp = 30
        self.name = "Heros"
        self.speed = 5
        self.attackSpeed = 2
        self.state = "idle"
