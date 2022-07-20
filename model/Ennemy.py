from model.Character import Character
import model.Heros as He
from model.State import State

coeffv = 2


class Ennemy (Character):

    def __init__(self, parent, x, y, **kwargs):
        # Initialisation en tant que Character
        Character.__init__(self, parent, x, y)

        # Insertion dans le tableau
        # Tableau contenant tous les ennemis existants
        parent.ennemies.append(self)

        # Le Monstre se dirige toujours vers l'objectif dès son apparition
        self.path = kwargs.get("path", None)
        if self.path == None:
            self.path = self.parent.defaultPath
        self.goToObjective()

    # Fonction chargée de faire déplacer le monstre
    def goToObjective(self):
        if self.move == None:
            if self.pathIndex != len(self.path):
                self.moveTo(self.path[self.pathIndex].x,
                            self.path[self.pathIndex].y)
            else:
                self.loseLife()

    def loseLife(self):
        if self.parent.lost is None:
            self.parent.health.set(self.parent.health.get() - 1)
            if self.parent.health.get() <= 0:
                self.parent.loseGame()
        del self

# ---------------------------- Différents ennemis présents dans le jeu --------------


class Skeleton (Ennemy):
    hp = 100 * coeffv
    name = "Skeleton"
    attackSpeed = 1
    speed = 2
    damage = 5

    barOffsetx = -20

    spriteSize = 32
    y_Anim = {State.IdleRight: 32, State.IdleLeft: 0, State.RunRight: 32,
              State.RunLeft: 0, State.AttackRight: 32, State.AttackLeft: 0, State.Die: 64}
    damagingSprite = [4, 6, 7, 8]
    num_sprintes = {State.IdleRight: 1, State.IdleLeft: 1, State.RunRight: 4,
                    State.RunLeft: 4, State.AttackRight: 8, State.AttackLeft: 8, State.Die: 4}
    spritesheet = "view/src/personnage/ennemis/Skeleton.png"
    zoom = 2
    dps = damage*len(damagingSprite) / \
        (0.5/attackSpeed*num_sprintes[State.AttackRight])
    purse = int(int(hp/5+dps*1.5+speed))


class miniSkeleton (Skeleton):
    hp = 50 * coeffv
    attackSpeed = 2
    speed = 2
    damage = 1
    zoom = 1
    damagingSprite = [4, 6, 7, 8]
    num_sprintes = {State.IdleRight: 1, State.IdleLeft: 1, State.RunRight: 4,
                    State.RunLeft: 4, State.AttackRight: 8, State.AttackLeft: 8, State.Die: 4}
    dps = damage*len(damagingSprite) / \
        (0.5/attackSpeed*num_sprintes[State.AttackRight])
    purse = int(int(hp/5+dps*1.5+speed))


class Bat(Ennemy):

    y_Anim = {State.IdleRight: 0, State.IdleLeft: 23, State.RunRight: 0,
              State.RunLeft: 23, State.AttackRight: 46, State.AttackLeft: 69, State.Die: 82}
    hp = 80 * coeffv
    name = 'Bat'
    attackSpeed = 2
    speed = 3
    damage = 5

    spritesheet = 'view/src/personnage/ennemis/batp.png'
    spriteSize = 23
    damagingSprite = [2]
    num_sprintes = {State.IdleRight: 5, State.IdleLeft: 5, State.RunRight: 5,
                    State.RunLeft: 5, State.AttackRight: 5, State.AttackLeft: 5, State.Die: 5}
    zoom = 2
    dps = damage*len(damagingSprite) / \
        (0.5/attackSpeed*num_sprintes[State.AttackRight])
    purse = int(hp/5+dps*1.5+speed)


class Dwarf (Ennemy):

    hp = 100 * coeffv
    name = 'Dwarf'
    attackSpeed = 3
    speed = 4
    damage = 5

    spritesheet = 'view/src/personnage/ennemis/Dwarf.png'
    spriteSize = 96
    damagingSprite = [2]
    num_sprintes = {State.IdleRight: 5, State.IdleLeft: 5, State.RunRight: 8,
                    State.RunLeft: 8, State.AttackRight: 9, State.AttackLeft: 9, State.Die: 6}
    y_Anim = {State.IdleRight: 5, State.IdleLeft: 5, State.RunRight: 8,
              State.RunLeft: 8, State.AttackRight: 9, State.AttackLeft: 9, State.Die: 6}
    zoom = 1
    dps = damage*len(damagingSprite) / \
        (0.5/attackSpeed*num_sprintes[State.AttackRight])
    purse = int(hp/5+dps*1.5+speed)


class SlimeE(Ennemy):

    hp = 150 * coeffv
    name = 'SlimeE'
    i = 0

    attackSpeed = 1
    speed = 1
    damage = 5

    barOffsety = 10
    barOffsetx = -5

    spritesheet = 'view/src/personnage/ennemis/Slime.png'
    spriteSize = 32
    damagingSprite = [5, 7, 8]
    num_sprintes = {State.IdleRight: 10, State.IdleLeft: 10, State.RunRight: 10,
                    State.RunLeft: 10, State.AttackRight: 10, State.AttackLeft: 10, State.Die: 10}
    zoom = 2
    y_Anim = {State.IdleRight: 0+160*i, State.IdleLeft: 0+160*i, State.RunRight: 32+160*i, State.RunLeft: 32 +
              160*i, State.AttackRight: 32*3+160*i, State.AttackLeft: 32*3+160*i, State.Die: 32*4+160*i}
    dps = damage*len(damagingSprite) / \
        (0.5/attackSpeed*num_sprintes[State.AttackRight])
    purse = int(hp/5+dps*1.5+speed)


class SlimeF(SlimeE):

    hp = 150 * coeffv
    name = 'SlimeF'
    i = 2

    attackSpeed = 1
    speed = 1
    damage = 5

    spritesheet = 'view/src/personnage/ennemis/Slime.png'
    spriteSize = 32
    damagingSprite = [5, 7, 8]
    num_sprintes = {State.IdleRight: 10, State.IdleLeft: 10, State.RunRight: 10,
                    State.RunLeft: 10, State.AttackRight: 10, State.AttackLeft: 10, State.Die: 10}
    zoom = 2
    y_Anim = {State.IdleRight: 0+160*i, State.IdleLeft: 0+160*i, State.RunRight: 32+160*i, State.RunLeft: 32 +
              160*i, State.AttackRight: 32*3+160*i, State.AttackLeft: 32*3+160*i, State.Die: 32*4+160*i}
    dps = damage*len(damagingSprite) / \
        (0.5/attackSpeed*num_sprintes[State.AttackRight])
    purse = int(hp/5+dps*1.5+speed)


class SlimeW(SlimeE):

    hp = 150 * coeffv
    name = 'SlimeW'
    i = 1

    attackSpeed = 1
    speed = 1
    damage = 5

    spritesheet = 'view/src/personnage/ennemis/Slime.png'
    spriteSize = 32
    damagingSprite = [5, 7, 8]
    num_sprintes = {State.IdleRight: 10, State.IdleLeft: 10, State.RunRight: 10,
                    State.RunLeft: 10, State.AttackRight: 10, State.AttackLeft: 10, State.Die: 10}
    zoom = 2
    y_Anim = {State.IdleRight: 0+160*i, State.IdleLeft: 0+160*i, State.RunRight: 32+160*i, State.RunLeft: 32 +
              160*i, State.AttackRight: 32*3+160*i, State.AttackLeft: 32*3+160*i, State.Die: 32*4+160*i}
    dps = damage*len(damagingSprite) / \
        (0.5/attackSpeed*num_sprintes[State.AttackRight])
    purse = int(hp/5+dps*1.5+speed)


class Gladiator(Ennemy):
    y_Anim = {State.IdleRight: 0, State.IdleLeft: 32*5, State.RunRight: 32,
              State.RunLeft: 32*6, State.AttackRight: 32*2, State.AttackLeft: 32*7, State.Die: 32*4}

    hp = 200 * coeffv
    name = 'Gladiator'
    attackSpeed = 1
    speed = 1
    damage = 25

    spritesheet = 'view/src/personnage/ennemis/Gladiator.png'
    spriteSize = 32
    damagingSprite = [4]
    num_sprintes = {State.IdleRight: 5, State.IdleLeft: 5, State.RunRight: 8,
                    State.RunLeft: 8, State.AttackRight: 7, State.AttackLeft: 7, State.Die: 7}
    zoom = 2
    dps = damage*len(damagingSprite) / \
        (0.5/attackSpeed*num_sprintes[State.AttackRight])
    purse = int(hp/5+dps*1.5+speed)


class Totor (Ennemy):

    hp = 250 * coeffv
    name = "Totor"
    attackSpeed = 2
    speed = 1
    damage = 20

    spritesheet = 'view/src/personnage/ennemis/Totor.png'
    spriteSize = 96
    y_Anim = {State.IdleRight: 0, State.IdleLeft: 960, State.RunRight: 96,
              State.RunLeft: 96*12, State.AttackRight: 96*3, State.AttackLeft: 96*13, State.Die: 96*9}
    damagingSprite = [1, 3]
    num_sprintes = {State.IdleRight: 5, State.IdleLeft: 5, State.RunRight: 8,
                    State.RunLeft: 8, State.AttackRight: 9, State.AttackLeft: 9, State.Die: 6}
    zoom = 2
    dps = damage*len(damagingSprite) / \
        (0.5/attackSpeed*num_sprintes[State.AttackRight])
    purse = int(hp/5+dps*1.5+speed)


class Fat_Totor (Totor):
    hp = 750 * coeffv
    name = "Fat Totor"
    damage = 40
    speed = 1
    zoom = 3

    num_sprintes = {State.IdleRight: 5, State.IdleLeft: 5, State.RunRight: 8,
                    State.RunLeft: 8, State.AttackRight: 9, State.AttackLeft: 9, State.Die: 6}
    attackSpeed = 1
    damagingSprite = [1, 3]
    dps = damage*len(damagingSprite) / \
        (0.5/attackSpeed*num_sprintes[State.AttackRight])
    purse = int(hp/5+dps*1.5+speed)


class RedGladiator(Gladiator):
    y_Anim = {State.IdleRight: 0, State.IdleLeft: 32*5, State.RunRight: 32,
              State.RunLeft: 32*6, State.AttackRight: 32*2, State.AttackLeft: 32*7, State.Die: 32*4}

    hp = 500
    name = 'RedGladiator'
    speed = 1
    attackSpeed = 1
    damage = 30

    spritesheet = 'view/src/personnage/ennemis/RedGladiator.png'
    spriteSize = 32
    damagingSprite = [4]
    num_sprintes = {State.IdleRight: 5, State.IdleLeft: 5, State.RunRight: 8,
                    State.RunLeft: 8, State.AttackRight: 7, State.AttackLeft: 7, State.Die: 7}
    zoom = 2
    dps = damage*len(damagingSprite) / \
        (0.5/attackSpeed*num_sprintes[State.AttackRight])
    purse = int(hp/5+dps*1.5+speed)
