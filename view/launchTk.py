import tkinter as tk
from model.Heros import Heros

# -----------------Chargement de la Frame LVL 1 ----------------------
class Lvl1(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # Définiton des variables
        self.backImg = tk.PhotoImage(file="view/src/Lvl1Background.png")
        rootWidth = self.backImg.width()
        rootHeight = self.backImg.height()

        # Instance de la Frame
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Reste du GUI
        canvas = tk.Canvas(self, width=rootWidth,
                           height=rootHeight, highlightthickness=0)
        canvas.create_image(0, 0, image=self.backImg, anchor="nw")
        
        heros = Heros(canvas, 900,250)
    
        canvas.bind("<Button-3>", heros.mouseMove)
        #---------------Définition des lignes---------------
        # Variable permmetant de définir la grille de la map
        squareFactor = 3
        squareHeight = int(30 * squareFactor)
        squareWidth = int(18 * squareFactor)
        showSquare = False

        # Mise en place de la grid de la map
        if showSquare:
            for i in range(squareHeight):
                canvas.create_line((i+1)*rootWidth/squareHeight, 0, (i+1)
                               * rootWidth/squareHeight, rootHeight, stipple="gray50")
            for i in range(squareWidth):
                canvas.create_line(0, (i+1)*rootHeight/squareWidth, rootWidth,
                               (i+1)*rootHeight/squareWidth, stipple="gray50")
        
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

    root.title("Tower Defense")
    # root.wm_attributes("-transparentcolor", "white")
    root.resizable(False, False)
    root.mainloop()
    return root


if __name__ == "__main__":
    launchApp()
