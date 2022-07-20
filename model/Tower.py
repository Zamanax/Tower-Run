import tkinter as tk
from threading import Thread
from model.Heros import Heros
from model.State import State
from model.fonctions_utiles import *  # pylint: disable=unused-wildcard-import
import time

# ---------------------------------------------------------------------------------------------------


class Tower(Thread):
    """Classe abstraite dont vont hériter les autres tours"""

    lvl = 1         # niveau de la tour
    last_storm = None
    last_img = None   # attributs pour les images
    seeking = None
    indice = 0
    target = None
    range = 0  # portée de tir
    dernier_tir = None
    speed = 3  # cadence de tir
    zone = -1  # zone de dégats si explosion

    d_up = 50
    r_up = 25
    damage = 1
    damage_evo = [1, 2, 3]
    # variables pour les changement de stats en fonction des niveaux
    range_evo = [range, range+r_up, range+r_up*2]
    speed_evo = [speed, speed+2, speed+6]
    price_evo = [0, 0, 0]

    def __del__(self):
        for el in self.__dict__:
            del el

    def __init__(self, parent, x, y, projectile):
        Thread.__init__(self)  # On thread chaque tour
        self.start()

        self.parent = parent  # le niveau
        self.projectile = projectile  # le projectile
        self.canvas = parent.canvas  # canvas
        self.x = x
        self.y = y

        self.damage = self.damage_evo[0]  # dégâts
        self.price = self.price_evo[1]
        self.ndamage = self.damage_evo[1]
        # variables pour la prévision des valeurs des niveaux suivants
        self.nrange = self.range_evo[1]
        self.nspeed = self.speed_evo[1]

        self.construction()
        self.seek()

    def show_evol(self):
        """Méthode chargée d'afficher la tornade en construction et en upgrade sur les tours"""

        spritenum = len(self.parent.upAnim)
        self.canvas.delete(self.last_storm)
        self.last_storm = self.canvas.create_image(
            self.x, self.y-30, image=self.parent.upAnim[self.indice])

        if self.indice == 2:  # à la 2e image
            if not self.lvl == 1:  # si on n'est pas en train de construire; c-a-d si on est en train d'améliorer
                # on efface  l'image de la tour du niveau inférieur
                self.canvas.delete(self.last_img)

        if self.indice == 3:  # à la 3e image
            # On place la nouvelle
            if self.lvl == 1:
                self.last_img = self.canvas.create_image(
                    self.x, self.y, image=self.lv1)

            elif self.lvl == 2 and str(self) != "Forgeron":
                self.last_img = self.canvas.create_image(
                    self.x, self.y-20, image=self.lv2)

            elif self.lvl == 2 and str(self) == "Forgeron":
                self.last_img = self.canvas.create_image(
                    self.x, self.y, image=self.lv2)

            elif self.lvl == 3 and str(self) != "Forgeron":
                self.last_img = self.canvas.create_image(
                    self.x, self.y-35, image=self.lv3)

            elif self.lvl == 3 and str(self) == "Forgeron":
                self.last_img = self.canvas.create_image(
                    self.x, self.y, image=self.lv3)

            # On la place au dessus du canvas de niveau
                self.canvas.tag_raise(self.last_img)

        self.indice += 1  # on incrémente l'indice de l'image

        if self.indice == spritenum:  # à la fin de l'animation
            self.indice = 0  # on réinitialise l'indice d'animation

            self.canvas.delete(self.last_storm)
            return
        self.canvas.after(150, self.show_evol)  # fonction récurssive

    def construction(self):
        self.show_evol()

    def upgrade(self):
        # wrapper des fonctions d'upgrade
        if self.lvl == 1:
            self.upgrade1()
        elif self.lvl == 2:
            self.upgrade2()

    def upgrade1(self):
        self.lvl = 2  # changment de niveau

        self.damage = self.damage_evo[1]
        self.ndamage = self.damage_evo[2]
        self.range = self.range_evo[1]  # chargement des nouvelles stats et des
        self.nrange = self.range_evo[2]  # stats du niveau d'après
        self.speed = self.speed_evo[1]
        self.nspeed = self.speed_evo[2]
        self.price = self.price_evo[2]

        self.show_evol()  # appel à l'affichage de transformation

    def upgrade2(self):
        self.lvl = 3

        self.damage = self.damage_evo[2]
        self.ndamage = "Max"
        self.range = self.range_evo[2]  # IDEM
        self.nrange = "Max"
        self.speed = self.speed_evo[2]
        self.nspeed = "Max"
        self.price = "Max"

        self.show_evol()

    def seek(self):
        """Méthode chargée de rechercher les ennemis à attaquer"""

        if self.target == None:
            ennemies = self.parent.ennemies  # liste des ennemis sur le niveau
            for ennemy in ennemies:
                if (((ennemy.x-self.x)**2)+((ennemy.y-self.y)**2))**0.5 <= self.range and ennemy.state != State.Die:

                    self.target = ennemy
                    try:
                        self.canvas.after_cancel(self.seeking)
                    except ValueError:
                        pass
                    self.tir_p()
                    self.ciblage()
                    return  # si l'ennemi n'est pas mort et qu'il est dans la portée de tir
                    # On le cible, on tir, et on arrête de chercher
            self.seeking = self.canvas.after(
                250, self.seek)  # sinon on recherche

    def ciblage(self):
        if self.target != None:  # si un ennemi est ciblé

            # si l'ennemi sort de la portée de tir
            if ((self.x - self.target.x)**2+(self.y - self.target.y)**2)**0.5 >= self.range:
                self.target = None  # on n'a plus de cible
                self.canvas.after_cancel(self.firing)
                self.canvas.after_cancel(self.ciblement)
                self.canvas.after(int(
                    10000/self.speed-(time.time()-self.dernier_tir)*1000), self.seek)  # on recherche
                return
        self.ciblement = self.canvas.after(50, self.ciblage)

    def tir_p(self):
        """fonction qui 'tire' le projectile"""
        if self.target != None:
            self.projectile(self)
            self.dernier_tir = time.time()
            self.firing = self.canvas.after(int(10000/self.speed), self.tir_p)

# Classe projectile permattant de leur affecter des méthodes


class Projectile(Thread):
    """classe abstraite des projectiles lancés par les tours"""

    damage = 0
    boomboom = True
    target = None
    seeking = None  # attributs de chargement d'images
    corps = None

    # Méthode chargée de l'apparition du projectile
    def __init__(self, tour, image, boom):
        Thread.__init__(self)
        self.start()  # Thread
        # print("projectile initialisé")
        self.zone = tour.zone
        self.tour = tour
        self.x = tour.x-5
        self.y = tour.y-70  # coordonnées
        self.boomname = boom
        self.img = tk.PhotoImage(file=image)
        self.boom = tk.PhotoImage(file=boom)  # Prép des images

        self.canvas = tour.canvas  # chargement des canvas
        self.damage = self.tour.damage
        self.target = tour.target
        self.tx = self.tour.target.x  # on prend les coordonnées de la cible à un moment donné
        self.ty = self.tour.target.y

        self.v = 5  # un coefficient en pixel pour le déplacement du projectile
        self.mininit()
        self.traj()  # on fait un calcul de trajectoire

    def mininit(self):
        pass

    def traj(self):
        # distance tour-ennemie divisée par le nombre de pixel de déplacement par coup
        n_coups = int((((self.x-self.tx)**2+(self.y-self.ty)**2)**0.5)/self.v)
        self.inc_abs = -(self.x-self.tx)/n_coups
        self.inc_ord = -(self.y-self.ty)/n_coups
        self.tir()
        # tir!

    # Méthode chargée du déplacement des projectiles
    def tir(self):
        # s'il y a une image de projectile sur le canvas
        if type(self.corps) != None and self.boomboom:
            self.canvas.delete(self.corps)  # on supprime

        if self.tx-10 <= self.x <= self.tx+10 and self.ty-16 <= self.y <= self.ty+16:  # si le projectile touche l'ennemi
            # on efface l'image
            self.corps = self.canvas.create_image(
                self.x, self.y, image=self.boom)  # on met l'image d'impact
            self.boomboom = False

            to_hit = []
            if self.zone != -1:
                for ennemy in self.tour.parent.ennemies:  # toute la partie de l'explosion
                    if (((ennemy.x-self.x)**2)+((ennemy.y-self.y)**2))**0.5 < self.zone and ennemy.state != State.Die:
                        to_hit.append(ennemy)
            else:
                to_hit.append(self.target)

            for cible in to_hit:
                if (cible.__class__.__name__ == "SlimeE" and self.__class__.__name__ == 'BouleDeFeu') or (cible.__class__.__name__ == "SlimeF" and self.__class__.__name__ == 'LameDEau') or (cible.__class__.__name__ == "SlimeW" and self.__class__.__name__ == 'Boulet'):
                    cible.hp -= 2*self.tour.damage
                else:  # Partie coup critique élémentaire
                    cible.hp -= self.tour.damage

            for cible in to_hit[1:len(to_hit)-1]:
                if cible.hp <= 0:
                    cible.die(False)

            if self.target.hp <= 0:
                self.target.die(False)
                self.tour.target = None
                self.canvas.after_cancel(self.tour.firing)
                self.canvas.after_cancel(self.tour.ciblement)
                try:
                    self.canvas.after_cancel(self.tour.seeking)
                except ValueError:
                    pass
                self.canvas.after(int(
                    10000/self.tour.speed-(time.time()-self.tour.dernier_tir)*1000), self.tour.seek)
                return

            # self.canvas.after(20, self.canvas.delete, self.corps)
            self.canvas.after_cancel(self.feufeufeu)
            return

        self.x += self.inc_abs  # on incrémente les coordonnés du projectile
        self.y += self.inc_ord

        self.corps = self.canvas.create_image(self.x, self.y, image=self.img)
        self.feufeufeu = self.canvas.after(20, self.tir)  # récurssion

# ----------------------------------------------------------------------------------------------------

# Classes des mortiers, archers, mages... basés sur le même template que les autres


class Mortier(Tower):
    coordsLvl1 = [16, 54, 85, 142]
    # coordonnées des images des différents niveaux dans la sprite sheet
    coordsLvl2 = [91, 30, 191, 142]
    coordsLvl3 = [203, 3, 313, 142]
    image = "view/src/tours/tours/Mortier.png"

    range = 100  # attributs
    speed = 1
    zone = 80
    r_up = 20

    damagetype = "explosion"  # type de dégâts

    damage_evo = [30, 37.5, 67.5]
    range_evo = [range, range+r_up, range+r_up*2]
    speed_evo = [speed, speed+1, speed+2]
    price_evo = [250, 500, 1250]
    price = price_evo[0]
    damage = damage_evo[0]

    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()

        self.lv1 = load(self.coordsLvl1, self.image)
        self.lv2 = load(self.coordsLvl2, self.image)
        self.lv3 = load(self.coordsLvl3, self.image)
        Tower.__init__(self, canvas, x, y-5, Boulet)

    def __str__(self):
        return "Mortier"


class FireM(Tower):

    coordsLvl1 = [3, 72, 69, 129]
    coordsLvl2 = [91, 49, 191, 139]
    coordsLvl3 = [203, 3, 313, 141]
    image = "view/src/tours/tours/Mage2.png"
    speed = 3
    zone = -1
    range = 120
    r_up = 30
    d_up = 10
    damagetype = "fire"
    damage_evo = [20, 30, 54]
    range_evo = [range, range+r_up, range+r_up*2]
    speed_evo = [speed, speed+1, speed+2]
    price_evo = [175, 350, 875]
    price = price_evo[0]
    damage = damage_evo[0]

    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        self.lv1 = load(self.coordsLvl1, self.image)
        self.lv2 = load(self.coordsLvl2, self.image)
        self.lv3 = load(self.coordsLvl3, self.image)
        Tower.__init__(self, canvas, x, y, BouleDeFeu)

        # self.spritesheet=tk.PhotoImage(file="Mage2.png")

        # self.root.mainloop()

    def __str__(self):
        return "Mage de Feu"


class WaterM(Tower):
    coordsLvl1 = [3, 72, 82, 139]
    coordsLvl2 = [91, 47, 195, 139]
    coordsLvl3 = [203, 0, 323, 139]
    image = "view/src/tours/tours/Mage3.png"
    speed = 3
    zone = -1
    range = 120
    damagetype = "water"
    d_up = 10
    r_up = 30
    damage_evo = [20, 30, 54]
    range_evo = [range, range+r_up, range+r_up*2]
    speed_evo = [speed, speed+1, speed+2]
    price_evo = [175, 350, 875]
    price = price_evo[0]
    damage = damage_evo[0]

    def __init__(self, parent, x, y):
        self.lv1 = load(self.coordsLvl1, self.image)
        self.lv2 = load(self.coordsLvl2, self.image)
        self.lv3 = load(self.coordsLvl3, self.image)
        Tower.__init__(self, parent, x, y, LameDEau)

    def __str__(self):
        return "Mage d'Eau"


class EarthM(Tower):
    image = "view/src/tours/tours/Mage1.png"
    coordsLvl1 = [3, 62, 82, 132]
    coordsLvl2 = [91, 47, 195, 132]
    coordsLvl3 = [203, 0, 323, 132]
    speed = 3
    zone = -1
    range = 120
    damagetype = "earth"
    d_up = 10
    r_up = 30
    damage_evo = [20, 30, 54]
    range_evo = [range, range+r_up, range+r_up*2]
    speed_evo = [speed, speed+1, speed+2]
    price_evo = [175, 350, 875]
    price = price_evo[0]
    damage = damage_evo[0]

    def __init__(self, parent, x, y):

        self.lv1 = load(self.coordsLvl1, self.image)
        self.lv2 = load(self.coordsLvl2, self.image)
        self.lv3 = load(self.coordsLvl3, self.image)
        Tower.__init__(self, parent, x-8, y, Caillou)

    def __str__(self):
        return "Mage de Terre"


class Archer(Tower):
    image = "view/src/tours/tours/Archer.png"
    coordsLvl1 = [3, 51, 82, 138]
    coordsLvl2 = [91, 35, 195, 144]
    coordsLvl3 = [203, 0, 295, 144]
    range = 200
    speed = 5
    zone = -1
    damagetype = "shot"
    d_up = 5
    r_up = 35
    damage_evo = [15, 22.5, 40.5]
    range_evo = [range, range+r_up, range+r_up*2]
    speed_evo = [speed, speed+2, speed+4]
    price_evo = [175, 350, 875]
    price = price_evo[0]
    damage = damage_evo[0]

    def __init__(self, parent, x, y):

        self.lv1 = load(self.coordsLvl1, self.image)
        self.lv2 = load(self.coordsLvl2, self.image)
        self.lv3 = load(self.coordsLvl3, self.image)
        Tower.__init__(self, parent, x+3, y-10, Fleche)

    def __str__(self):
        return "Archer"


class Forgeron(Tower):
    zone = None
    coordsLvl1 = [0, 0, 120, 115]
    coordsLvl2 = [125, 0, 250, 115]
    coordsLvl3 = [250, 0, 380, 115]
    image = 'view/src/tours/tours/Forgeron.png'
    price_evo = [400, 700, 1200]
    price = price_evo[0]

    def __init__(self, parent, x, y):
        self.lv1 = load(self.coordsLvl1, self.image)
        self.lv2 = load(self.coordsLvl2, self.image)
        self.lv3 = load(self.coordsLvl3, self.image)
        self.hero = parent.heros
        Tower.__init__(self, parent, x, y-20, 0)

    def seek(self):
        pass

    def ciblage(self):
        pass

    def tir_p(self):
        pass

    def construction(self):
        Tower.construction(self)
        self.hero.transform()

    def upgrade1(self):
        self.lvl = 2
        self.price = self.price_evo[2]
        self.show_evol()
        self.hero.transform()

    def upgrade2(self):
        self.lvl = 3
        self.price = "Max"
        self.show_evol()
        self.hero.transform()

    def __str__(self):
        return "Forgeron"


class Mine(Tower):
    coordsLvl1 = [13, 13, 148, 110]
    coordsLvl2 = [165, 8, 289, 120]
    coordsLvl3 = [334, 5, 486, 125]
    image = 'view/src/tours/tours/Mine.png'
    price_evo = [0, 800, 1500]
    production = 0

    def __init__(self, parent, x, y):
        # self.root=tk.Tk()
        #test_subimage(self.image, 3, 51, 82, 138, self.root)
        self.lv1 = load(self.coordsLvl1, self.image)
        self.lv2 = load(self.coordsLvl2, self.image)
        self.lv3 = load(self.coordsLvl3, self.image)
        self.parent = parent
        Tower.__init__(self, parent, x, y, 0)

    def produce(self):
        self.parent.gold.set(self.parent.gold.get()+self.production)
        self.parent.interface.preView()
        self.canvas.after(5000, self.produce)

    def seek(self):
        pass

    def ciblage(self):
        pass

    def tir_p(self):
        pass

    def upgrade2(self):
        self.lvl = 3
        self.production = 100
        self.show_evol()

    def upgrade1(self):
        self.lvl = 2
        self.production = 50
        self.produce()
        self.show_evol()

    def __str__(self):
        return "Mine"

    def __name__(self):
        return self.__str__()


class Boulet(Projectile):
    def __init__(self, tour):
        Projectile.__init__(self, tour, "view/src/tours/projectile/bouletDeCanon.png",
                            "view/src/tours/projectile/kaboom.png")


class BouleDeFeu(Projectile):
    def __init__(self, tour):
        Projectile.__init__(self, tour, "view/src/tours/projectile/flamèche.png",
                            "view/src/tours/projectile/flamèche.png")


class LameDEau(Projectile):
    def __init__(self, tour):
        Projectile.__init__(self, tour, "view/src/tours/projectile/petit shuriken eau.png",
                            "view/src/tours/projectile/petit shuriken eau.png")


class Caillou(Projectile):
    def __init__(self, tour):
        Projectile.__init__(self, tour, "view/src/tours/projectile/caillou.png",
                            "view/src/tours/projectile/caillou.png")


class Fleche(Projectile):
    def __init__(self, tour):
        Projectile.__init__(self, tour, "view/src/tours/projectile/flèche gh.png",
                            "view/src/tours/projectile/flèche gh.png")

    def mininit(self):
        if self.tx <= self.x and self.ty <= self.y:
            self.img = tk.PhotoImage(
                file="view/src/tours/projectile/flèche gh.png")
        elif self.tx >= self.x and self.ty >= self.y:
            self.img = tk.PhotoImage(
                file="view/src/tours/projectile/flèche db.png")
        elif self.tx >= self.x and self.ty <= self.y:
            self.img = tk.PhotoImage(
                file="view/src/tours/projectile/flèche dh.png")
        elif self.tx <= self.x and self.ty >= self.y:
            self.img = tk.PhotoImage(
                file="view/src/tours/projectile/flèche gb.png")
        self.boom = self.img
        self.v = 4
