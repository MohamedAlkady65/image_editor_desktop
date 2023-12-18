from customtkinter import  CTkSlider,CTkLabel

class SliderPart():
    def __init__(self,master,initial,min,max,title,order,isReal=False):

        def on_change(v):
            s = "{0:.2f}".format(v)
            self.label.configure(text=f"{title} : { s if isReal else int(v)}")

        self.slider = CTkSlider(master=master, from_=min, to=max,command=on_change)
        self.slider.set(initial)
        self.slider.grid(row=order+1, column=0, columnspan=2, padx=20, pady=(10,20) ,sticky="ew")


        self.label = CTkLabel(master=master, text=f"{title}: {initial}")
        self.label.grid(row=order, column=0, columnspan=2, padx=20,pady=(10,0),  sticky="ew")

    def get(self):
        return self.slider.get()
