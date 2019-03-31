import tkinter as tk
from model.Character import Character


class Heros(Character):

    def __init__(self, master, x, y):
        # tk.Canvas.__init__(self,master, bg="white", highlightthickness=0)
        # self.config(height=32,width=32)
        self.x = x
        self.y = y
        self.canvas = master
        self.team = "ally"
        self.hp = 30
        self.name = "Heros"
        self.speed = 5
        self.attackSpeed = 2
        self.state = "idle"       
        self.last_img = None


        self.spritesheet = tk.PhotoImage(file="view/src/Adventurer.png")

        self.getSprite(self)

    @staticmethod
    def getSprite(self):
        self.num_sprintes = 13
        self.images = [self.subimage(self, 32*i, 0, 32*(i+1), 32)
                       for i in range(self.num_sprintes)]
        # self.updateimage( 0, self.x, self.y)

    @staticmethod
    def subimage(self, l, t, r, b):
        dst = tk.PhotoImage()
        dst.tk.call(dst, 'copy', self.spritesheet,
                    '-from', l, t, r, b, '-to', 0, 0)
        return dst

    def updateimage(self, sprite, x, y):
        #self.delete(self.last_img)
        self.canvas.delete(self.last_img)
        self.last_img = self.canvas.create_image(x, y, image=self.images[sprite])

        self.canvas.after(150, self.updateimage, ((sprite+1) % self.num_sprintes), self.x, self.y)

    def update(self, x, y):
        self.updateimage(0, self.x, self.y)