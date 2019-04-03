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
        sprite.tk.call(sprite, 'copy', spritesheet, '-from', l, t, r, b, '-to', 0, 0)
        canvas.create_image(0,0, image=sprite)
        canvas.pack()
        #root.mainloop()
        return sprite

