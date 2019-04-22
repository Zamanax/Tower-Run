import tkinter as tk
import controller.Interface as View
import model.Tower as Tow
import model.Heros as He
import model.Ennemy as Enn
from model.fonctions_utiles import subimage

def refresh(canvas, img):
        canvas.tag_raise(img)
        canvas.after(1,refresh, canvas, img)

class Emplacement():
    bonus = {}
    state = None
    tower = None
    last_img = None

    def __init__(self, x, y, *args, **kwargs):
        state = kwargs.get('state', None)
        bonus = kwargs.get('bonus', None)

        self.x = x
        self.y = y

        if state:
            self.state = state
        if bonus: 
            self.bonus = bonus
            

class Lvl(tk.Frame):
    heros = None
    spots = []
    image = None

    def __init__(self, parent,*args, **kwargs):
        self.selectedHeros = self.heros
        # Définiton des variables

        self.backImg = tk.PhotoImage(file=self.image)
        self.rootWidth = self.backImg.width()
        self.rootHeight = self.backImg.height()

        # Instance de la Frame
        tk.Frame.__init__(self, parent)
    
        self.upImage = "view/src/Storm_evolution.png"
        self.upAnim = [subimage(self.upImage, 200*i, 0, 200*(i+1), 200)
                     for i in range(6)]

        # Reste du GUI
        self.canvas = tk.Canvas(self, width=self.rootWidth,
                           height=self.rootHeight, highlightthickness=0)
        self.canvas.create_image(0, 0, image=self.backImg, anchor="nw")

        self.gold = tk.IntVar(self.canvas, self.gold)
        self.health = tk.IntVar(self.canvas, 20)
        
        if self.selectedHeros == "Ichigo":
            self.heros = He.Ichigo(self, 900, 250, 260, 160)
        elif self.selectedHeros == "Goku":
            self.heros = He.Goku(self, 900, 250, 260, 160)
        else:
            self.heros = He.Adventurer(self, 900, 250, 260, 160)

        self.launchWaves()
        # Début de l'interface
        self.interface = View.Interface(self)

        # Bind du clic gauche et droit pour l'interface et les déplacements du héros
        self.canvas.bind("<Button-1>", self.interface.selectSpot)
        self.canvas.bind("<Button-3>", self.heros.mouseMove)

        self.interface.pack(side="right", fill="y")
        self.canvas.pack(side="right", fill='both', expand=True)

    def makeLigns(self):
        #---------------Définition des lignes---------------
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

    def launchWaves(self):
        pass

    def __del__(self):
        for ennemy in Enn.ennemies:
            del ennemy
        del Enn.ennemies
        for el in self.__dict__:
            del el

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
    heros = "Aventurier"
    image = "view/src/Lvl1Background.png"
    gold = 1000
    spots = [Emplacement(180,175),
        Emplacement(358,175),
        Emplacement(574,175),
        Emplacement(755,175),
        Emplacement(791,355),
        Emplacement(538,355),
        Emplacement(323,355),
        Emplacement(143,355, state="Mine")]

    def launchWaves(self):
        Enn.Skeleton(self, 0, 225, self.heros)
        Enn.Skeleton(self, -100, 225, self.heros)
        Enn.Skeleton(self, -50, 225, self.heros)
        Enn.Skeleton(self, -150, 225, self.heros)
        Enn.Skeleton(self, 50, 225, self.heros)        

# -----------------Chargement de la Frame LVL 2 ----------------------
class Lvl2(Lvl):
    heros = "Aventurier"
    image = "view/src/Lvl2Background.png"
    gold = 1000
    spots = [Emplacement(180,175),
        Emplacement(358,175),
        Emplacement(574,175),
        Emplacement(755,175),
        Emplacement(791,355),
        Emplacement(538,355),
        Emplacement(323,355),
        Emplacement(143,355, state="Mine")]

    def launchWaves(self):
        Enn.Skeleton(self, 0, 225, self.heros)
        Enn.Skeleton(self, -100, 225, self.heros)
        Enn.Skeleton(self, -50, 225, self.heros)
        Enn.Skeleton(self, -150, 225, self.heros)
        Enn.Skeleton(self, 50, 225, self.heros)        

# -----------------Chargement de la vue principale--------------------
class MainApplication(tk.Frame):
    currentFrame = None

    def __init__(self, parent, *args, **kwargs):
        # Instance de la Frame
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.switchFrame(Lvl1)

        # tk.Button(self, text="pass", command=self.launchLvl2).place(x=200,y=200)

    def switchFrame(self, nframe):
        nlevel = nframe(self, self.parent)
        if self.currentFrame :
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
