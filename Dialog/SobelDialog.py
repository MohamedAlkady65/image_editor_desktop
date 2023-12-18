from customtkinter import *
from .CustomSliderDialog import CustomSliderDialog


class SobelDialog(CustomSliderDialog):

    def __init__(self, ):
        super().__init__(title='Sobel Edge Detection',text="Choose Edge Detection Mode",options_order=5)

    def build_main(self):
        self.radio_var = StringVar(self,'vertical')



        vertical = CTkRadioButton(master=self, text="Vertical", variable=self.radio_var, value="vertical")
        horizontal = CTkRadioButton(master=self, text="Horizontal", variable=self.radio_var, value="horizontal")
        both = CTkRadioButton(master=self, text="Both", variable=self.radio_var, value="both")


        vertical.grid(row=1 , column=0 ,padx=20, pady=10)
        horizontal.grid(row=2, column=0 ,padx=20, pady=10)
        both.grid(row=3, column=0 ,padx=20, pady=10)

        CTkLabel(self,text="").grid(row=4,column=0)



    def _ok_event(self, event=None):
        self._user_input =self.radio_var.get()
        self.grab_release()
        self.destroy()




