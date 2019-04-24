import tkinter as tk
import controller.Interface as View
import model.Tower as Tow
import model.Heros as He
from model.Ennemy import *
from model.fonctions_utiles import subimage

# Classe des emplacement stockants les données pour l'interface
class Emplacement():
    bonus = {}
    state = None
    tower = None
    last_img = None
    
    # Utilisation des arguments accessoires pour ajouter des tours supplémentaires
    def __init__(self, x, y, *args, **kwargs):
        state = kwargs.get('state', None)
        bonus = kwargs.get('bonus', None)

        self.x = x
        self.y = y

        if state:
            self.state = state
        if bonus:
            self.bonus = bonus

# Classe des niveaux 
class Lvl(tk.Frame):
    # Définiton des variables de chaque niveau
    heros = None
    ennemies = []
    spots = []

    image = None

    def __init__(self, parent, *args, **kwargs):
        # On récupère le heros choisi
        selectedHeros = kwargs.get('heros', None)

        # Défintion de l'arrière plan du niveau
        self.backImg = tk.PhotoImage(file=self.image)

        # Définition des dimensions de la fenêtre
        self.rootWidth = self.backImg.width()
        self.rootHeight = self.backImg.height()

        # Instance de la Frame
        tk.Frame.__init__(self, parent)

        # Chargement de l'animation des tours
        self.upImage = "view/src/Storm_evolution.png"
        self.upAnim = [subimage(self.upImage, 200*i, 0, 200*(i+1), 200)
                       for i in range(6)]

        # Chargement du canvas
        self.canvas = tk.Canvas(self, width=self.rootWidth,
                                height=self.rootHeight, highlightthickness=0)

        # Affichage de l'arrière plan 
        self.canvas.create_image(0, 0, image=self.backImg, anchor="nw")

        # Défintion de l'argent et de la vie
        self.gold = tk.IntVar(self.canvas, self.gold)
        self.health = tk.IntVar(self.canvas, 20)

        # Chargement du Héros
        if selectedHeros == "Ichigo":
            self.heros = He.Ichigo(self, 900, 250, 260, 160)
        elif selectedHeros == "Goku":
            self.heros = He.Goku(self, 900, 250, 260, 160)
        else:
            self.heros = He.Adventurer(self, 900, 250, 260, 160)

        # Lancement des Vagues
        self.launchWaves()

        # Début de l'interface
        self.interface = View.Interface(self)

        # Bind des évenèments utilisateurs 
        self.canvas.bind("<Button-1>", self.interface.selectSpot)
        self.canvas.bind("<Button-3>", self.heros.mouseMove)
        self.canvas.bind_all("t", self.heros.specialAttack)

        # Pack des canvas pour affichage
        self.interface.pack(side="right", fill="y")
        self.canvas.pack(side="right", fill='both', expand=True)

    # Fonction annexe permettant de quadriller le niveau
    def makeLigns(self):
        # ---------------Définition des lignes---------------
        # Variable permmetant de définir la grille de la map
        squareFactor = 3
        squareHeight = int(30 * squareFactor)
        squareWidth = int(18 * squareFactor)
        showSquare = False

        # Mise en place de la grid de la map
        if showSquare:
            for i in range(squareHeight):
                self.canvas.create_line((i+1)*self.rootWidth/squareHeight, 0, (i+1)
                                        * self.rootWidth/squareHeight, self.rootHeight, stipple="gray50")
            for i in range(squareWidth):
                self.canvas.create_line(0, (i+1)*self.rootHeight/squareWidth, self.rootWidth,
                                        (i+1)*self.rootHeight/squareWidth, stipple="gray50")

    # Fonction nulle contenant dans les autress niveaux les ennemis à charger
    def launchWaves(self):
        pass

    # Fonction permettant de détruire chaquen entitée chargée par le niveau
    def __del__(self):
        for ennemy in self.ennemies:
            del ennemy
        for el in self.__dict__:
            del el

# Classe du menu principal
class MainMenu(tk.Frame):
    def __init__(self, parent, *args, **kwargs):

        # Définiton des variables
        self.backImg = tk.PhotoImage(file="view/src/MainMenu.png")
        self.rootWidth = self.backImg.width()
        self.rootHeight = self.backImg.height()

        # Instance de la Frame
        tk.Frame.__init__(self, parent)

        # Reste du GUI
        self.canvas = tk.Canvas(self, width=self.rootWidth,
                                height=self.rootHeight, highlightthickness=0)
        self.canvas.create_image(0, 0, image=self.backImg, anchor="nw")


# -----------------Chargement de la Frame LVL 1 ----------------------
class Lvl1(Lvl):
    image = "view/src/Lvl1Background.png"
    gold = 1000

    spots = [Emplacement(180, 175),
             Emplacement(358, 175),
             Emplacement(574, 175),
             Emplacement(755, 175),
             Emplacement(791, 355),
             Emplacement(538, 355),
             Emplacement(323, 355),
             Emplacement(143, 355, state="Mine")]

    def launchWaves(self):
        Skeleton(self, 0, 225, self.heros)
        Skeleton(self, -100, 225, self.heros)
        Skeleton(self, -50, 225, self.heros)
        Skeleton(self, -150, 225, self.heros)
        Skeleton(self, 50, 225, self.heros)

# -----------------Chargement de la Frame LVL 2 ----------------------


class Lvl2(Lvl):
    image = "view/src/Lvl2Background.png"
    gold = 1000

    spots = [Emplacement(180, 175),
             Emplacement(358, 175),
             Emplacement(574, 175),
             Emplacement(755, 175),
             Emplacement(791, 355),
             Emplacement(538, 355),
             Emplacement(323, 355),
             Emplacement(143, 355, state="Mine")]

    def launchWaves(self):
        Skeleton(self, 0, 225, self.heros)
        Skeleton(self, -100, 225, self.heros)
        Skeleton(self, -50, 225, self.heros)
        Skeleton(self, -150, 225, self.heros)
        Skeleton(self, 50, 225, self.heros)

# -----------------Chargement de la vue principale--------------------
class MainApplication(tk.Frame):
    currentFrame = None

    def __init__(self, parent, *args, **kwargs):
        # Instance de la Frame
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Chargement de la Frame de départ
        self.switchFrame(Lvl1)

    # Fonction permettant de passer d'une frame à l'autre en détruisant l'autre
    def switchFrame(self, nframe):
        nlevel = nframe(self, self.parent, heros="Goku")
        if self.currentFrame:
            self.currentFrame.destroy()
            del self.currentFrame

        self.currentFrame = nlevel
        self.currentFrame.pack(side="top", fill="both", expand=True)

    # def launchLvl2(self):
    #     self.switchFrame(Lvl2)


# -----------------Fonction à executer pour lancer le jeu-------------
def launchApp():
    root = tk.Tk()

    MainApplication(root).pack(side="top", fill="both", expand=True)

    root.title("Tower Run")
    root.resizable(False, False)
    root.mainloop()
