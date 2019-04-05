import tkinter as tk


class Tower():
    x = 0
    y = 0
    lv1 = None
    lv2 = None
    lv3 = None
    last_img = None

    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.construction()
        # self.refresh()

    def construction(self):
        self.canvas.delete(self.last_img)
        self.last_img = self.canvas.create_image(
            self.x, self.y, image=self.lv1, anchor="s")
        self.canvas.tag_raise(self.last_img)

        self.canvas.after(1000000, self.construction, self)

    # def refresh(self):
    #     self.canvas.tag_raise(self.last_img)
    #     self.canvas.after(1,self.refresh)

    @staticmethod
    def subimage(spritesheet, l, t, r, b):

        # canvas=tk.Canvas(root)
        sprite = tk.PhotoImage()
        spritesheet = tk.PhotoImage(file=spritesheet)
        sprite.tk.call(sprite, 'copy', spritesheet,
                       '-from', l, t, r, b, '-to', 0, 0)
        # canvas.create_image(0,0, image=sprite)
        # canvas.pack()
        # root.mainloop()
        return sprite

    @staticmethod
    def test_subimage(spritesheet, l, t, r, b, root):

        # root=tk.Tk()
        canvas = tk.Canvas(root)
        sprite = tk.PhotoImage()
        spritesheet = tk.PhotoImage(file=spritesheet)
        sprite.tk.call(sprite, 'copy', spritesheet,
                       '-from', l, t, r, b, '-to', 0, 0)
        canvas.create_image(100, 100, image=sprite)
        canvas.pack()
        # root.mainloop()
        return sprite

    @staticmethod    
    def load(coords, image):
        return Tower.subimage(image, coords[0], coords[1], coords[2], coords[3])  # , self.root)

class Mortier(Tower):
    
    coordsLvl1=[ 16, 54, 85, 142]
    coordsLvl2=[ 91, 30, 191, 142]
    coordsLvl3=[ 203, 3, 313, 142]
    image="view/src/Mortier.png"

    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        
        self.lv1=self.load(self.coordsLvl1, self.image)
        self.lv2=self.load(self.coordsLvl2, self.image)
        self.lv3=self.load(self.coordsLvl3, self.image)

        Tower.__init__(self, canvas, x, y)
        self.damage = 5
        self.speed = 1
        self.zone = 3
        self.damagetype = "fire"
        # self.spritesheet=tk.PhotoImage(file="towers.png")
        # self.root.mainloop()
    
    

class Mage(Tower):
    def __init__(self, canvas, x, y):
        Tower.__init__(self, canvas, x, y)
        self.damage = 4
        self.speed = 2
        self.zone = 1


class FireM(Mage):
    
    coordsLvl1 = [3, 72, 69, 129]
    coordsLvl2 = [91, 49, 191, 139]
    coordsLvl3 = [203, 3, 313, 141]
    image="view/src/Mage2.png"

    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        self.lv1=self.load(self.coordsLvl1, self.image)
        self.lv2=self.load(self.coordsLvl2, self.image)
        self.lv3=self.load(self.coordsLvl3, self.image)
        Mage.__init__(self, canvas, x, y)
        self.damagetype = "fire"
        # self.spritesheet=tk.PhotoImage(file="Mage2.png")

        # self.root.mainloop()

class WaterM(Mage):
    coordsLvl1=[3,72,82,139]
    coordsLvl2=[91,47,195,139]
    coordsLvl3=[203,0,323,139]
    image="view/src/Mage3.png"
    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        self.lv1=self.load(self.coordsLvl1, self.image)
        self.lv2=self.load(self.coordsLvl2, self.image)
        self.lv3=self.load(self.coordsLvl3, self.image)
        Mage.__init__(self, canvas, x, y)
        self.damagetype = "water"

        # self.root.mainloop()


class EarthM(Mage):
    image="view/src/Mage1.png"
    coordsLvl1 = [3, 62, 82, 132]
    coordsLvl2= [91, 47, 195, 132]
    coordsLvl3 = [203, 0, 323, 132]

    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        self.lv1=self.load(self.coordsLvl1, self.image)
        self.lv2=self.load(self.coordsLvl2, self.image)
        self.lv3=self.load(self.coordsLvl3, self.image)
        Mage.__init__(self, canvas, x, y)
        self.damagetype = "earth"
        
    # self.root.mainloop()

    

class Archer(Tower):
    image="view/src/Archer.png"
    coordsLvl1 = [3,51,82,138]
    coordsLvl2= [91,35,195,144]
    coordsLvl3 = [203,0,295,144]
    def __init__(self, canvas, x, y):
        # self.root=tk.Tk()
        self.lv1=self.load(self.coordsLvl1, self.image)
        self.lv2=self.load(self.coordsLvl2, self.image)
        self.lv3=self.load(self.coordsLvl3, self.image)
        Tower.__init__(self, canvas, x, y)
        self.damage = 4
        self.speed = 4
        self.zone = 1
        self.damagetype = "shot"
        # self.root.mainloop()


