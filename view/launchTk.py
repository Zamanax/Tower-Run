import Tkinter as tk

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent

        canv = tk.Canvas(height=500, width=1000)
        canv.pack()
    
def launchApp():
    root = tk.Tk()
    MainApplication(root).pack(side="top", fill="both", expand=True)
    root.title("Tower Defense")
    root.mainloop()

if __name__ == "__main__":
    launchApp()
