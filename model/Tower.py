import tkinter as tk
class Tower(): 
    x = 0
    y = 0
    def __init__(self,canvas, x, y ):
        self.canvas=canvas
        self.x=x
        self.y=y
        self.construction()
        
    def construction(self):
        self.last_img = self.canvas.create_image(self.x,self.y,image=self.lv1, anchor="s")
        
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
        Tower.__init__(self, canvas, x, y)
        self.last_img = None
        self.damage=5
        self.speed=1
        self.zone=3
        self.damagetype="fire"      
        #self.spritesheet=tk.PhotoImage(file="towers.png")
        self.lv1=self.subimage("towers.png",380, 287, 418, 338).zoom(2)#,self.root)
        self.lv2=self.subimage("towers.png", 420, 290, 465, 338).zoom(2)#,self.root)
        self.lv3=self.subimage("towers.png", 480, 280, 530, 338).zoom(2)#,self.root)
        #self.root.mainloop()


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
        Mage.__init__(self, canvas, x, y)
        self.damagetype="fire"
        #self.spritesheet=tk.PhotoImage(file="Mage2.png")
        self.lv1=self.subimage("Mage2.png",3,72,69,129)#, self.root)
        self.lv2=self.subimage("Mage2.png",91,49,191,139)#, self.root)
        self.lv3=self.subimage("Mage2.png",203,3,313,141)#, self.root)
        self.root.mainloop()


    
        


