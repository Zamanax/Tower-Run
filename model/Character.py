class Character () :
    hp = 0
    name = ""
    speed = 0
    damage = 0
    attackSpeed = 0
    state = ""
    position = 0
    def move(self):
        raise NotImplementedError
    def attack(self):
        raise NotImplementedError
    def afficher(self):
        raise NotImplementedError