import tkinter as tk
class Tower(): 
    x = 0
    y = 0
    lv1 = None
    lv2 = None
    lv3 = None
    last_img = None
    def __init__(self,canvas, x, y ):
        self.canvas=canvas
        self.x=x
        self.y=y
        self.construction()

    def construction(self):
        self.canvas.delete(self.last_img)
        self.last_img = self.canvas.create_image(self.x,self.y,image=self.lv1, anchor="s")
        self.canvas.after(1000000, self.construction, self)
        
    @staticmethod
    def subimage(spritesheet, l, t, r, b):
  
        # canvas=tk.Canvas(root)
        sprite = tk.PhotoImage()
        spritesheet = tk.PhotoImage(file=spritesheet)
        sprite.tk.call(sprite, 'copy', spritesheet, '-from', l, t, r, b, '-to', 0, 0)
        # canvas.create_image(0,0, image=sprite)
        # canvas.pack()
        # root.mainloop()
        return sprite

    @staticmethod
    def test_subimage(spritesheet, l, t, r, b,root):
  
        #root=tk.Tk()
        canvas=tk.Canvas(root)
        sprite = tk.PhotoImage()
        spritesheet = tk.PhotoImage(file=spritesheet)
        sprite.tk.call(sprite, 'copy',spritesheet, '-from', l, t, r, b, '-to', 0, 0)
        canvas.create_image(100,100, image=sprite)
        canvas.pack()
        #root.mainloop()
        return sprite

class Mortier(Tower):

    def __init__(self, canvas, x, y):
        #self.root=tk.Tk()
        self.load()
        Tower.__init__(self, canvas, x, y)
        self.last_img = None
        self.damage=5
        self.speed=1
        self.zone=3
        self.damagetype="fire"      
        #self.spritesheet=tk.PhotoImage(file="towers.png")
        self.lv1
        #self.root.mainloop()
    
    def load(self):
        self.lv1=Tower.subimage("view/src/Mortier.png",3,50,85,142)#,self.root)
        self.lv2=Tower.subimage("view/src/Mortier.png", 91,30,191,142)#,self.root)
        self.lv3=Tower.subimage("view/src/Mortier.png", 203,3,313,142)#,self.root)

class Mage(Tower):
    def __init__(self, canvas, x, y):
        Tower.__init__(self, canvas, x, y)
        self.last_img = None
        self.damage=4
        self.speed=2
        self.zone=1

class FireM(Mage):
    def __init__(self, canvas, x, y):
        #self.root=tk.Tk()
        self.load()
        Mage.__init__(self, canvas, x, y)
        self.damagetype="fire"
        #self.spritesheet=tk.PhotoImage(file="Mage2.png")
        
        #self.root.mainloop()
    
    def load(self):
        self.lv1=self.subimage("view/src/Mage2.png",3,72,69,129)#, self.root)
        self.lv2=self.subimage("view/src/Mage2.png",91,49,191,139)#, self.root)
        self.lv3=self.subimage("view/src/Mage2.png",203,3,313,141)#, self.root)

class WaterM(Mage):
    def __init__(self, canvas, x, y):
        #self.root=tk.Tk()
        self.load()
        Mage.__init__(self, canvas,x,y)
        self.damagetype="water"
        
        #self.root.mainloop()
    
    def load(self):
        self.lv1=self.subimage("view/src/Mage3.png",3,72,82,139)#, self.root)
        self.lv2=self.subimage("view/src/Mage3.png",91,47,195,139)#,self.root)
        self.lv3=self.subimage("view/src/Mage3.png",203,0,323,139)#,self.root)

class EarthM(Mage):
    def __init__(self, canvas, x, y):
        #self.root=tk.Tk()
        self.load()
        Mage.__init__(self, canvas, x, y)
        self.damagetype="earth"
        self.lv1=self.subimage("view/src/Mage1.png",3,62,82,132)#,self.root)
        self.lv2=self.subimage("view/src/Mage1.png",91,47,195,132)#,self.root)
        self.lv3=self.subimage("view/src/Mage1.png",203,0,323,132)#,self.root)
        #self.root.mainloop()
    
    def load(self):
        self.lv1=self.subimage("view/src/Mage1.png",3,62,82,132)#,self.root)
        self.lv2=self.subimage("view/src/Mage1.png",91,47,195,132)#,self.root)
        self.lv3=self.subimage("view/src/Mage1.png",203,0,323,132)#,self.root)

class Archer(Tower):
    def __init__(self,canvas,x,y):
        #self.root=tk.Tk()
        self.load()
        Tower.__init__(self, canvas, x, y)
        self.last_img = None
        self.damage=4
        self.speed=4
        self.zone=1
        self.damagetype="shot"
        #self.root.mainloop()
    
    def load(self):
        self.lv1=self.subimage("view/src/Archer.png",3,51,82,138)#,self.root)
        self.lv2=self.subimage("view/src/Archer.png", 91,35,195,144)#,self.root)
        self.lv3=self.subimage("view/src/Archer.png",203,0,295,144)#, self.root)

    

