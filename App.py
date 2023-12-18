from customtkinter import CTk
from Controller import Controller
from Model import Model
from View import View

class App(CTk):

    def __init__(self):

        super().__init__()
        view = View(self)
        model = Model()
        controller = Controller(view,model)
        view.init(controller)


    def run(self):
        self.mainloop()
