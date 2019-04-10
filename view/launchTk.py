import tkinter as tk
import model.Tower as Tow
import model.Heros as He
import model.Ennemy as Enn

selectedHeros = "Goku"

def refresh(canvas, img):
        canvas.tag_raise(img)
        canvas.after(1,refresh, canvas, img)

class Interface(tk.Frame):
    def __init__(self, parent, canvas, *args, **kwargs):
        self.parent = parent
        self.canvas = canvas

        # Instance de la Frame
        tk.Frame.__init__(self, parent)

        self.backImg = tk.PhotoImage(file="view/src/Lvl1Background.png")
        self.rootWidth = self.backImg.width()
        self.rootHeight = self.backImg.height()
        self.backImg = tk.PhotoImage(file="view/src/Interface.png")
        canvas = tk.Canvas(self, width=200, height=self.rootHeight, highlightthickness=0)
        canvas.create_image(0, 0, image=self.backImg, anchor="nw")
 
        Wallet = tk.Label(canvas, text="Riche", bg="#743A3A", fg="white")
        Wallet.place(x=31,y=617)

        Life = tk.Label(canvas, text="20", bg="#743A3A", fg="white")
        Life.place(x=150,y=617)
        canvas.pack()

# -----------------Chargement de la Frame LVL 1 ----------------------
class Lvl1(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        global selectedHeros
        # Définiton des variables
        self.backImg = tk.PhotoImage(file="view/src/Lvl1Background.png")
        self.rootWidth = self.backImg.width()
        self.rootHeight = self.backImg.height()

        # Instance de la Frame
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Reste du GUI
        canvas = tk.Canvas(self, width=self.rootWidth,
                           height=self.rootHeight, highlightthickness=0)
        canvas.create_image(0, 0, image=self.backImg, anchor="nw")

        if selectedHeros == "Ichigo" :
            heros = He.Ichigo(canvas, 900,250, 260, 160)
        elif selectedHeros == "Goku":
            heros = He.Goku(canvas, 900,250, 260, 160)
        else:
            heros = He.Adventurer(canvas, 900,250, 260, 160)

        Enn.Skeleton(canvas, -100, 225, heros)

        canvas.bind("<Button-3>", heros.mouseMove)
        canvas.bind("<Button-1>", heros.transformTo1)
        canvas.bind('<Key-T>', heros.transformTo2)
        Tow.Mortier(canvas, 400, 170)
        # arc1 = Tow.Archer(canvas, 900, 350)
        # refresh(canvas, arc1.last_img)

        # Début de l'interface
        self.interface = Interface(self, parent, canvas)
        self.interface.pack(side="right", fill="y")

        #---------------Définition des lignes---------------
        # Variable permmetant de définir la grille de la map
        squareFactor = 3
        squareHeight = int(30 * squareFactor)
        squareWidth = int(18 * squareFactor)
        showSquare = False

        # Mise en place de la grid de la map
        if showSquare:
            for i in range(squareHeight):
                canvas.create_line((i+1)*self.rootWidth/squareHeight, 0, (i+1)
                               * self.rootWidth/squareHeight, self.rootHeight, stipple="gray50")
            for i in range(squareWidth):
                canvas.create_line(0, (i+1)*self.rootHeight/squareWidth, self.rootWidth,
                               (i+1)*self.rootHeight/squareWidth, stipple="gray50")
        
        canvas.pack(side="right", fill="both", expand="true")


# -----------------Chargement de la vue principale--------------------
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # Instance de la Frame
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Chargement des Frames voulues
        self.lvl1 = Lvl1(self, parent)

        # Mise en vue principale des vues voulues
        self.lvl1.pack()


# -----------------Fonction à executer pour lancer le jeu-------------
def launchApp():
    root = tk.Tk()

    MainApplication(root).pack(side="top", fill="both", expand=True)

    root.title("Tower Run")
    root.resizable(False, False)
    root.mainloop()
