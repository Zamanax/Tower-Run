from model.Tower import Tower
import tkinter as tk

class Mortier(Tower):
    def __init__(self, canvas, x, y):
        Tower.__init__(self, canvas, x, y):
        self.last_img = None
        self.damage=5
        self.speed=1
        self.zone=3
        self.damagetype="fire"
        self.canvas=canvas
        #self.root=tk.Tk()
        self.spritesheet=tk.PhotoImage(file="view/src/towers.png")
        self.lv1=self.subimage(380, 287, 418, 338).zoom(2)#,self.root)
        self.lv2=self.subimage(420, 290, 465, 338).zoom(2)#,self.root)
        self.lv3=self.subimage(480, 280, 530, 338).zoom(2)#,self.root)
        self.construction()
        #self.root.mainloop()
        # Tower.__init__(canvas, x, y)
        
    
        

   
        
