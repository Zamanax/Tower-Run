from Tower import Tower
import tkinter as tk

class Mortier(Tower):
    def __init__(self,canvas, x, y ):
        self.damage=5
        self.speed=1
        self.zone=3
        self.damagetype="fire"
        #self.root=tk.Tk()
        #self.spritesheet=tk.PhotoImage(file="towers.png")
        self.lv1=Tower.subimage("../view/src/towers.png",380,287,418,338)#,self.root)
        self.lv2=Tower.subimage("../view/src/towers.png",420, 290, 465, 338)#,self.root)
        self.lv3=Tower.subimage("../view/src/towers.png",480,280,530,338)#,self.root)
        #self.root.mainloop()
        Tower.__init__(canvas, x, y)
        
    # def subimage(self, l, t, r, b):
    #     Tower.subimage(self.spritesheet, l, t, r, b)


    
        
        
   
        
