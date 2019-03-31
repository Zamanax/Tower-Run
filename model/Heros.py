import tkinter as tk
from model.Character import Character

class Heros(Character):

    def __init__(self, master):
        tk.Canvas.__init__(self,master, bg="white", highlightthickness=0)
        self.team = "ally"
        self.hp = 30
        self.name = "Heros"
        self.speed = 5
        self.attackSpeed = 2
        self.state = "idle"

        self.spritesheet = tk.PhotoImage(file="view/src/Adventurer.png")

        self.getSprite(self)
    
    @staticmethod
    def getSprite(self):
        self.num_sprintes = 13
        self.last_img = None
        self.images = [self.subimage(self, 32*i, 0, 32*(i+1), 32) for i in range(self.num_sprintes)]
        self.updateimage(self, 0)

    @staticmethod
    def subimage(self, l, t, r, b):
        dst = tk.PhotoImage()
        dst.tk.call(dst, 'copy', self.spritesheet, '-from', l, t, r, b, '-to', 0, 0)
        return dst

    @staticmethod
    def updateimage(self, sprite):
        self.delete(self.last_img)
        self.last_img = self.create_image(16, 8, image=self.images[sprite])
        self.after(150, self.updateimage, self,(sprite+1) % self.num_sprintes)
