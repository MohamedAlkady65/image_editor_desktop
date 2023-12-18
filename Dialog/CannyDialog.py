from .CustomSliderDialog import CustomSliderDialog
from .SliderPart import SliderPart

class CannyDialog(CustomSliderDialog):

    def __init__(self, ):
        super().__init__(title='Canny Edge Detection', options_order=7)

    def build_main(self):
        self.kernal_size = SliderPart(master=self, title="Kernal Size", min=3, max=7, initial=3, order=1, )
        self.min = SliderPart(master=self, title="Minimum Value", min=0, max=255, initial=100, order=3, )
        self.max = SliderPart(master=self, title="Maximum Value", min=0, max=255, initial=200, order=5, )

    def _ok_event(self, event=None):
        kernal_size = int(self.kernal_size.get())
        min_value = int(self.min.get())
        max_value = int(self.max.get())
        kernal_size = kernal_size + (1 if kernal_size % 2 == 0 else 0)


        self._user_input = (kernal_size, min_value, max_value,)

        self.grab_release()
        self.destroy()



