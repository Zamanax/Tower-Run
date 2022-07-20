import tkinter as tk
import controller.Interface as View
import model.Tower as Tow
from model.herostats import *
from model.Ennemy import *
from model.fonctions_utiles import subimage
import tkinter.ttk as ttk
from threading import Thread
import asyncio
import os

# Classe des emplacement stockants les données pour l'interface


class keySpot():
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Rectangle():
    def __init__(self, min_x, max_x, min_y, max_y):
        self.min_x = min_x
        self.max_x = max_x
        self.min_y = min_y
        self.max_y = max_y


class Emplacement(keySpot):
    bonus = {}
    state = None
    tower = None
    last_img = None

    # Utilisation des arguments accessoires pour ajouter des tours supplémentaires
    def __init__(self, x, y, *args, **kwargs):
        keySpot.__init__(self, x, y)
        state = kwargs.get('state', None)
        bonus = kwargs.get('bonus', None)

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
    lost = None

    wave1 = []
    waveIndex = 0

    def __init__(self, parent, *args, **kwargs):
        self.parent = parent

        # On récupère le heros choisi
        selectedHeros = kwargs.get('heros', None)
        # Défintion de l'arrière plan du niveau
        self.backImg = tk.PhotoImage(file=self.image)
        self.gagne = tk.PhotoImage(file="view/src/background/Win.png")
        self.perdu = tk.PhotoImage(file="view/src/background/Lose.png")

        # Définition des dimensions de la fenêtre
        self.rootWidth = self.backImg.width()
        self.rootHeight = self.backImg.height()

        # Instance de la Frame
        tk.Frame.__init__(self, parent)

        # Chargement de l'animation des tours
        self.upImage = "view/src/assets/Storm_evolution.png"
        self.upAnim = [subimage(self.upImage, 200*i, 0, 200*(i+1), 200)
                       for i in range(6)]

        # Chargement du canvas
        self.canvas = tk.Canvas(self, width=self.rootWidth,
                                height=self.rootHeight, highlightthickness=0)

        # Affichage de l'arrière plan
        self.background = self.canvas.create_image(
            0, 0, image=self.backImg, anchor="nw")

        # Défintion de l'argent et de la vie
        self.gold = tk.IntVar(self.canvas, self.gold)
        self.health = tk.IntVar(self.canvas, 5)

        # Chargement du Héros
        if hasattr(selectedHeros, "name"):
            self.heros = selectedHeros
            self.heros.x = 900
            self.heros.y = 250
            self.heros.canvas = self.canvas
            self.heros.parent = self
        else:
            if selectedHeros == "Ichigo":
                self.heros = Ichigo(
                    self, 900, 250, quality=self.parent.quality)
            elif selectedHeros == "Goku":
                self.heros = Goku(self, 900, 250, quality=self.parent.quality)
            else:
                self.heros = Adventurer(self, 900, 250)
        self.parent.heros = self.heros
        # Lancement des Vagues
        self.launchWaves(self.wave1)

        # Début de l'interface
        self.interface = View.Interface(self)

        # Bind des évenèments utilisateurs
        self.canvas.bind("<Button-1>", self.interface.selectSpot)
        self.canvas.bind("<Button-3>", self.heros.mouseMove)
        self.canvas.bind("<Button-2>", self.heros.instantMove)
        self.canvas.bind_all("<space>", self.heros.specialAttack)
        self.canvas.bind_all("<KeyPress-Right>", self.heros.reOrient)
        self.canvas.bind_all("<KeyPress-Left>", self.heros.reOrient)

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

    def winGame(self):
        nb = 0
        for ennemy in self.ennemies:
            if ennemy.state == State.Die:
                nb += 1
        # and self.parent.waveIndex == len(self.parent.waveDict) -1:
        if nb == len(self.ennemies) and self.waveIndex == len(self.waveDict):
            self.win = self.canvas.create_image(540, 325, image=self.gagne)

            self.restartBtn = tk.Button(
                self.canvas, text="Restart", command=self.restartGame)
            self.restartBtn.place(x=400, y=450)

            self.nextLvlBtn = tk.Button(
                self.canvas, text="Next Level", command=self.launchNextLvl)
            self.nextLvlBtn.place(x=600, y=450)

    def loseGame(self):
        self.lost = self.canvas.create_image(540, 325, image=self.perdu)
        self.restartBtn = tk.Button(
            self.canvas, text="Restart", command=self.restartGame)
        self.restartBtn.place(x=500, y=400)

    def restartGame(self):
        self.heros.reset()
        self.parent.switchFrame(self.__class__)

    def launchNextLvl(self):
        self.heros.reset()
        self.parent.switchFrame(self.nextLvl)

    def launchWaves(self, dict):
        for i in range(len(dict)):
            dict[i](self, -50*i, self.spawnPoint.y)
        self.waveIndex += 1

    def nextWave(self):
        if self.waveIndex <= len(self.waveDict) - 1:
            self.launchWaves(self.waveDict[self.waveIndex])

    # Fonction permettant de détruire chaque entitée chargée par le niveau
    def __del__(self):
        for ennemy in self.ennemies:
            del ennemy
        for el in self.__dict__:
            del el

# -----------------Chargement de la Frame LVL 3 ----------------------


class Lvl3(Lvl):
    image = "view/src/background/Lvl3Background.png"
    gold = 500
    defaultPath = [keySpot(410, 175),
                   keySpot(410, 520),
                   keySpot(730, 520),
                   keySpot(730, 175),
                   keySpot(1200, 175)]

    spawnPoint = keySpot(0, 175)

    wave1 = [miniSkeleton, Skeleton, miniSkeleton, miniSkeleton,
             Bat, Skeleton, miniSkeleton, miniSkeleton, miniSkeleton, Bat]
    wave2 = [miniSkeleton, Skeleton, miniSkeleton,
             SlimeE, SlimeW, SlimeF, Skeleton, Skeleton]
    wave3 = [SlimeE, SlimeW, SlimeF, SlimeE,
             SlimeW, SlimeF, Skeleton, miniSkeleton]
    wave4 = [Gladiator, SlimeE, SlimeW, SlimeF, Skeleton, RedGladiator]
    wave5 = [Fat_Totor, Gladiator, SlimeE, SlimeW, SlimeF]
    wave6 = [Bat, Bat, Totor, SlimeE, SlimeW, SlimeF, Totor]
    wave7 = [Fat_Totor, RedGladiator, SlimeE, SlimeW, SlimeF, RedGladiator]
    wave8 = [Fat_Totor, SlimeE, SlimeW, SlimeF, Fat_Totor]
    wave9 = [Fat_Totor, Gladiator, Fat_Totor, Gladiator, Fat_Totor]

    waveDict = [wave1, wave2, wave3, wave4, wave5, wave6, wave7, wave8, wave9]

    authorized = [Rectangle(0, 465, 120, 220),
                  Rectangle(350, 790, 120, 570),
                  Rectangle(680, 1200, 120, 220)]

    def __init__(self, parent, *args, **kwargs):
        self.spots = [Emplacement(50, 280),
                      Emplacement(180, 280),
                      Emplacement(300, 280),
                      Emplacement(315, 385),
                      Emplacement(510, 180),
                      Emplacement(635, 180),
                      Emplacement(510, 390),
                      Emplacement(635, 390),
                      Emplacement(840, 280),
                      Emplacement(960, 280),
                      Emplacement(840, 385),
                      Emplacement(840, 485)]
        super().__init__(parent, *args, **kwargs)

# -----------------Chargement de la Frame LVL 2 ----------------------


class Lvl2(Lvl):
    image = "view/src/background/Lvl2Background.png"
    gold = 500
    defaultPath = [keySpot(1200, 225)]

    wave1 = [miniSkeleton, Skeleton, miniSkeleton, miniSkeleton,
             Bat, Skeleton, miniSkeleton, miniSkeleton, miniSkeleton, Bat]
    wave2 = [miniSkeleton, Skeleton, miniSkeleton,
             SlimeE, SlimeW, SlimeF, Skeleton, Skeleton]
    wave3 = [SlimeE, SlimeW, SlimeF, SlimeE,
             SlimeW, SlimeF, Skeleton, miniSkeleton]
    wave4 = [Gladiator, SlimeE, SlimeW, SlimeF, Skeleton, RedGladiator]
    wave5 = [Fat_Totor, Gladiator, SlimeE, SlimeW, SlimeF]
    wave6 = [Bat, Bat, Totor, SlimeE, SlimeW, SlimeF, Totor]
    wave7 = [Fat_Totor, RedGladiator, SlimeE, SlimeW, SlimeF, RedGladiator]
    wave8 = [Fat_Totor, SlimeE, SlimeW, SlimeF, Fat_Totor]
    wave9 = [Fat_Totor, Gladiator, Fat_Totor, Gladiator, Fat_Totor]

    waveDict = [wave1, wave2, wave3, wave4, wave5, wave6, wave7, wave8, wave9]

    nextLvl = Lvl3

    authorized = [Rectangle(0, 385, 150, 550),
                  Rectangle(385, 1200, 170, 250),
                  Rectangle(385, 455, 170, 550),
                  Rectangle(385, 1200, 470, 550)]

    spawnPoint = keySpot(0, 200)

    def __init__(self, parent, *args, **kwargs):
        self.spots = [Emplacement(60, 150),
                      Emplacement(200, 150),
                      Emplacement(285, 150),
                      Emplacement(570, 335),
                      Emplacement(660, 335),
                      Emplacement(750, 335),
                      Emplacement(860, 335),
                      Emplacement(975, 335),
                      Emplacement(525, 610),
                      Emplacement(635, 610),
                      Emplacement(750, 610),
                      Emplacement(850, 610),
                      Emplacement(955, 610),
                      Emplacement(55, 375),
                      Emplacement(230, 375)]
        super().__init__(parent, *args, **kwargs)

# -----------------Chargement de la Frame LVL 1 ----------------------


class Lvl1(Lvl):
    image = "view/src/background/Lvl1Background.png"
    gold = 500
    defaultPath = [keySpot(1200, 225)]

    wave1 = [miniSkeleton, Skeleton, miniSkeleton, miniSkeleton,
             Bat, Skeleton, miniSkeleton, miniSkeleton, miniSkeleton, Bat]
    wave2 = [miniSkeleton, Skeleton, miniSkeleton,
             SlimeE, SlimeW, SlimeF, Skeleton, Skeleton]
    wave3 = [SlimeE, SlimeW, SlimeF, SlimeE,
             SlimeW, SlimeF, Skeleton, miniSkeleton]
    wave4 = [Gladiator, SlimeE, SlimeW, SlimeF, Skeleton, RedGladiator]
    wave5 = [Fat_Totor, Gladiator, SlimeE, SlimeW, SlimeF]
    wave6 = [Bat, Bat, Totor, SlimeE, SlimeW, SlimeF, Totor]
    wave7 = [Fat_Totor, RedGladiator, SlimeE, SlimeW, SlimeF, RedGladiator]
    wave8 = [Fat_Totor, SlimeE, SlimeW, SlimeF, Fat_Totor]
    wave9 = [Fat_Totor, Gladiator, Fat_Totor, Gladiator, Fat_Totor]

    waveDict = [wave1, wave2, wave3, wave4, wave5, wave6, wave7, wave8, wave9]

    nextLvl = Lvl2

    authorized = [Rectangle(0, 1200, 160, 260)]

    spawnPoint = keySpot(0, 200)

    def __init__(self, parent, *args, **kwargs):
        self.spots = [Emplacement(180, 150),
                      Emplacement(358, 150),
                      Emplacement(574, 150),
                      Emplacement(755, 150),
                      Emplacement(791, 302),
                      Emplacement(538, 302),
                      Emplacement(323, 302),
                      Emplacement(143, 319, state="Mine")]
        super().__init__(parent, *args, **kwargs)


class MainSelectLevel(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        # Définiton des variables
        self.backImg = tk.PhotoImage(
            file="view/src/background/MainSelectLevels.png")
        self.rootWidth = self.backImg.width()
        self.rootHeight = self.backImg.height()

        # Instance de la Frame
        tk.Frame.__init__(self, parent)

        self.levels = tk.StringVar(self)

        self.canvas = tk.Canvas(self, width=self.rootWidth,
                                height=self.rootHeight, highlightthickness=0)
        self.canvas.create_image(0, 0, image=self.backImg, anchor="nw")

        self.makeButtons()

        self.canvas.bind("<Button-1>", self.startLevel)

        self.canvas.pack(side="right", fill='both', expand=True)

    def makeButtons(self):
        self.Level1Btn = tk.Radiobutton(self.canvas, text="Level1", value="Lvl1", variable=self.levels,
                                        bg="#1ea7e1", activebackground="#1ea7e1", selectcolor="#1886b4", borderwidth=2, highlightthickness=0, indicatoron=0, padx=25, pady=5)
        self.Level1Btn.place(x=256, y=450)

        self.Level2Btn = tk.Radiobutton(self.canvas, text="Level2", value="Lvl2", variable=self.levels,
                                        bg="#ffcc00", activebackground="#ffcc00", selectcolor="#cca300", borderwidth=2, highlightthickness=0, indicatoron=0, padx=25, pady=5)
        self.Level2Btn.place(x=600, y=450)

        self.Level3Btn = tk.Radiobutton(self.canvas, text="Level3", value="Lvl3", variable=self.levels,
                                        bg="#73cb4d", activebackground="#73cb4d", selectcolor="#5ab134", borderwidth=2, highlightthickness=0, indicatoron=0, padx=25, pady=5)
        self.Level3Btn.place(x=925, y=450)

        self.Level1Btn.select()

    def startLevel(self, event):
        # if ((event.x-centreducercle.x)**2 + (event.y-centreducercle.y)**2)**(0.5):
        if 390 < event.x < 890 and 500 < event.y < 900:
            self.parent.levels = self.levels.get()
            self.parent.switchFrame(MainMenu)
        elif 242 < event.x < 391 and 285 < event.y < 435:
            self.Level1Btn.select()
        elif 563 < event.x < 714 and 285 < event.y < 435:
            self.Level2Btn.select()
        elif 888 < event.x < 1042 and 285 < event.y < 435:
            self.Level3Btn.select()

# Classe du menu principal


class MainMenu(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        # Définiton des variables
        self.backImg = tk.PhotoImage(file="view/src/background/MainMenu.png")
        self.rootWidth = self.backImg.width()
        self.rootHeight = self.backImg.height()

        # Instance de la Frame
        tk.Frame.__init__(self, parent)

        self.heros = tk.StringVar(self)
        self.quality = tk.IntVar(self)

        self.canvas = tk.Canvas(self, width=self.rootWidth,
                                height=self.rootHeight, highlightthickness=0)
        self.canvas.create_image(0, 0, image=self.backImg, anchor="nw")

        self.makeButtons()

        self.canvas.bind("<Button-1>", self.startGame)

        self.canvas.pack(side="right", fill='both', expand=True)

    def makeButtons(self):
        self.adventurerBtn = tk.Radiobutton(self.canvas, text="Aventurier", value="Aventurier", variable=self.heros,
                                            bg="#1ea7e1", activebackground="#1ea7e1", selectcolor="#1886b4", borderwidth=2, highlightthickness=0, indicatoron=0, padx=25, pady=5)
        self.adventurerBtn.place(x=256, y=450)

        self.gokuBtn = tk.Radiobutton(self.canvas, text="Goku", value="Goku", variable=self.heros,
                                      bg="#ffcc00", activebackground="#ffcc00", selectcolor="#cca300", borderwidth=2, highlightthickness=0, indicatoron=0, padx=25, pady=5)
        self.gokuBtn.place(x=600, y=450)

        self.ichigoBtn = tk.Radiobutton(self.canvas, text="Ichigo", value="Ichigo", variable=self.heros,
                                        bg="#73cb4d", activebackground="#73cb4d", selectcolor="#5ab134", borderwidth=2, highlightthickness=0, indicatoron=0, padx=25, pady=5)
        self.ichigoBtn.place(x=925, y=450)

        self.adventurerBtn.select()

        self.cdiscountBtn = tk.Radiobutton(self.canvas, text="Discount", value=4, variable=self.quality,
                                           borderwidth=2, highlightthickness=0, indicatoron=0, padx=25, pady=5)
        self.cdiscountBtn.place(x=256, y=250)
        self.lowBtn = tk.Radiobutton(self.canvas, text="Low", value=2, variable=self.quality,
                                     borderwidth=2, highlightthickness=0, indicatoron=0, padx=25, pady=5)
        self.lowBtn.place(x=600, y=250)
        self.rtxBtn = tk.Radiobutton(self.canvas, text="RTX ON", value=1, variable=self.quality,
                                     borderwidth=2, highlightthickness=0, indicatoron=0, padx=25, pady=5)
        self.rtxBtn.place(x=925, y=250)

        self.lowBtn.select()

    def startGame(self, event):
        if 390 < event.x < 890 and 500 < event.y < 900:
            if self.parent.heros == None:
                self.parent.heros = self.heros.get()
                self.parent.quality = self.quality.get()
                self.launchProgress()
                if self.parent.levels == "Lvl1":
                    self.parent.switchFrame(Lvl1)
                elif self.parent.levels == "Lvl2":
                    self.parent.switchFrame(Lvl2)
                elif self.parent.levels == "Lvl3":
                    self.parent.switchFrame(Lvl3)
        elif 242 < event.x < 391 and 285 < event.y < 435:
            self.adventurerBtn.select()
        elif 563 < event.x < 714 and 285 < event.y < 435:
            self.gokuBtn.select()
        elif 888 < event.x < 1042 and 285 < event.y < 435:
            self.ichigoBtn.select()

    def launchProgress(self):

        self.progressBar = ttk.Progressbar(
            self.canvas, orient="horizontal", length=400, mode="determinate")
        if self.heros.get() == "Goku":
            self.progressBar["maximum"] = 290
        if self.heros.get() == "Ichigo":
            self.progressBar["maximum"] = 249
        self.progressBar.place(x=440, y=615)

# -----------------Chargement de la vue principale--------------------


class MainApplication(tk.Frame):
    currentFrame = None
    heros = None

    def __init__(self, parent, *args, **kwargs):
        # Instance de la Frame
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Chargement de la Frame de départ
        self.switchFrame(MainSelectLevel)

    # Fonction permettant de passer d'une frame à l'autre en détruisant l'autre
    def switchFrame(self, nframe):
        nlevel = nframe(self, self.parent, heros=self.heros)
        if self.currentFrame:
            self.currentFrame.destroy()
            del self.currentFrame

        self.currentFrame = nlevel
        self.currentFrame.pack(side="top", fill="both", expand=True)
        return nlevel

# -----------------Fonction à executer pour lancer le jeu-------------


def launchApp():
    root = tk.Tk()

    MainApplication(root).pack(side="top", fill="both", expand=True)

    root.title("Tower Run")

    imgicon = tk.PhotoImage(file=os.path.join("view/src/assets/Icon.png"))
    root.tk.call('wm', 'iconphoto', root._w, imgicon)

    root.resizable(False, False)
    root.mainloop()
