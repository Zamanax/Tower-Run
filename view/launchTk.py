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
        self.gagne=tk.PhotoImage(file="view/src/background/Win.png")
        self.perdu=tk.PhotoImage(file="view/src/background/Lose.png")

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
        self.health = tk.IntVar(self.canvas, 1)

        # Chargement du Héros
        if hasattr(selectedHeros, "name"):
            self.heros = selectedHeros
            self.heros.changeStats(self.heros.lv0)
            self.heros.lvl = 0

            self.heros.transfromAnim = self.heros.transformAnim0
            self.heros.idleRight = self.heros.idleRight0
            self.heros.idleLeft = self.heros.idleLeft0
            self.heros.runRight = self.heros.runRight0
            self.heros.runLeft = self.heros.runLeft0
            self.heros.specialMoveRight = self.heros.specialMoveRight0
            self.heros.specialMoveLeft = self.heros.specialMoveLeft0
            self.heros.attackLeft = self.heros.attackLeft0
            self.heros.attackRight = self.heros.attackRight0
            self.heros.death = self.heros.death0
            self.heros.instantMoveAnim = self.heros.instantMoveAnim0

            self.heros.x = 900
            self.heros.y = 250
            self.heros.canvas = self.canvas
            self.heros.parent = self
        else :
            if selectedHeros == "Ichigo":
                self.heros = Ichigo(self, 900, 250, 260, 160, quality=self.parent.quality)
            elif selectedHeros == "Goku":
                self.heros = Goku(self, 900, 250, 260, 160, quality=self.parent.quality)
            else:
                self.heros = Adventurer(self, 900, 250, 260, 160)
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
        self.canvas.bind_all("<KeyPress-Right>",self.heros.reOrient)
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
            if ennemy.state == "die":
                nb +=1
        if nb == len(self.ennemies) and self.waveIndex == len(self.waveDict): # and self.parent.waveIndex == len(self.parent.waveDict) -1:
            self.win = self.canvas.create_image(540,325, image=self.gagne)

            self.restartBtn = tk.Button(self.canvas, text="Restart", command=self.restartGame)
            self.restartBtn.place(x = 400, y = 450)

            self.nextLvlBtn = tk.Button(self.canvas, text="Next Level", command=self.launchNextLvl)
            self.nextLvlBtn.place(x = 600, y = 450)

    def loseGame(self):
        self.lost = self.canvas.create_image(540,325, image=self.perdu)
        self.restartBtn = tk.Button(self.canvas, text="Restart", command=self.restartGame)
        self.restartBtn.place(x = 500, y = 400)

    def restartGame(self):
        self.parent.switchFrame(self.__class__)

    def launchNextLvl(self):
        self.parent.switchFrame(self.nextLvl)
        
    # Fonction nulle contenant dans les autress niveaux les ennemis à charger
    def launchWaves(self):
        pass

    def launchWaves(self, dict):
        for i in range(len(dict)):
            dict[i](self, -50*i, 225, self.heros)
        self.waveIndex += 1

    def nextWave(self):
        if self.waveIndex <= len(self.waveDict) - 1:
            self.launchWaves(self.waveDict[self.waveIndex])

    # Fonction permettant de détruire chaquen entitée chargée par le niveau
    def __del__(self):
        for ennemy in self.ennemies:
            del ennemy
        for el in self.__dict__:
            del el

# -----------------Chargement de la Frame LVL 3 ----------------------
class Lvl3(Lvl):
    image = "view/src/background/Lvl3Background.png"
    gold = 1000
    defaultPath = [keySpot(1200, 225)]

    wave1 = [Skeleton, Skeleton, Skeleton, Skeleton, Skeleton]
    wave2 = [miniSkeleton, Skeleton, miniSkeleton]

    waveDict = [wave1, wave2]

    def __init__(self, parent, *args, **kwargs):
        self.spots=[Emplacement(50,280),
                    Emplacement(130,280),
                    Emplacement(300,280),
                    Emplacement(315,385),
                    Emplacement(510,180),
                    Emplacement(635,180),
                    Emplacement(510,390),
                    Emplacement(635,390),
                    Emplacement(1040,28),
                    Emplacement(860,280),
                    Emplacement(960,280),
                    Emplacement(860,385),
                    Emplacement(860,385),
                    Emplacement(860,485),
                    Emplacement(960,385)]
        return super().__init__(parent, *args, **kwargs)

# -----------------Chargement de la Frame LVL 2 ----------------------
class Lvl2(Lvl):
    image = "view/src/background/Lvl2Background.png"
    gold = 1000
    defaultPath = [keySpot(1200, 225)]

    wave1 = [Skeleton, Skeleton, Skeleton, Skeleton, Skeleton]
    wave2 = [miniSkeleton, Skeleton, miniSkeleton]

    waveDict = [wave1, wave2]

    nextLvl = Lvl3
    def __init__(self, parent, *args, **kwargs):
        self.spots =[Emplacement(77,115),
                    Emplacement(203,108),
                    Emplacement(286,112),
                    Emplacement(571,338),
                    Emplacement(674,341),
                    Emplacement(745,333),
                    Emplacement(858,335),
                    Emplacement(973,334),
                    Emplacement(523,610),
                    Emplacement(636,610),
                    Emplacement(752,607),
                    Emplacement(852,608),
                    Emplacement(955,609),
                    Emplacement(56,373),
                    Emplacement(231,372)]
        return super().__init__(parent, *args, **kwargs)

# -----------------Chargement de la Frame LVL 1 ----------------------
class Lvl1(Lvl):
    image = "view/src/background/Lvl1Background.png"
    gold = 1500
    defaultPath = [keySpot(1200, 225)]

    wave1 = [Skeleton, Totor, Skeleton, Skeleton, Skeleton]
    wave2 = [miniSkeleton, Skeleton, miniSkeleton]

    waveDict = [wave1, wave2]

    nextLvl = Lvl2

    def __init__(self, parent, *args, **kwargs):
        self.spots = [Emplacement(180, 175),
                Emplacement(358, 175),
                Emplacement(574, 175),
                Emplacement(755, 175),
                Emplacement(791, 355),
                Emplacement(538, 355),
                Emplacement(323, 355),
                Emplacement(143, 355, state="Mine")]
        return super().__init__(parent, *args, **kwargs)

class MainSelectLevel(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        self.parent = parent
        # Définiton des variables
        self.backImg = tk.PhotoImage(file="view/src/background/MainSelectLevels.png")
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
        self.Level1Btn = tk.Radiobutton(self.canvas, text="Level1", value="Level1", variable=self.levels,
                                            bg="#1ea7e1", activebackground="#1ea7e1",selectcolor="#1886b4", borderwidth=2, highlightthickness=0, indicatoron=0, padx=25, pady=5)
        self.Level1Btn.place(x=256, y= 450)

        self.Level2Btn = tk.Radiobutton(self.canvas, text="Level2", value="Level2", variable=self.levels,
                                    bg="#ffcc00", activebackground="#ffcc00", selectcolor="#cca300", borderwidth=2, highlightthickness=0, indicatoron=0, padx=25, pady=5)
        self.Level2Btn.place(x=600, y= 450)

        self.Level3Btn = tk.Radiobutton(self.canvas, text="Level3", value="Level3", variable=self.levels,
                                        bg="#73cb4d", activebackground="#73cb4d", selectcolor="#5ab134", borderwidth=2, highlightthickness=0, indicatoron=0, padx=25, pady=5)
        self.Level3Btn.place(x=925, y= 450)

        self.Level1Btn.select()

    def startLevel(self, event):
        #if ((event.x-centreducercle.x)**2 + (event.y-centreducercle.y)**2)**(0.5):
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
                                            bg="#1ea7e1", activebackground="#1ea7e1",selectcolor="#1886b4", borderwidth=2, highlightthickness=0, indicatoron=0, padx=25, pady=5)
        self.adventurerBtn.place(x=256, y= 450)

        self.gokuBtn = tk.Radiobutton(self.canvas, text="Goku", value="Goku", variable=self.heros,
                                      bg="#ffcc00", activebackground="#ffcc00", selectcolor="#cca300", borderwidth=2, highlightthickness=0, indicatoron=0, padx=25, pady=5)
        self.gokuBtn.place(x=600, y= 450)

        self.ichigoBtn = tk.Radiobutton(self.canvas, text="Ichigo", value="Ichigo", variable=self.heros,
                                        bg="#73cb4d", activebackground="#73cb4d", selectcolor="#5ab134", borderwidth=2, highlightthickness=0, indicatoron=0, padx=25, pady=5)
        self.ichigoBtn.place(x=925, y= 450)

        self.adventurerBtn.select()

        self.cdiscountBtn = tk.Radiobutton(self.canvas, text="Discount", value=4, variable=self.quality, borderwidth=2, highlightthickness=0, indicatoron=0, padx=25, pady=5)
        self.cdiscountBtn.place(x=256, y=250)
        self.lowBtn = tk.Radiobutton(self.canvas, text="Low", value=2, variable=self.quality, borderwidth=2, highlightthickness=0, indicatoron=0, padx=25, pady=5)
        self.lowBtn.place(x=600, y=250)
        self.rtxBtn = tk.Radiobutton(self.canvas, text="RTX ON", value=1, variable=self.quality, borderwidth=2, highlightthickness=0, indicatoron=0, padx=25, pady=5)
        self.rtxBtn.place(x=925, y=250)

        self.lowBtn.select()

    def startGame(self, event):
        if 390 < event.x < 890 and 500 < event.y < 900:
            if self.parent.heros == None:
                self.parent.heros = self.heros.get()
                self.parent.quality = self.quality.get()
                self.launchProgress()
                self.parent.switchFrame(Lvl1)
        elif 242 < event.x < 391 and 285 < event.y < 435:
            self.adventurerBtn.select()
        elif 563 < event.x < 714 and 285 < event.y < 435:
            self.gokuBtn.select()
        elif 888 < event.x < 1042 and 285 < event.y < 435:
            self.ichigoBtn.select()

    def launchProgress(self):
        
        self.progressBar = ttk.Progressbar(self.canvas,orient="horizontal", length=400, mode="determinate")
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
