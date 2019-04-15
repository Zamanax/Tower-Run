import tkinter as tk
import view.Interface as View
import model.Tower as Tow
import model.Heros as He
import model.Ennemy as Enn


def refresh(canvas, img):
        canvas.tag_raise(img)
        canvas.after(1,refresh, canvas, img)

class Emplacement():
    bonus = {}
    state = "None"
    last_img = None
    tower = None
    def __init__(self, x, y, *args, **kwargs):
        state = kwargs.get('state', None)
        bonus = kwargs.get('bonus', None)
        self.x = x
        self.y = y
        if state:
            self.state = state
        if bonus: 
            self.bonus = bonus

# -----------------Chargement de la Frame LVL 1 ----------------------
class Lvl1(tk.Frame):
    canvas = None
    def __init__(self, parent, *args, **kwargs):
        self.selectedHeros = "Ichigo"
        self.spots = []
        self.spotsImage = []
        self.fillspots(self.spots)
        # Définiton des variables
        self.backImg = tk.PhotoImage(file="view/src/Lvl1Background.png")
        self.rootWidth = self.backImg.width()
        self.rootHeight = self.backImg.height()

        # Instance de la Frame
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Reste du GUI
        self.canvas = tk.Canvas(self, width=self.rootWidth,
                           height=self.rootHeight, highlightthickness=0)
        self.canvas.create_image(0, 0, image=self.backImg, anchor="nw")

        if self.selectedHeros == "Ichigo" :
            heros = He.Ichigo(self, 900, 250, 260, 160)
        elif self.selectedHeros == "Goku":
            heros = He.Goku(self, 900, 250, 260, 160)
        else:
            heros = He.Adventurer(self, 900, 250, 260, 160)

        Enn.Skeleton(self, 0, 225, heros)
        Enn.Skeleton(self, -100, 225, heros)
        Enn.Skeleton(self, -50, 225, heros)
        Enn.Skeleton(self, -150, 225, heros)
        Enn.Skeleton(self, -200, 225, heros)
        Enn.Skeleton(self, 50, 225, heros)

        self.gold = tk.IntVar(self.canvas,300)
        self.health = tk.IntVar(self.canvas, 20)

        self.canvas.bind("<Button-3>", heros.mouseMove)
        # Tow.Mortier(canvas, 400, 170)
        # Tow.Archer(canvas, 400, 350)
        # refresh(canvas, arc1.last_img)

        # Début de l'interface
        self.interface = View.Interface(self)
        self.canvas.bind("<Button-1>", self.interface.selectSpot)
        self.canvas.bind("<Button-2>", heros.transform)

        self.interface.pack(side="right", fill="y")
        self.canvas.pack(side="right", fill='both', expand=True)

    @staticmethod
    def fillspots(dict):
        dict.append(Emplacement(180,170))
        dict.append(Emplacement(358,170))
        dict.append(Emplacement(574,170))
        dict.append(Emplacement(755,170))
        dict.append(Emplacement(791,350))
        dict.append(Emplacement(538,350))
        dict.append(Emplacement(323,350))
        dict.append(Emplacement(143,350))

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

# -----------------Chargement de la vue principale--------------------
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # Instance de la Frame
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Chargement des Frames voulues
        self.lvl1 = Lvl1(self, parent)

        # Mise en vue principale des vues voulues
        self.lvl1.pack(side="top", fill="both", expand=True)


# -----------------Fonction à executer pour lancer le jeu-------------
def launchApp():
    root = tk.Tk()

    MainApplication(root).pack(side="top", fill="both", expand=True)

    root.title("Tower Run")
    root.resizable(False, False)
    root.mainloop()
