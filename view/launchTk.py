import tkinter as tk
backImg = ""


class Lvl1(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        canvas = tk.Canvas(self, height=500, width=1000)
        backImg = tk.PhotoImage(file="Lvl1Background.gif")
        canvas.create_image(0, 0, image=backImg, anchor="nw")
        canvas.pack()


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        global backImg
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        canvas = tk.Canvas(self, width=backImg.width(),height=backImg.height())
        canvas.create_image(0,0,image=backImg,anchor="nw")
        # canvas.pack()
        canvas.pack(side="right",fill="both",expand="true")
        # self.lvl1 = Lvl1(self, parent)
        # self.lvl1.pack()


def launchApp():
    global backImg
    root = tk.Tk()
    backImg = tk.PhotoImage(file="Lvl1Background.png")
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.title("Tower Defense")
    root.mainloop()


if __name__ == "__main__":
    launchApp()
