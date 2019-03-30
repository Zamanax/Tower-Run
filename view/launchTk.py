import tkinter as tk
backImg = ""

#-----------------Chargement de la Frame LVL 1 ----------------------
class Lvl1(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # Définiton des variables
        global backImg
        rootWidth = backImg.width()
        rootHeight = backImg.height()

        # Instance de la Frame
        tk.Frame.__init__(self, parent)
        self.parent = parent

        # Reste du GUI
        canvas = tk.Canvas(self, width=rootWidth,height=rootHeight,highlightthickness=0)
        canvas.create_image(0,0,image=backImg,anchor="nw")
        canvas.pack(side="right",fill="both",expand="true")


#-----------------Chargement de la vue principale--------------------
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        # Instance de la Frame
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # Chargement des Frames voulues
        self.lvl1 = Lvl1(self, parent)

        # Mise en vue principale des vues voulues
        self.lvl1.pack()


def launchApp():
    global backImg
    root = tk.Tk()
    backImg = tk.PhotoImage(file="./src/Lvl1Background.png")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.title("Tower Defense")
    root.resizable(False,False)
    root.mainloop()


if __name__ == "__main__":
    launchApp()
