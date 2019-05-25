from model.Character import Character
import model.Heros as He

coeffv =2
class Ennemy (Character):
 
    def __init__ (self, parent, x, y, **kwargs) :
        #Initialisation en tant que Character
        Character.__init__(self,parent,x,y)

        # Insertion dans le tableau
        # Tableau contenant tous les ennemis existants
        parent.ennemies.append(self)

        #Le Monstre se dirige toujours vers l'objectif dès son apparition
        self.path = kwargs.get("path", None)
        if self.path == None:
            self.path = self.parent.defaultPath
        self.goToObjective()

    # Fonction chargée de faire déplacer le monstre
    def goToObjective(self):
        if self.move == None:
            if self.pathIndex != len(self.path) :
                self.moveTo(self.path[self.pathIndex].x,self.path[self.pathIndex].y)
            else : 
                self.loseLife()

    def loseLife(self):
        if self.parent.health.get() <= 0 and self.parent.lost is None:
            self.parent.loseGame()
        else :
            self.parent.health.set(self.parent.health.get() - 1)
        del self

#---------------------------- Différents ennemis présents dans le jeu --------------
class Skeleton (Ennemy) :
    __slots__ = ("idle", "runRight", "runLeft", "attackRight", "attackLeft", "death")
    hp = 100 * coeffv
    name = "Skeleton"
    attackSpeed = 1
    speed = 2
    damage = 5


    barOffsetx = -20

    spriteSize = 32
    y_Anim = {"idleRight" : 32,"idleLeft":0, "runRight" : 32, "runLeft" : 0, "attackRight": 32, "attackLeft": 0, "die" : 64}
    damagingSprite = [4,6,7,8]
    num_sprintes = {"idleRight": 1, "idleLeft" : 1, "runRight" : 4, "runLeft" : 4, "attackRight" : 8, "attackLeft": 8, "die": 4}
    spritesheet = "view/src/personnage/ennemis/Skeleton.png"
    zoom = 2
    dps = damage*len(damagingSprite)/ (0.5/attackSpeed*num_sprintes["attackRight"])
    purse = hp/5+dps*1.5+speed
    
class miniSkeleton (Skeleton) :
    hp = 50 * coeffv
    attackSpeed = 2
    speed = 3
    damage = 1
    zoom = 1
    damagingSprite = [4,6,7,8]
    num_sprintes = {"idleRight": 1, "idleLeft" : 1, "runRight" : 4, "runLeft" : 4, "attackRight" : 8, "attackLeft": 8, "die": 4}
    dps = damage*len(damagingSprite)/ (0.5/attackSpeed*num_sprintes["attackRight"])
    purse = hp/5+dps*1.5+speed

class Bat(Ennemy):
    __slots__ = ('idle', 'runRight', 'runLeft', 'attackRight', 'attackLeft', "death")
 
    y_Anim = {'idleRight' : 0, "idleLeft": 23, 'runRight' : 0, 'runLeft' : 23, 'attackRight' : 46, 'attackLeft' : 69, 'die' : 82}
    hp = 80 * coeffv
    name = 'Bat'
    attackSpeed = 2
    speed = 3
    damage = 15
 

    spritesheet = 'view/src/personnage/ennemis/batp.png'
    spriteSize = 23
    damagingSprite = [2]
    num_sprintes = {'idleRight' : 5, "idleLeft": 5, 'runRight' : 5, 'runLeft' : 5, 'attackRight' : 5, 'attackLeft' : 5, 'die' : 5}
    zoom = 2
    dps = damage*len(damagingSprite)/ (0.5/attackSpeed*num_sprintes["attackRight"])
    purse = hp/5+dps*1.5+speed
    
class Dwarf (Ennemy) :
    __slots__ = ('idle', 'runRight', 'runLeft', 'attackRight', 'attackLeft', "death")

    hp = 100 * coeffv
    name = 'Dwarf'
    attackSpeed = 3
    speed = 4
    damage = 5


    spritesheet = 'view/src/personnage/ennemis/Dwarf.png'
    spriteSize = 96
    damagingSprite = [2]
    num_sprintes = {'idleRight' : 5, "idleLeft": 5, 'runRight' : 8, 'runLeft' : 8, 'attackRight' : 9, 'attackLeft' : 9, 'die' : 6}
    y_Anim = {'idleRight' : 5, "idleLeft": 5, 'runRight' : 8, 'runLeft' : 8, 'attackRight' : 9, 'attackLeft' : 9, 'die' : 6}
    zoom = 1
    dps = damage*len(damagingSprite)/ (0.5/attackSpeed*num_sprintes["attackRight"])
    purse = hp/5+dps*1.5+speed
    


class SlimeE(Ennemy):    
    __slots__ = ('idle', 'runRight', 'runLeft', 'attackRight', 'attackLeft', "death")
   

    hp = 150 * coeffv
    name= 'SlimeE'
    i=0


    attackSpeed = 1
    speed = 1
    damage = 5

    barOffsety = 10
    barOffsetx = -5

    spritesheet = 'view/src/personnage/ennemis/Slime.png'
    spriteSize = 32
    damagingSprite = [5,7,8]
    num_sprintes = {'idleRight' : 10, "idleLeft": 10, 'runRight' : 10, 'runLeft' : 10, 'attackRight' : 10, 'attackLeft' : 10, 'die' : 10}
    zoom = 2
    y_Anim = {'idleRight' : 0+160*i, "idleLeft": 0+160*i, 'runRight' : 32+160*i, 'runLeft' : 32+160*i, 'attackRight' : 32*3+160*i, 'attackLeft' : 32*3+160*i, 'die' : 32*4+160*i}
    dps = damage*len(damagingSprite)/ (0.5/attackSpeed*num_sprintes["attackRight"])
    purse = hp/5+dps*1.5+speed
    
class SlimeF(SlimeE):
    __slots__ = ('idle', 'runRight', 'runLeft', 'attackRight', 'attackLeft', "death")
   

    hp = 150 * coeffv
    name= 'SlimeF'
    i=2


    attackSpeed = 1
    speed = 1 
    damage = 5


    spritesheet = 'view/src/personnage/ennemis/Slime.png'
    spriteSize = 32
    damagingSprite = [5,7,8]
    num_sprintes = {'idleRight' : 10, "idleLeft": 10, 'runRight' : 10, 'runLeft' : 10, 'attackRight' : 10, 'attackLeft' : 10, 'die' : 10}
    zoom = 2
    y_Anim = {'idleRight' : 0+160*i, "idleLeft": 0+160*i, 'runRight' : 32+160*i, 'runLeft' : 32+160*i, 'attackRight' : 32*3+160*i, 'attackLeft' : 32*3+160*i, 'die' : 32*4+160*i}
    dps = damage*len(damagingSprite)/ (0.5/attackSpeed*num_sprintes["attackRight"])
    purse = hp/5+dps*1.5+speed

class SlimeW(SlimeE):
    __slots__ = ('idle', 'runRight', 'runLeft', 'attackRight', 'attackLeft', "death")
   

    hp = 150* coeffv
    name= 'SlimeW'
    i=1


    attackSpeed = 1
    speed = 1
    damage = 5
 

    spritesheet = 'view/src/personnage/ennemis/Slime.png'
    spriteSize = 32
    damagingSprite = [5,7,8]
    num_sprintes = {'idleRight' : 10, "idleLeft": 10, 'runRight' : 10, 'runLeft' : 10, 'attackRight' : 10, 'attackLeft' : 10, 'die' : 10}
    zoom = 2
    y_Anim = {'idleRight' : 0+160*i, "idleLeft": 0+160*i, 'runRight' : 32+160*i, 'runLeft' : 32+160*i, 'attackRight' : 32*3+160*i, 'attackLeft' : 32*3+160*i, 'die' : 32*4+160*i}
    dps = damage*len(damagingSprite)/ (0.5/attackSpeed*num_sprintes["attackRight"])
    purse = hp/5+dps*1.5+speed

class Gladiator(Ennemy):
    __slots__ = ('idle', 'runRight', 'runLeft', 'attackRight', 'attackLeft', "death")
    y_Anim = {'idleRight' : 0, "idleLeft": 32*5, 'runRight' : 32, 'runLeft' : 32*6, 'attackRight' : 32*2, 'attackLeft' : 32*7, 'die' : 32*4}

    hp = 200 * coeffv 
    name = 'Gladiator'
    attackSpeed = 1
    speed = 1
    damage = 25


    spritesheet = 'view/src/personnage/ennemis/Gladiator.png'
    spriteSize = 32
    damagingSprite = [4]
    num_sprintes = {'idleRight' : 5, "idleLeft": 5, 'runRight' : 8, 'runLeft' : 8, 'attackRight' : 7, 'attackLeft' : 7, 'die' : 7}
    zoom = 2
    dps = damage*len(damagingSprite)/ (0.5/attackSpeed*num_sprintes["attackRight"])
    purse = hp/5+dps*1.5+speed

class Totor (Ennemy):
    __slots__ = ("idle", "runRight",
                "runLeft", "attackRight", "attackLeft", "death")

    hp = 250 * coeffv
    name = "Totor"
    attackSpeed = 2
    speed = 1
    damage = 20


    spritesheet = 'view/src/personnage/ennemis/Totor.png'
    spriteSize = 96
    y_Anim = {"idleRight" : 0, "idleLeft" : 960, "runRight" : 96, "runLeft" : 96*12, "attackRight": 96*3, "attackLeft": 96*13, "die" : 96*9}
    damagingSprite = [1,3]
    num_sprintes = {"idleRight" : 5, "idleLeft": 5, "runRight" : 8, "runLeft" : 8, "attackRight" : 9, "attackLeft": 9, "die": 6}
    zoom = 2
    dps = damage*len(damagingSprite)/ (0.5/attackSpeed*num_sprintes["attackRight"])
    purse = hp/5+dps*1.5+speed

class Fat_Totor (Totor) :
    hp = 750 * coeffv
    name = "Fat Totor"
    damage = 40
    speed = 1
    zoom = 3
    
    num_sprintes = {"idleRight" : 5, "idleLeft": 5, "runRight" : 8, "runLeft" : 8, "attackRight" : 9, "attackLeft": 9, "die": 6}
    attackSpeed = 1
    damagingSprite = [1,3]
    dps = damage*len(damagingSprite)/ (0.5/attackSpeed*num_sprintes["attackRight"])
    purse = hp/5+dps*1.5+speed

class RedGladiator(Gladiator):
    __slots__ = ('idle', 'runRight', 'runLeft', 'attackRight', 'attackLeft', "death")
    y_Anim = {'idleRight' : 0, "idleLeft": 32*5, 'runRight' : 32, 'runLeft' : 32*6, 'attackRight' : 32*2, 'attackLeft' : 32*7, 'die' : 32*4}

    hp = 500
    name = 'RedGladiator'
    speed = 1
    attackSpeed = 1
    damage = 30

    spritesheet = 'view/src/personnage/ennemis/RedGladiator.png'
    spriteSize = 32
    damagingSprite = [4]
    num_sprintes = {'idleRight' : 5, "idleLeft": 5, 'runRight' : 8, 'runLeft' : 8, 'attackRight' : 7, 'attackLeft' : 7, 'die' : 7}
    zoom = 2
    dps = damage*len(damagingSprite)/ (0.5/attackSpeed*num_sprintes["attackRight"])
    purse = hp/5+dps*1.5+speed
