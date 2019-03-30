import tkinter as tk
backImg = ""
rootWidth = 0
rootHeight = 0

class Lvl1(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        global backImg, rootHeight, rootWidth
        tk.Frame.__init__(self, parent)
        self.parent = parent

        canvas = tk.Canvas(self, width=rootWidth,height=rootHeight,highlightthickness=0)
        canvas.create_image(0,0,image=backImg,anchor="nw")
        canvas.pack(side="right",fill="both",expand="true")


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        self.lvl1 = Lvl1(self, parent)

        self.lvl1.pack()


def launchApp():
    global backImg, rootHeight, rootWidth
    root = tk.Tk()
    backImg = tk.PhotoImage(file="./src/Lvl1Background.png")
    rootWidth=backImg.width()
    rootHeight=backImg.height()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.title("Tower Defense")
    root.resizable(False,False)
    root.mainloop()


if __name__ == "__main__":
    launchApp()
