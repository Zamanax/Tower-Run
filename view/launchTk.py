import tkinter as tk
import controller.Interface as View
import model.Tower as Tow
import model.Heros as He
import model.Ennemy as Enn


def refresh(canvas, img):
        canvas.tag_raise(img)
        canvas.after(1,refresh, canvas, img)

class Emplacement():
    bonus = {}
    state = None
    last_img = None
    tower = None
    def __init__(self, x, y, *args, **kwargs):
        state = kwargs.get('state', None)
        bonus = kwargs.get('bonus', None)
        tower = kwargs.get('tower', None)
        parent = kwargs.get('parent', None)
        self.x = x
        self.y = y
        if state:
            self.state = state
            dico = {"Mage d'Eau": Tow.WaterM, "Mage de Terre": Tow.EarthM, "Mage de Feu": Tow.FireM, "Archer": Tow.Archer,
            "Mortier": Tow.Mortier, "Forgeron": Tow.Forgeron, "Mine": Tow.Mine}
            self.tower = dico[state](parent, x, y)
        if bonus: 
            self.bonus = bonus
        if tower:
            self.tower = tower

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
        

        # Reste du GUI
        self.canvas = tk.Canvas(self, width=self.rootWidth,
                           height=self.rootHeight, highlightthickness=0)
        self.canvas.create_image(0, 0, image=self.backImg, anchor="nw")

        self.gold = tk.IntVar(self.canvas, self.gold)
        self.health = tk.IntVar(self.canvas, 20)

        self.fillspots(self.spots)
        
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

    def fillspots(self, dict):
        pass

    def launchWaves(self):
        pass

# -----------------Chargement de la Frame LVL 1 ----------------------
class Lvl1(Lvl):
    heros = "Aventurier"
    image = "view/src/Lvl1Background.png"
    gold = 1000

    def launchWaves(self):
        Enn.Skeleton(self, 0, 225, self.heros)
        Enn.Skeleton(self, -100, 225, self.heros)
        Enn.Skeleton(self, -50, 225, self.heros)
        Enn.Skeleton(self, -150, 225, self.heros)
        Enn.Skeleton(self, 50, 225, self.heros)        

    def fillspots(self, dict):
        dict.append(Emplacement(180,175))
        dict.append(Emplacement(358,175))
        dict.append(Emplacement(574,175))
        dict.append(Emplacement(755,175))
        dict.append(Emplacement(791,355))
        dict.append(Emplacement(538,355))
        dict.append(Emplacement(323,355))
        dict.append(Emplacement(143,355, parent=self, state="Mine"))

# -----------------Chargement de la Frame LVL 2 ----------------------
class Lvl2(Lvl):
    heros = "Aventurier"
    image = "view/src/Lvl2Background.png"
    gold = 1000
    
    def launchWaves(self):
        Enn.Skeleton(self, 0, 225, self.heros)
        Enn.Skeleton(self, -100, 225, self.heros)
        Enn.Skeleton(self, -50, 225, self.heros)
        Enn.Skeleton(self, -150, 225, self.heros)
        Enn.Skeleton(self, 50, 225, self.heros)        

    def fillspots(self, dict):
        dict.append(Emplacement(180,175))
        dict.append(Emplacement(358,175))
        dict.append(Emplacement(574,175))
        dict.append(Emplacement(755,175))
        dict.append(Emplacement(791,355))
        dict.append(Emplacement(538,355))
        dict.append(Emplacement(323,355))
        dict.append(Emplacement(143,355, parent=self, state="Mine"))

# -----------------Chargement de la vue principale--------------------
class MainApplication(tk.Frame):
    currentFrame = None

    def __init__(self, parent, *args, **kwargs):
        # Instance de la Frame
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.switchFrame(Lvl1)

    def switchFrame(self, nframe):
        if self.currentFrame :
            self.currentFrame.destroy()
            del self.currentFrame

        self.currentFrame = nframe(self, self.parent)
        self.currentFrame.pack(side="top", fill="both", expand=True)


# -----------------Fonction à executer pour lancer le jeu-------------
def launchApp():
    root = tk.Tk()

    MainApplication(root).pack(side="top", fill="both", expand=True)

    root.title("Tower Run")
    root.resizable(False, False)
    root.mainloop()
