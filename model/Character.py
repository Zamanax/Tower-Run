class Character () :
    team = ""
    hp = 0
    name = ""
    speed = 0
    damage = 0
    attackSpeed = 0
    state = ""
    position = 0
    target = None
    mvtype= "ground"
    def move(self):
        self.position += self.speed
    def attack(self):
        if self.target:
            self.target.hp -= self.damage
        else :
            raise NameError("NoTargetError")
    def afficher(self):
        raise NotImplementedError
