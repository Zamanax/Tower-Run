import tkinter as tk
import model.Tower as Tow
import tkinter.ttk as ttk


class Interface(tk.Frame):

    # ____________________________Dico avec pour clé le nom de la tour (méthode spé __str__) et pour valeur elle même______
    dico = {"Mage d'Eau": Tow.WaterM, "Mage de Terre": Tow.EarthM, "Mage de Feu": Tow.FireM, "Archer": Tow.Archer,
            "Mortier": Tow.Mortier, "Forgeron": Tow.Forgeron}

    selected = None
    last_preview = None
    last_lochoice = None
    range_preview = None
    spotName = None
    spotZone = None
    spotSpeed = None
    spotDamage = None
    spotDamagetype = None

    def __init__(self, parent, *args, **kwargs):
        self.lochoice = tk.PhotoImage(file="view/src/lochoice.png")
        self.hammerSign = tk.PhotoImage(file="view/src/HammerSign.png")
        self.parent = parent
        self.canvas = parent.canvas

        # Instance de la Frame
        tk.Frame.__init__(self, parent)
        self.v = tk.StringVar()
        # self.v.set("00000000Archer")

        self.backImg = tk.PhotoImage(file="view/src/Interface.png")
        self.interface = tk.Canvas(
            self, width=200, height=650, highlightthickness=0)
        self.interface.create_image(0, 0, image=self.backImg, anchor="nw")
        self.makeLabel()
        self.emplacementMake()
        self.interface.pack()

        self.makeButton()

# ___________________________On va faire les check buttons ici max/yann ______________
    def makeButton(self):
        self.waterchb = tk.Radiobutton(self.interface, value="Mage d'Eau", variable=self.v,
                                       bg="#1ea7e1", activebackground="#1ea7e1", highlightthickness=0)
        self.waterchb.place(x=160, y=23)
        self.earthchb = tk.Radiobutton(self.interface, value="Mage de Terre", variable=self.v,
                                       bg="#73cd4b", activebackground="#73cd4b", highlightthickness=0)
        self.earthchb.place(x=160, y=81)
        self.firechb = tk.Radiobutton(self.interface, value="Mage de Feu", variable=self.v,
                                      bg="#e86a17", activebackground="#e86a17", highlightthickness=0)
        self.firechb.place(x=160, y=135)
        self.archerchb = tk.Radiobutton(self.interface, value="Archer", variable=self.v,
                                        bg="#ffcc00", activebackground="#ffcc00", highlightthickness=0)
        self.archerchb.place(x=160, y=191)
        self.mortierchb = tk.Radiobutton(self.interface, value="Mortier", variable=self.v,
                                         bg="#eeeeee", activebackground="#eeeeee", highlightthickness=0)
        self.mortierchb.place(x=160, y=246)
        self.forgeronchb = tk.Radiobutton(
            self.interface, value=Tow.Forgeron, text="F", variable=self.v)
        self.forgeronchb.place(x=160, y=300)
        self.waterchb.select()  # on choisit les mages d'eaux par défaut au début
        self.buildButton = tk.Button(
            self.interface, command=self.buildTower, text="Construire", width=24)
        self.buildButton.place(x=12, y=585)

    def makeLabel(self):
        self.wallet = tk.Label(
            self.interface, textvariable=self.parent.gold, bg="#743A3A", fg="white")
        self.wallet.place(x=31, y=617)

        self.life = tk.Label(self.interface, textvariable=self.parent.health,
                             bg="#743A3A", fg="white", font=("Arial", 8))
        self.life.place(x=150, y=617)

        self.mageWPrice = tk.Label(
            self.interface, text="50", bg="#1ea7e1", fg="black", font=("Arial", 8))
        self.mageWPrice.place(x=75, y=26)

        self.mageEPrice = tk.Label(
            self.interface, text="50", bg="#73cd4b", fg="black", font=("Arial", 8))
        self.mageEPrice.place(x=75, y=82)

        self.mageFPrice = tk.Label(
            self.interface, text="50", bg="#e86a17", fg="black", font=("Arial", 8))
        self.mageFPrice.place(x=75, y=137)

        self.archerPrice = tk.Label(
            self.interface, text="50", bg="#ffcc00", fg="black", font=("Arial", 8))
        self.archerPrice.place(x=75, y=192)

        self.mortierPrice = tk.Label(
            self.interface, text="50", bg="#eeeeee", fg="black", font=("Arial", 8))
        self.mortierPrice.place(x=75, y=250)

    def selectSpot(self, event):
        state = ''.join([i for i in self.v.get() if not i.isdigit()])
        area = 45
        for spot in self.parent.spots:
            if spot.x-area < event.x < spot.x+area and spot.y-area < event.y < spot.y+area:
                self.canvas.delete(self.range_preview)
                self.half_range = self.dico[state].range
                self.range_preview = self.canvas.create_oval(spot.x+self.half_range, spot.y+self.half_range, spot.x - self.half_range, spot.y - self.half_range,
                                                             outline="blue")
                self.canvas.delete(self.last_lochoice)
                self.selected = spot
                self.last_lochoice = self.canvas.create_image(
                    spot.x, spot.y, image=self.lochoice)
                found = True
                break
        if found != True:
            self.selected = None
        self.preView()

    def preView(self):
        if self.selected:
            if self.spotName:
                self.spotName.destroy()
            if self.spotDamage:
                self.spotDamage.destroy()
            if self.spotSpeed:
                self.spotSpeed.destroy()
            if self.spotZone:
                self.spotZone.destroy()
            if self.spotDamagetype:
                self.spotDamagetype.destroy()

            self.spotName = tk.Label(self.interface, text="Nom: ", bg="#743A3A", fg="white")
            self.spotName.place(x=10, y=300)
            
            self.interface.delete(self.last_preview)
            
            if self.selected.tower:

                self.spotDamage = tk.Label(self.interface, text="Dégâts: ", bg="#743A3A", fg="white")
                self.spotZone = tk.Label(self.interface, text="Zone de dégâts: ", bg="#743A3A", fg="white")
                self.spotDamagetype = tk.Label(self.interface, text="Type de dégâts: ", bg="#743A3A", fg="white")
                self.spotSpeed = tk.Label(self.interface, text="Cadence de tir: ", bg="#743A3A", fg="white")

                self.spotDamage.place(x=10, y=320)
                self.spotZone.place(x=10, y=340)
                self.spotDamagetype.place(x=10, y=360)
                self.spotSpeed.place(x=10, y=380)

                if self.selected.tower.lvl == 1:
                    self.last_preview = self.interface.create_image(
                        100, 450, image=self.selected.tower.lv1)
                elif self.selected.tower.lvl == 2:
                    self.last_preview = self.interface.create_image(
                        100, 450, image=self.selected.tower.lv2)
                elif self.selected.tower.lvl == 3:
                    self.last_preview = self.interface.create_image(
                        100, 450, image=self.selected.tower.lv3)
                        
                self.spotName["text"] += str(self.selected.tower)
                self.spotDamage["text"] += str(self.selected.tower.damage)
                self.spotZone["text"] += str(self.selected.tower.zone)
                self.spotDamagetype["text"] += str(self.selected.tower.damagetype)
                self.spotSpeed["text"] += str(self.selected.tower.speed)
                
            else:
                self.last_preview = self.interface.create_image(
                    100, 450, image=self.hammerSign)
                self.spotName["text"] += "Emplacement Vide"

    def buildTower(self):
        state = ''.join([i for i in str(self.v.get()) if not i.isdigit()])

        if self.selected:
            if self.selected.state != "None":
                self.canvas.delete(self.selected.last_img)
                self.selected.tower.upgrade()

            else:
                if state == "Forgeron":
                    self.selected.state = state
                    self.canvas.delete(self.selected.last_img)
                    self.selected.tower = self.dico[state](
                        self.canvas, self.selected.x, self.selected.y, self.parent.heros)

                else:
                    self.selected.state = state
                    self.canvas.delete(self.selected.last_img)
                    self.selected.tower = self.dico[state](
                        self.canvas, self.selected.x, self.selected.y)

            self.preView()

    def emplacementMake(self):
        for spot in self.parent.spots:
            if spot.state == "None":
                spot.last_img = self.canvas.create_image(
                    spot.x, spot.y, image=self.hammerSign, anchor="s")
