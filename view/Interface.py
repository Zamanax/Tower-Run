import tkinter as tk        
import model.Tower as Tow

class Interface(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        self.hammerSign = tk.PhotoImage(file="view/src/HammerSign.png")
        self.parent = parent
        self.canvas = parent.canvas

        # Instance de la Frame
        tk.Frame.__init__(self, parent)

        self.backImg = tk.PhotoImage(file="view/src/Interface.png")
        self.interface = tk.Canvas(self, width=200, height=650, highlightthickness=0)
        self.interface.create_image(0, 0, image=self.backImg, anchor="nw")
        self.makeLabel()
        self.emplacementMake()
        self.interface.pack()

    def makeLabel(self):
        self.wallet = tk.Label(self.interface, text="0", bg="#743A3A", fg="white")
        self.wallet.place(x=31,y=617)

        self.life = tk.Label(self.interface, text="20", bg="#743A3A", fg="white", font=("Arial",8))
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

    def buildTower(self, event):
        area = 25
        for spot in self.parent.spots:
            if spot.x-area < event.x < spot.x+area and spot.y-area < event.y < spot.y+area:
                if spot.state != "None":
                    self.canvas.delete(spot.last_img)
                    spot.tower.upgrade()
                    return
                else:
                    spot.state = "Mortier"
                    self.canvas.delete(spot.last_img)
                    spot.tower = Tow.Mortier(self.canvas, spot.x, spot.y)
                    return

    def emplacementMake(self):
        for spot in self.parent.spots:
            if spot.state == "None":
                spot.last_img = self.canvas.create_image(spot.x, spot.y, image=self.hammerSign, anchor="s")