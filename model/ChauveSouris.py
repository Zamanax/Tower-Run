from Character import Character

class ChauveSouris (Character):
    def __init__(self):
        self.team = "ennemy"
        self.gold=8
        self.hp=30
        self.name= "Chauve-souris"
        self.speed=1
        self.attackSpeed=2
        self.state="move"
        mvtype ="fly"
