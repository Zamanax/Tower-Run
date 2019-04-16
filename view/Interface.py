import tkinter as tk        
import model.Tower as Tow

class Interface(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        self.hammerSign = tk.PhotoImage(file="view/src/HammerSign.png")
        self.parent = parent
        self.canvas = parent.canvas

        # Instance de la Frame
        tk.Frame.__init__(self, parent)
        self.v=tk.StringVar()
        #self.v.set("00000000Archer")

        self.backImg = tk.PhotoImage(file="view/src/Interface.png")
        self.interface = tk.Canvas(self, width=200, height=650, highlightthickness=0)
        self.interface.create_image(0, 0, image=self.backImg, anchor="nw")
        self.makeLabel()
        self.emplacementMake()
        self.interface.pack()
#___________________________On va faire les check buttons ici max/yann ______________
        self.waterchb= tk.Radiobutton(self.interface,value=Tow.WaterM, variable=self.v, bg="#1ea7e1")
        self.waterchb.place(x=160, y=23)
        self.earthchb=tk.Radiobutton(self.interface,value=Tow.EarthM, variable=self.v, bg="#73cd4b")
        self.earthchb.place(x=160, y=81)
        self.firechb=tk.Radiobutton(self.interface,value=Tow.FireM, variable=self.v, bg="#e86a17")
        self.firechb.place(x=160, y=135)
        self.archerchb=tk.Radiobutton(self.interface,value=Tow.Archer, variable=self.v, bg="#ffcc00")
        self.archerchb.place(x=160, y=191)
        self.mortierchb=tk.Radiobutton(self.interface,value=Tow.Mortier, variable=self.v, bg="#eeeeee")
        self.mortierchb.place(x=160, y=246)
        self.forgeronchb=tk.Radiobutton(self.interface, value=Tow.Forgeron, text="F", variable=self.v)
        self.forgeronchb.place(x=160, y=300)
        self.archerchb.select() #on choisit les archers par défaut au début c tt

#____________________________Dico avec pour clé le nom de la tour (méthode spé __str__) et pour valeur elle même______
        self.dico={"WaterM":Tow.WaterM, "EarthM": Tow.EarthM, "FireM": Tow.FireM, "Archer": Tow.Archer, 
        "Mortier":Tow.Mortier, "Forgeron":Tow.Forgeron}

    def makeLabel(self):
        self.wallet = tk.Label(self.interface, textvariable=self.parent.gold, bg="#743A3A", fg="white")
        self.wallet.place(x=31,y=617)

        self.life = tk.Label(self.interface, textvariable=self.parent.health, bg="#743A3A", fg="white", font=("Arial",8))
        self.life.place(x=150,y=617)

        self.mageWPrice = tk.Label(self.interface, text="50", bg="#1ea7e1", fg="black", font=("Arial",8))
        self.mageWPrice.place(x=75,y=26)

        self.mageEPrice = tk.Label(self.interface, text="50", bg="#73cd4b", fg="black", font=("Arial",8))
        self.mageEPrice.place(x=75,y=82)

        self.mageFPrice = tk.Label(self.interface, text="50", bg="#e86a17", fg="black",font=("Arial",8))
        self.mageFPrice.place(x=75,y=137)   

        self.archerPrice = tk.Label(self.interface, text="50", bg="#ffcc00", fg="black", font=("Arial",8))
        self.archerPrice.place(x=75,y=192)

        self.mortierPrice = tk.Label(self.interface, text="50", bg="#eeeeee", fg="black", font=("Arial",8))
        self.mortierPrice.place(x=75,y=250)

    def selectSpot(self, event):
        area = 45
        for spot in self.parent.spots:
            if spot.x-area < event.x < spot.x+area and spot.y-area < event.y < spot.y+area:
                self.selected = spot
                self.buildTower()
                return

    def buildTower(self):
        l=len(self.v.get())
        state=self.v.get()[8:l]
        #print(state)
        if self.selected :
            if self.selected.state != "None":
                self.canvas.delete(self.selected.last_img)
                self.selected.tower.upgrade()
                return
            else:
                if state=="Forgeron":
                    self.selected.state = state
                    self.canvas.delete(self.selected.last_img)
                    self.selected.tower = self.dico[state](self.canvas, self.selected.x, self.selected.y, self.parent.heros)
                    return
                else:
                    self.selected.state = state
                    self.canvas.delete(self.selected.last_img)
                    self.selected.tower = self.dico[state](self.canvas, self.selected.x, self.selected.y)
                return

    def emplacementMake(self):
        for spot in self.parent.spots:
            if spot.state == "None":
                spot.last_img = self.canvas.create_image(spot.x, spot.y, image=self.hammerSign, anchor="s")

# if spot.state != "None":
#     self.canvas.delete(spot.last_img)
#     spot.tower.upgrade()
#     return
# else:
#     spot.state = "Mortier"
#     self.canvas.delete(spot.last_img)
#     spot.tower = Tow.Mortier(self.canvas, spot.x, spot.y)
#     return