from model.Tower import Tower
import tkinter as tk

class Mortier():
    def __init__(self, canvas, x, y):
        self.last_img = None
        self.damage=5
        self.speed=1
        self.zone=3
        self.damagetype="fire"
        self.canvas=canvas
        self.x=x
        self.y=y
        #self.root=tk.Tk()
        self.spritesheet=tk.PhotoImage(file="view/src/towers.png")
        self.lv1=self.subimage(380, 287, 418, 338).zoom(2)#,self.root)
        self.lv2=self.subimage(420, 290, 465, 338).zoom(2)#,self.root)
        self.lv3=self.subimage(480, 280, 530, 338).zoom(2)#,self.root)
        self.construction()
        #self.root.mainloop()
        # Tower.__init__(canvas, x, y)
        
    # def subimage(self, l, t, r, b):
    #     Tower.subimage(self.spritesheet, l, t, r, b)
    def construction(self):
        self.canvas.delete(self.last_img)
        self.last_img = self.canvas.create_image(self.x,self.y,image=self.lv2, anchor="s")
        self.canvas.after(1000000, self.construction)
    
        
    def subimage(self, l, t, r, b):
        # Création de la variable à retourner
        sprite = tk.PhotoImage()

        # Décupage de l'image en Tcl
        sprite.tk.call(sprite, 'copy', self.spritesheet,
                    '-from', l, t, r, b, '-to', 0, 0)
        return sprite

   
        
