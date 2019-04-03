import tkinter as tk
class Tower(): 
    x = 0
    y = 0
    #inutile
    def __init__(self,canvas, x, y ):
        self.damage=0
        self.damagetype="shot"
        self.zone=0
        self.speed=1
        self.canvas=canvas
        # self.x=x
        # self.y=y
        self.construction()
        self.lv1= tk.PhotoImage()
        
    def construction(self):
        self.canvas.create_image(self.x,self.y,image=self.lv1, anchor="s")
        
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
        sprite.tk.call(sprite, 'copy', spritesheet, '-from', l, t, r, b, '-to', 0, 0)
        canvas.create_image(0,0, image=sprite)
        canvas.pack()
        #root.mainloop()
        return sprite

