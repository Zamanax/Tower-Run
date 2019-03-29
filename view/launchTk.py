import Tkinter as tk
import sys

class Lvl1(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        canvas = tk.Canvas(self, height=500, width=1000)
        backImg = tk.PhotoImage("Lvl1Background.gif")
        canvas.create_image(0,0,image=backImg,anchor="nw")
        canvas.pack()
        
class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        # canv = tk.Canvas(self, height=500, width=1000)
        # backImg = tk.PhotoImage("Lvl1Background.gif")
        # canv.create_image(0,0,image=backImg,anchor="nw")
        # canv.pack(side="right", fill="both", expand=True)
        self.Lvl1 = Lvl1(self,parent)
        self.Lvl1.pack()

def launchApp():
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.title("Tower Defense")
    root.mainloop()

if __name__ == "__main__":
    launchApp()
