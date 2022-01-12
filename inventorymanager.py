from tkinter import * 
from tkinter.ttk import *
from tkinter import ttk as ttk

from sqlite_backend import *
from ttk_frontend import *
from invman_controller import *

class App(Tk):
    def __init__(self):
        super().__init__()
        self.title("Inventory Manager -by Ohbster")
        
        model = Model()
        view = View(self)
        controller = Controller(_model=model,_view=view)
        view.set_controller(controller)
        view.draw_main()
        
        
if __name__ == '__main__':
    app = App()
    app.mainloop()
