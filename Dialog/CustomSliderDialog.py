from customtkinter import *


class CustomSliderDialog(CTkToplevel):

    def __init__(self,
                 title: str = "CTkDialog", text=None, min_value=0, max_value=255, initial_value=None,isreal=False,options_order=3):
        super().__init__()

        self._user_input = None
        self._running = False
        self._title = title
        self._text = text
        self.min_value = min_value
        self.max_value = max_value
        self.isreal = isreal
        self.options_order = options_order
        self.initial_value = min_value if initial_value is None else initial_value
        self.title(self._title)
        self.lift()
        self.attributes("-topmost", True)
        self.protocol("WM_DELETE_WINDOW", self._on_closing)
        self.after(10,
                   self._create_widgets)
        self.resizable(False, False)
        self.grab_set()

    def _create_widgets(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)



        self.build_label()
        self.build_main()
        self.options_btns()


    def build_label(self):
        if self._text is not None:
            self._label = CTkLabel(master=self,
                                   width=300,
                                   wraplength=300,
                                   text=self._text,
                                   )
            self._label.grid(row=0, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

    def build_main(self):
        self.slider_label = CTkLabel(master=self, text=f'{self.initial_value}')

        self.slider_label.grid(row=1, column=0, columnspan=2, padx=20, pady=20, sticky="ew")

        def slider_on_change(v):
            self.slider_label.configure(text="{0:.2f}".format(v) if self.isreal else f"{int(v)}" )

        self.slider = CTkSlider(master=self, from_=self.min_value, to=self.max_value, command=slider_on_change)

        self.slider.set(self.initial_value)

        self.slider.grid(row=2, column=0, columnspan=2, padx=20, pady=(0, 20), sticky="ew")

    def options_btns(self):
        self._ok_button = CTkButton(master=self,
                                    width=100,
                                    border_width=0,
                                    text='Ok',
                                    command=self._ok_event)
        self._ok_button.grid(row=self.options_order, column=0, columnspan=1, padx=(20, 10), pady=(0, 20), sticky="ew")

        self._cancel_button = CTkButton(master=self,
                                        width=100,
                                        border_width=0,
                                        text='Cancel',
                                        command=self._cancel_event)
        self._cancel_button.grid(row=self.options_order, column=1, columnspan=1, padx=(10, 20), pady=(0, 20), sticky="ew")

    def _ok_event(self, event=None):
        self._user_input = self.slider.get()
        self.grab_release()
        self.destroy()

    def _on_closing(self):
        self.grab_release()
        self.destroy()

    def _cancel_event(self):
        self.grab_release()
        self.destroy()

    def get_input(self):
        self.master.wait_window(self)
        return self._user_input
