import tkinter as tk

#-----------------Chargement de la Frame LVL 1 ----------------------
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
        canvas = tk.Canvas(self, width=rootWidth,height=rootHeight,highlightthickness=0)
        canvas.create_image(0,0,image=self.backImg,anchor="nw")
        for i in range(29):
            canvas.create_line((i+1)*rootWidth/30, 0, (i+1)*rootWidth/30, rootHeight)
        for i in range(18):
            canvas.create_line(0,(i+1)*rootHeight/18, rootWidth, (i+1)*rootHeight/18)
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


#-----------------Fonction à executer pour lancer le jeu-------------
def launchApp():
    root = tk.Tk()

    MainApplication(root).pack(side="top", fill="both", expand=True)
    
    root.title("Tower Defense")
    root.resizable(False,False)
    root.mainloop()

if __name__ == "__main__":
    launchApp()