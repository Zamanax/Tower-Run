import tkinter as tk
def load(coords, image):
    return subimage(image, coords[0], coords[1], coords[2], coords[3])  # , self.root)


def subimage(spritesheet, l, t, r, b):

        
    sprite = tk.PhotoImage()
    spritesheet = tk.PhotoImage(file=spritesheet)
    sprite.tk.call(sprite, 'copy', spritesheet,
                    '-from', l, t, r, b, '-to', 0, 0)
    
    return sprite


def test_subimage(spritesheet, l, t, r, b, root):

    # root=tk.Tk()
    canvas = tk.Canvas(root)
    sprite = tk.PhotoImage()
    spritesheet = tk.PhotoImage(file=spritesheet)
    sprite.tk.call(sprite, 'coy', spritesheet,
                    '-from', l, t, r, b, '-to', 0, 0)
    canvas.create_image(100, 100, image=sprite)
    canvas.pack()
    # root.mainloop()
    return sprite

def coeffdirecteur(object1x,object1y, object2):
    try:
        return (object1y-object2.y)/(object1x-object2.x)
    except ZeroDivisionError:
        return "x"